import { useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "sonner";
import Shell from "@/components/Shell";
import api from "@/lib/api";
import { ROOM_TYPES, BUDGET_PRESETS, PALETTES, formatINR } from "@/lib/constants";
import { Upload, ArrowRight, ArrowLeft, Loader2, Wand2, Check, X } from "lucide-react";

const STEPS = ["Upload", "Room Type", "Budget", "Palette", "Requirements"];

export default function CreateWizard() {
  const [step, setStep] = useState(0);
  const [imageData, setImageData] = useState(null); // base64 incl data url for preview
  const [imageRaw, setImageRaw] = useState(null);   // raw base64 for backend
  const [roomType, setRoomType] = useState("Living Room");
  const [budget, setBudget] = useState(200000);
  const [palette, setPalette] = useState("Warm Beige");
  const [requirements, setRequirements] = useState("");
  const [generating, setGenerating] = useState(false);
  const [drag, setDrag] = useState(false);
  const fileRef = useRef(null);
  const nav = useNavigate();

  const handleFile = (file) => {
    if (!file) return;
    if (!/^image\/(jpe?g|png|webp)$/i.test(file.type)) {
      toast.error("Please upload a JPG, PNG, or WEBP image.");
      return;
    }
    if (file.size > 20 * 1024 * 1024) {
      toast.error("Image must be under 20MB.");
      return;
    }
    const reader = new FileReader();
    reader.onload = (e) => {
      const data = e.target.result;
      setImageData(data);
      setImageRaw(String(data).split(",")[1]);
    };
    reader.readAsDataURL(file);
  };

  const canNext = () => {
    if (step === 0) return !!imageRaw;
    return true;
  };

  const generate = async () => {
    if (!imageRaw) { toast.error("Please upload a room photo."); setStep(0); return; }
    setGenerating(true);
    try {
      // Stage 1: kick off async image-generation job (returns job_id immediately)
      const { data: started } = await api.post("/design/generate", {
        image_base64: imageRaw,
        room_type: roomType,
        budget,
        color_palette: palette,
        requirements,
      });
      const jobId = started.job_id;
      if (!jobId) throw new Error("No job id returned");

      // Poll for completion (each poll is a quick GET, well under the 30s edge timeout)
      let generatedImage = null;
      const start = Date.now();
      const MAX_MS = 180000;     // 3 minutes ceiling
      const POLL_MS = 3000;      // poll every 3s
      while (Date.now() - start < MAX_MS) {
        await new Promise(r => setTimeout(r, POLL_MS));
        const { data: status } = await api.get(`/design/status/${jobId}`);
        if (status.status === "done") { generatedImage = status.generated_image; break; }
        if (status.status === "error") throw new Error(status.error || "Generation failed");
      }
      if (!generatedImage) throw new Error("Generation timed out. Please try again.");

      // Stage 2: analysis (parallel on backend, ~10s — well under 30s)
      const { data: an } = await api.post("/design/analyze", {
        room_type: roomType,
        budget,
        color_palette: palette,
        requirements,
      });

      sessionStorage.setItem("kr_last_result", JSON.stringify({
        generated_image: generatedImage,
        furniture_estimate: an.furniture_estimate,
        total_cost: an.total_cost,
        space_analysis: an.space_analysis,
        vastu_report: an.vastu_report,
        vastu_score: an.vastu_score,
        original_image: imageRaw,
        room_type: roomType,
        budget,
        color_palette: palette,
        requirements,
      }));
      nav("/result");
    } catch (err) {
      toast.error(err?.response?.data?.detail || err?.message || "Generation failed. Please try again.");
      setGenerating(false);
    }
  };

  if (generating) return <LoadingScreen/>;

  return (
    <Shell>
      <div style={{maxWidth:880, margin:"0 auto"}}>
        {/* Stepper */}
        <div style={{display:"flex", alignItems:"center", gap:8, marginBottom:28, flexWrap:"wrap"}}>
          {STEPS.map((s, i) => (
            <div key={s} style={{display:"flex", alignItems:"center", gap:8}}>
              <div data-testid={`step-${i}`} style={{
                width:28, height:28, borderRadius:9999, display:"grid", placeItems:"center",
                background: i <= step ? "#FF7A00" : "#fff",
                color: i <= step ? "#fff" : "#9CA3AF",
                border: "1px solid " + (i <= step ? "#FF7A00" : "#E5E7EB"),
                fontWeight:800, fontSize:13,
              }}>{i < step ? <Check size={14}/> : i+1}</div>
              <div style={{fontSize:13, fontWeight: i === step ? 700 : 500, color: i === step ? "#0A0A0A" : "#6B7280"}}>{s}</div>
              {i < STEPS.length - 1 && <div style={{width:24, height:1, background:"#E5E7EB"}}/>}
            </div>
          ))}
        </div>

        <div className="card-solid fade-in-up" style={{padding:28}}>
          {step === 0 && (
            <Step0 imageData={imageData} drag={drag} setDrag={setDrag} fileRef={fileRef} handleFile={handleFile} clear={() => { setImageData(null); setImageRaw(null); }}/>
          )}
          {step === 1 && <Step1 value={roomType} onChange={setRoomType}/>}
          {step === 2 && <Step2 value={budget} onChange={setBudget}/>}
          {step === 3 && <Step3 value={palette} onChange={setPalette}/>}
          {step === 4 && <Step4 value={requirements} onChange={setRequirements}/>}
        </div>

        <div style={{display:"flex", justifyContent:"space-between", marginTop:24}}>
          <button data-testid="wizard-back-btn" className="btn-ghost" onClick={() => setStep(Math.max(0, step-1))} disabled={step === 0}>
            <ArrowLeft size={16}/> Back
          </button>
          {step < STEPS.length - 1 ? (
            <button data-testid="wizard-next-btn" className="btn-primary" onClick={() => setStep(step+1)} disabled={!canNext()}>
              Next <ArrowRight size={16}/>
            </button>
          ) : (
            <button data-testid="wizard-generate-btn" className="btn-primary" onClick={generate}>
              <Wand2 size={16}/> Generate design
            </button>
          )}
        </div>
      </div>
    </Shell>
  );
}

function Step0({ imageData, drag, setDrag, fileRef, handleFile, clear }) {
  return (
    <div>
      <div className="kr-label" style={{color:"#FF7A00"}}>Step 1</div>
      <h2 className="font-display" style={{fontSize:30, fontWeight:900, letterSpacing:"-0.02em", margin:"4px 0 6px"}}>Upload your empty room</h2>
      <p style={{color:"#6B7280", marginBottom:24}}>JPG, PNG, or WEBP. Up to 20MB. Brighter, wider angles work best.</p>

      {!imageData ? (
        <div
          data-testid="upload-dropzone"
          className={`dropzone ${drag ? "drag" : ""}`}
          onClick={() => fileRef.current?.click()}
          onDragOver={(e) => { e.preventDefault(); setDrag(true); }}
          onDragLeave={() => setDrag(false)}
          onDrop={(e) => { e.preventDefault(); setDrag(false); handleFile(e.dataTransfer.files?.[0]); }}
        >
          <div style={{width:60, height:60, borderRadius:18, background:"#FFA64D", color:"#fff", display:"grid", placeItems:"center", margin:"0 auto 16px"}}>
            <Upload size={26}/>
          </div>
          <div className="font-display" style={{fontWeight:800, fontSize:20}}>Drag & drop your room photo</div>
          <div style={{color:"#6B7280", marginTop:6}}>or click to browse</div>
          <input ref={fileRef} type="file" accept="image/jpeg,image/jpg,image/png,image/webp" style={{display:"none"}}
                 onChange={(e) => handleFile(e.target.files?.[0])} data-testid="upload-input"/>
        </div>
      ) : (
        <div style={{position:"relative", borderRadius:24, overflow:"hidden", background:"#000"}}>
          <img src={imageData} alt="Uploaded room" style={{width:"100%", maxHeight:480, objectFit:"contain"}}/>
          <button data-testid="upload-clear-btn" onClick={clear} style={{
            position:"absolute", top:14, right:14, width:36, height:36, borderRadius:9999, border:"none",
            background:"rgba(0,0,0,0.6)", color:"#fff", cursor:"pointer", display:"grid", placeItems:"center"
          }}><X size={16}/></button>
        </div>
      )}
    </div>
  );
}

function Step1({ value, onChange }) {
  return (
    <div>
      <div className="kr-label" style={{color:"#FF7A00"}}>Step 2</div>
      <h2 className="font-display" style={{fontSize:30, fontWeight:900, letterSpacing:"-0.02em", margin:"4px 0 24px"}}>Which room is this?</h2>
      <div style={{display:"grid", gridTemplateColumns:"repeat(auto-fit, minmax(160px, 1fr))", gap:14}}>
        {ROOM_TYPES.map(r => (
          <div key={r.id} data-testid={`room-${r.id}`} className={`tile ${value === r.id ? "selected" : ""}`} onClick={() => onChange(r.id)} style={{padding:0, overflow:"hidden"}}>
            <div style={{aspectRatio:"4/3", overflow:"hidden"}}>
              <img src={r.img} alt={r.label} style={{width:"100%", height:"100%", objectFit:"cover"}} loading="lazy"/>
            </div>
            <div style={{padding:"12px 14px", display:"flex", justifyContent:"space-between", alignItems:"center"}}>
              <div style={{fontWeight:700, fontSize:14}}>{r.label}</div>
              {value === r.id && <div style={{width:22, height:22, borderRadius:9999, background:"#FF7A00", color:"#fff", display:"grid", placeItems:"center"}}><Check size={13}/></div>}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function Step2({ value, onChange }) {
  return (
    <div>
      <div className="kr-label" style={{color:"#FF7A00"}}>Step 3</div>
      <h2 className="font-display" style={{fontSize:30, fontWeight:900, letterSpacing:"-0.02em", margin:"4px 0 6px"}}>What's your budget?</h2>
      <p style={{color:"#6B7280", marginBottom:28}}>The AI tunes furniture quality and quantity to match.</p>

      <div style={{textAlign:"center", marginBottom:24}}>
        <div className="font-display gradient-text" style={{fontSize:64, fontWeight:900, letterSpacing:"-0.04em"}}>{formatINR(value)}</div>
        <div className="kr-label">Selected budget</div>
      </div>

      <input type="range" min={25000} max={2500000} step={25000} value={value} onChange={(e) => onChange(parseInt(e.target.value))}
             data-testid="budget-slider" style={{width:"100%", accentColor:"#FF7A00"}}/>

      <div style={{display:"flex", gap:8, flexWrap:"wrap", marginTop:24, justifyContent:"center"}}>
        {BUDGET_PRESETS.map(b => (
          <button key={b.value} data-testid={`budget-${b.value}`} onClick={() => onChange(b.value)} style={{
            padding:"10px 20px", borderRadius:9999, border:"1px solid " + (value === b.value ? "#FF7A00" : "#E5E7EB"),
            background: value === b.value ? "#FF7A00" : "#fff",
            color: value === b.value ? "#fff" : "#0A0A0A",
            fontWeight:600, fontSize:14, cursor:"pointer"
          }}>{b.label}</button>
        ))}
      </div>
    </div>
  );
}

function Step3({ value, onChange }) {
  return (
    <div>
      <div className="kr-label" style={{color:"#FF7A00"}}>Step 4</div>
      <h2 className="font-display" style={{fontSize:30, fontWeight:900, letterSpacing:"-0.02em", margin:"4px 0 24px"}}>Pick a color palette</h2>
      <div style={{display:"grid", gridTemplateColumns:"repeat(auto-fit, minmax(160px, 1fr))", gap:14}}>
        {PALETTES.map(p => (
          <div key={p.id} data-testid={`palette-${p.id}`} className={`swatch ${value === p.id ? "selected" : ""}`} onClick={() => onChange(p.id)}
               style={{background:`linear-gradient(135deg, ${p.colors[0]} 0%, ${p.colors[1]} 60%, ${p.colors[2]} 100%)`, height:140, padding:14}}>
            <div style={{position:"absolute", left:14, bottom:14, padding:"6px 12px", borderRadius:9999, background:"rgba(255,255,255,0.85)", backdropFilter:"blur(6px)"}}>
              <div style={{fontSize:13, fontWeight:700, color:"#0A0A0A"}}>{p.id}</div>
            </div>
            {value === p.id && (
              <div style={{position:"absolute", top:12, right:12, width:24, height:24, borderRadius:9999, background:"#FF7A00", color:"#fff", display:"grid", placeItems:"center"}}><Check size={14}/></div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

function Step4({ value, onChange }) {
  const suggestions = ["Family-friendly with kid-safe corners", "Work-from-home corner with bookshelf", "Pooja shelf in the east wall", "Plenty of indoor plants", "Hidden storage for clutter-free look"];
  return (
    <div>
      <div className="kr-label" style={{color:"#FF7A00"}}>Step 5</div>
      <h2 className="font-display" style={{fontSize:30, fontWeight:900, letterSpacing:"-0.02em", margin:"4px 0 6px"}}>Anything specific?</h2>
      <p style={{color:"#6B7280", marginBottom:20}}>Tell the designer about lifestyle, must-haves, or cultural touches. Optional.</p>
      <textarea data-testid="requirements-input" value={value} onChange={(e) => onChange(e.target.value)} placeholder="e.g., need a pooja corner, kid-friendly sofa, Indo-modern art on accent wall…"
                rows={5} className="input-kr" style={{resize:"vertical", lineHeight:1.55}}/>
      <div style={{display:"flex", gap:8, flexWrap:"wrap", marginTop:14}}>
        {suggestions.map(s => (
          <button key={s} type="button" onClick={() => onChange(value ? value + " · " + s : s)} className="btn-ghost" style={{padding:"6px 12px", fontSize:13, border:"1px solid #E5E7EB"}}>
            + {s}
          </button>
        ))}
      </div>
    </div>
  );
}

function LoadingScreen() {
  const steps = ["Analyzing space…", "Placing furniture…", "Estimating cost…", "Running Vastu analysis…"];
  return (
    <Shell>
      <div style={{display:"grid", placeItems:"center", minHeight:"60vh"}}>
        <div className="card-glass" style={{padding:36, maxWidth:480, width:"100%", textAlign:"center"}} data-testid="loading-card">
          <div className="pulse-orange" style={{width:84, height:84, borderRadius:9999, background:"linear-gradient(135deg,#FF7A00,#FFA64D)", margin:"0 auto", display:"grid", placeItems:"center"}}>
            <Wand2 size={36} color="#fff"/>
          </div>
          <div className="font-display" style={{fontSize:24, fontWeight:900, letterSpacing:"-0.02em", marginTop:22}}>Designing your room…</div>
          <p style={{color:"#6B7280", marginTop:6, fontSize:14}}>This usually takes 30–60 seconds.</p>
          <div style={{marginTop:24, display:"grid", gap:10, textAlign:"left"}}>
            {steps.map(s => (
              <div key={s} style={{display:"flex", alignItems:"center", gap:10, fontSize:14, color:"#374151"}}>
                <div className="spin-slow" style={{width:18, height:18, borderRadius:9999, border:"2px solid #FFE6CC", borderTopColor:"#FF7A00"}}/>
                {s}
              </div>
            ))}
          </div>
        </div>
      </div>
    </Shell>
  );
}
