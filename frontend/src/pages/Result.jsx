import { useEffect, useMemo, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "sonner";
import Shell from "@/components/Shell";
import api from "@/lib/api";
import { formatINR } from "@/lib/constants";
import { Save, Download, Sparkles, Loader2, ArrowLeftRight, Compass, ShoppingBag } from "lucide-react";

export default function Result() {
  const nav = useNavigate();
  const [data, setData] = useState(null);
  const [saving, setSaving] = useState(false);
  const [name, setName] = useState("");

  useEffect(() => {
    const raw = sessionStorage.getItem("kr_last_result");
    if (!raw) { nav("/create"); return; }
    const parsed = JSON.parse(raw);
    setData(parsed);
    setName(`${parsed.room_type} · ${parsed.color_palette}`);
  }, [nav]);

  if (!data) return null;

  const save = async () => {
    setSaving(true);
    try {
      const { data: p } = await api.post("/projects", {
        name,
        original_image: data.original_image,
        generated_image: data.generated_image,
        room_type: data.room_type,
        budget: data.budget,
        color_palette: data.color_palette,
        requirements: data.requirements,
        furniture_estimate: data.furniture_estimate,
        total_cost: data.total_cost,
        vastu_score: data.vastu_score,
        vastu_report: data.vastu_report,
        space_analysis: data.space_analysis,
      });
      sessionStorage.removeItem("kr_last_result");
      toast.success("Project saved");
      nav(`/project/${p.id}`);
    } catch (err) {
      toast.error(err?.response?.data?.detail || "Failed to save");
    } finally {
      setSaving(false);
    }
  };

  const downloadImg = () => {
    const a = document.createElement("a");
    a.href = `data:image/png;base64,${data.generated_image}`;
    a.download = `${name}.png`;
    a.click();
  };

  return (
    <Shell>
      <div style={{maxWidth:1180, margin:"0 auto"}}>
        <div style={{display:"flex", alignItems:"flex-end", justifyContent:"space-between", flexWrap:"wrap", gap:16, marginBottom:24}}>
          <div>
            <div className="kr-label" style={{color:"#FF7A00"}}>Design ready</div>
            <h1 className="font-display" style={{fontSize:"clamp(28px, 4vw, 44px)", fontWeight:900, letterSpacing:"-0.03em", margin:"4px 0 8px"}}>Your dream room is here.</h1>
            <div style={{color:"#6B7280", fontSize:15}}>{data.room_type} · {data.color_palette} · Budget {formatINR(data.budget)}</div>
          </div>
          <div style={{display:"flex", gap:10, flexWrap:"wrap"}}>
            <button data-testid="result-download-btn" onClick={downloadImg} className="btn-secondary"><Download size={16}/> Download</button>
            <input data-testid="result-name-input" value={name} onChange={e => setName(e.target.value)} className="input-kr" style={{maxWidth:240, padding:"12px 14px"}} placeholder="Project name"/>
            <button data-testid="result-save-btn" onClick={save} disabled={saving} className="btn-primary">
              {saving ? <Loader2 size={16} className="spin-slow"/> : <><Save size={16}/> Save project</>}
            </button>
          </div>
        </div>

        <BeforeAfter before={data.original_image} after={data.generated_image}/>

        <div style={{display:"grid", gridTemplateColumns:"1.2fr 1fr", gap:20, marginTop:24}} className="result-grid">
          <FurnitureList items={data.furniture_estimate} total={data.total_cost} budget={data.budget}/>
          <VastuSummary score={data.vastu_score} report={data.vastu_report}/>
        </div>

        <SpaceAnalysis space={data.space_analysis}/>
        <ShoppingSuggestions items={data.furniture_estimate}/>
      </div>

      <style>{`
        @media (max-width: 900px) {
          .result-grid { grid-template-columns: 1fr !important; }
        }
      `}</style>
    </Shell>
  );
}

export function BeforeAfter({ before, after }) {
  const [pos, setPos] = useState(50);
  const ref = useRef(null);

  const move = (clientX) => {
    if (!ref.current) return;
    const r = ref.current.getBoundingClientRect();
    const p = ((clientX - r.left) / r.width) * 100;
    setPos(Math.max(0, Math.min(100, p)));
  };

  return (
    <div ref={ref} className="card-solid" style={{position:"relative", overflow:"hidden", padding:0, aspectRatio:"16/10", userSelect:"none", touchAction:"none"}}
         data-testid="before-after"
         onMouseMove={(e) => e.buttons === 1 && move(e.clientX)}
         onTouchMove={(e) => move(e.touches[0].clientX)}
    >
      <img src={`data:image/png;base64,${after}`} alt="After" style={{position:"absolute", inset:0, width:"100%", height:"100%", objectFit:"cover"}}/>
      <div style={{position:"absolute", inset:0, width:`${pos}%`, overflow:"hidden"}}>
        <img src={`data:image/png;base64,${before}`} alt="Before" style={{position:"absolute", inset:0, width:`${100 / (pos/100)}%`, height:"100%", objectFit:"cover", maxWidth:"none"}}/>
      </div>
      <div style={{position:"absolute", left:`${pos}%`, top:0, bottom:0, width:2, background:"#FF7A00", transform:"translateX(-1px)"}}/>
      <div style={{position:"absolute", left:`${pos}%`, top:"50%", transform:"translate(-50%, -50%)", width:46, height:46, borderRadius:9999, background:"#fff", boxShadow:"0 6px 16px rgba(0,0,0,0.25)", display:"grid", placeItems:"center", color:"#FF7A00", cursor:"ew-resize"}}>
        <ArrowLeftRight size={18}/>
      </div>
      <input type="range" min={0} max={100} value={pos} onChange={(e) => setPos(parseInt(e.target.value))}
             aria-label="Before after slider" data-testid="ba-range"
             style={{position:"absolute", left:0, right:0, bottom:0, width:"100%", opacity:0, height:50, cursor:"ew-resize"}}/>
      <Badge text="BEFORE" left/>
      <Badge text="AFTER" right/>
    </div>
  );
}

function Badge({ text, left, right }) {
  return (
    <div style={{
      position:"absolute", top:14,
      [left ? "left" : "right"]: 14,
      padding:"6px 12px", borderRadius:9999,
      background:"rgba(255,255,255,0.92)", backdropFilter:"blur(10px)",
      fontSize:11, letterSpacing:"0.2em", fontWeight:800, color:"#0A0A0A"
    }}>{text}</div>
  );
}

function FurnitureList({ items, total, budget }) {
  const matchPct = budget ? Math.round((total / budget) * 100) : 100;
  return (
    <div className="card-solid" style={{padding:24}} data-testid="furniture-card">
      <div className="kr-label" style={{color:"#FF7A00"}}>Furniture estimate</div>
      <div style={{display:"flex", alignItems:"baseline", gap:12, marginTop:6}}>
        <div className="font-display" style={{fontSize:36, fontWeight:900, letterSpacing:"-0.03em"}}>{formatINR(total)}</div>
        <div style={{fontSize:13, color:"#6B7280"}}>Total · {matchPct}% of ₹{(budget/1000).toFixed(0)}K budget</div>
      </div>
      <div style={{marginTop:16, borderTop:"1px solid #F0F0F0"}}>
        {(items || []).map((it, i) => (
          <div key={i} style={{display:"flex", justifyContent:"space-between", padding:"12px 0", borderBottom:"1px solid #F5F5F5", alignItems:"center"}}>
            <div>
              <div style={{fontWeight:600, fontSize:14.5, color:"#0A0A0A"}}>{it.name}</div>
              <div style={{fontSize:12, color:"#9CA3AF", marginTop:2, letterSpacing:"0.05em", textTransform:"uppercase"}}>{it.category}</div>
            </div>
            <div style={{fontWeight:700, fontSize:14, color:"#0A0A0A"}}>{formatINR(it.price_inr)}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

function VastuSummary({ score, report }) {
  const color = score >= 85 ? "#10B981" : score >= 70 ? "#F59E0B" : "#EF4444";
  const grade = score >= 90 ? "Excellent" : score >= 75 ? "Good" : score >= 60 ? "Average" : "Poor";
  return (
    <div className="card-solid" style={{padding:24}} data-testid="vastu-card">
      <div className="kr-label" style={{color:"#FF7A00"}}>Vastu Shastra</div>
      <div style={{display:"flex", gap:20, alignItems:"center", marginTop:14}}>
        <div className="score-ring" style={{"--p": score, "--size":"130px", "--thickness":"12px", background: `conic-gradient(${color} calc(${score} * 1%), #F0F0F0 0)`}}>
          <div style={{textAlign:"center"}}>
            <div className="font-display" style={{fontSize:34, fontWeight:900, letterSpacing:"-0.03em", color:"#0A0A0A"}}>{score}</div>
            <div style={{fontSize:11, color:"#6B7280", letterSpacing:"0.1em", textTransform:"uppercase"}}>/ 100</div>
          </div>
        </div>
        <div>
          <div className="font-display" style={{fontWeight:800, fontSize:22, color, letterSpacing:"-0.02em"}}>{grade}</div>
          <p style={{color:"#374151", fontSize:14, marginTop:6, lineHeight:1.5}}>{report?.summary}</p>
        </div>
      </div>

      {report?.recommendations?.length > 0 && (
        <div style={{marginTop:18}}>
          <div className="kr-label" style={{color:"#0A0A0A"}}>Recommendations</div>
          <ul style={{padding:0, listStyle:"none", marginTop:8}}>
            {report.recommendations.slice(0, 3).map((r, i) => (
              <li key={i} style={{display:"flex", gap:10, fontSize:14, color:"#374151", padding:"6px 0"}}>
                <Compass size={15} color="#FF7A00" style={{flexShrink:0, marginTop:2}}/>{r}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

function SpaceAnalysis({ space }) {
  if (!space) return null;
  return (
    <div className="card-solid" style={{padding:24, marginTop:20}} data-testid="space-card">
      <div className="kr-label" style={{color:"#FF7A00"}}>Space analysis</div>
      <div style={{display:"flex", alignItems:"baseline", gap:10, marginTop:4}}>
        <div className="font-display" style={{fontSize:30, fontWeight:900, letterSpacing:"-0.03em"}}>{space.estimated_size_sqft || "—"} sqft</div>
        <div style={{fontSize:13, color:"#6B7280"}}>Estimated size</div>
      </div>
      <div style={{display:"grid", gridTemplateColumns:"repeat(auto-fit, minmax(220px, 1fr))", gap:20, marginTop:18}}>
        {[
          ["Available zones", space.available_zones],
          ["Design opportunities", space.design_opportunities],
          ["Optimization tips", space.optimization_suggestions],
        ].map(([t, arr]) => (
          <div key={t}>
            <div className="kr-label" style={{color:"#0A0A0A", marginBottom:8}}>{t}</div>
            <ul style={{padding:0, listStyle:"none", margin:0}}>
              {(arr || []).map((it, i) => (
                <li key={i} style={{fontSize:14, color:"#374151", padding:"4px 0", display:"flex", gap:8}}>
                  <Sparkles size={12} color="#FF7A00" style={{marginTop:5, flexShrink:0}}/>{it}
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
}

function ShoppingSuggestions({ items }) {
  if (!items?.length) return null;
  const stores = ["Urban Ladder", "Pepperfry", "IKEA India", "Amazon India"];
  return (
    <div className="card-solid" style={{padding:24, marginTop:20}} data-testid="shopping-card">
      <div style={{display:"flex", justifyContent:"space-between", alignItems:"center"}}>
        <div>
          <div className="kr-label" style={{color:"#FF7A00"}}>Shop the look</div>
          <h3 className="font-display" style={{fontSize:22, fontWeight:900, letterSpacing:"-0.02em", margin:"2px 0 0"}}>Indian retailers</h3>
        </div>
        <ShoppingBag size={22} color="#FF7A00"/>
      </div>
      <div style={{display:"grid", gridTemplateColumns:"repeat(auto-fit, minmax(220px, 1fr))", gap:12, marginTop:16}}>
        {items.slice(0, 6).map((it, i) => {
          const q = encodeURIComponent(it.name);
          return (
            <div key={i} className="card-solid" style={{padding:14, boxShadow:"none", border:"1px solid #F0F0F0"}}>
              <div style={{fontWeight:700, fontSize:14, color:"#0A0A0A"}}>{it.name}</div>
              <div style={{fontSize:12, color:"#6B7280", marginTop:2}}>{formatINR(it.price_inr)}</div>
              <div style={{display:"flex", gap:6, marginTop:10, flexWrap:"wrap"}}>
                {stores.map(s => (
                  <a key={s} href={`https://www.google.com/search?q=${q}+${encodeURIComponent(s)}`} target="_blank" rel="noreferrer"
                     data-testid={`shop-${s}-${i}`}
                     style={{fontSize:11, padding:"5px 10px", borderRadius:9999, border:"1px solid #E5E7EB", color:"#FF7A00", textDecoration:"none", fontWeight:600}}>{s}</a>
                ))}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
