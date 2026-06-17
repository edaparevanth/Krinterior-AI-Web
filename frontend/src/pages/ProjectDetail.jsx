import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { toast } from "sonner";
import Shell from "@/components/Shell";
import api from "@/lib/api";
import { BeforeAfter } from "@/pages/Result";
import { formatINR } from "@/lib/constants";
import { Pencil, Trash2, Loader2, ArrowLeft, Compass, RefreshCw, Download } from "lucide-react";

export default function ProjectDetail() {
  const { id } = useParams();
  const [p, setP] = useState(null);
  const [tab, setTab] = useState("design");
  const [editing, setEditing] = useState(false);
  const [name, setName] = useState("");
  const [reanalyzing, setReanalyzing] = useState(false);
  const nav = useNavigate();

  useEffect(() => {
    (async () => {
      try {
        const { data } = await api.get(`/projects/${id}`);
        setP(data); setName(data.name);
      } catch { toast.error("Project not found"); nav("/projects"); }
    })();
  }, [id, nav]);

  if (!p) return <Shell><div style={{display:"grid", placeItems:"center", padding:80}}><Loader2 className="spin-slow" color="#FF7A00"/></div></Shell>;

  const rename = async () => {
    try {
      const { data } = await api.patch(`/projects/${id}`, { name });
      setP(data); setEditing(false); toast.success("Renamed");
    } catch { toast.error("Failed to rename"); }
  };

  const del = async () => {
    if (!window.confirm("Delete this project?")) return;
    try { await api.delete(`/projects/${id}`); toast.success("Deleted"); nav("/projects"); } catch {}
  };

  const reanalyze = async () => {
    setReanalyzing(true);
    try {
      const { data } = await api.post("/vastu/analyze", { project_id: id });
      setP({ ...p, vastu_score: data.vastu_score, vastu_report: data.vastu_report });
      toast.success("Vastu re-analyzed");
    } catch { toast.error("Failed"); }
    setReanalyzing(false);
  };

  const downloadImg = () => {
    const a = document.createElement("a");
    a.href = `data:image/png;base64,${p.generated_image}`;
    a.download = `${p.name}.png`;
    a.click();
  };

  return (
    <Shell>
      <div style={{maxWidth:1180, margin:"0 auto"}}>
        <button onClick={() => nav("/projects")} data-testid="back-btn" className="btn-ghost"><ArrowLeft size={16}/> All projects</button>

        <div style={{display:"flex", justifyContent:"space-between", alignItems:"flex-end", marginTop:14, marginBottom:18, flexWrap:"wrap", gap:14}}>
          <div>
            {editing ? (
              <div style={{display:"flex", gap:8}}>
                <input data-testid="rename-input" value={name} onChange={e => setName(e.target.value)} className="input-kr" style={{padding:"10px 14px", maxWidth:300}}/>
                <button onClick={rename} className="btn-primary" style={{padding:"10px 18px"}} data-testid="rename-save">Save</button>
              </div>
            ) : (
              <>
                <div className="kr-label" style={{color:"#FF7A00"}}>{p.room_type} · {p.color_palette}</div>
                <h1 className="font-display" style={{fontSize:"clamp(28px, 4vw, 44px)", fontWeight:900, letterSpacing:"-0.03em", margin:"4px 0 6px"}}>{p.name}</h1>
                <div style={{color:"#6B7280", fontSize:14}}>Budget {formatINR(p.budget)} · Total {formatINR(p.total_cost)}</div>
              </>
            )}
          </div>
          <div style={{display:"flex", gap:10, flexWrap:"wrap"}}>
            <button data-testid="dl-btn" onClick={downloadImg} className="btn-secondary"><Download size={16}/> Download</button>
            <button data-testid="rename-btn" onClick={() => setEditing(!editing)} className="btn-secondary"><Pencil size={14}/> Rename</button>
            <button data-testid="delete-btn" onClick={del} className="btn-secondary" style={{color:"#EF4444", borderColor:"#FECACA"}}><Trash2 size={14}/> Delete</button>
          </div>
        </div>

        {/* Tabs */}
        <div style={{display:"flex", gap:4, marginBottom:18, borderBottom:"1px solid #E5E7EB"}}>
          {[["design","Design"], ["vastu","Vastu"]].map(([k, l]) => (
            <button key={k} data-testid={`tab-${k}`} onClick={() => setTab(k)} style={{
              padding:"12px 18px", border:"none", background:"transparent", cursor:"pointer",
              fontWeight:700, fontSize:14, color: tab === k ? "#FF7A00" : "#6B7280",
              borderBottom: tab === k ? "2px solid #FF7A00" : "2px solid transparent",
              marginBottom:-1
            }}>{l}</button>
          ))}
        </div>

        {tab === "design" && (
          <>
            <BeforeAfter before={p.original_image} after={p.generated_image}/>
            <div className="card-solid" style={{padding:24, marginTop:18}}>
              <div className="kr-label" style={{color:"#FF7A00"}}>Furniture · {formatINR(p.total_cost)}</div>
              {(p.furniture_estimate || []).map((it, i) => (
                <div key={i} style={{display:"flex", justifyContent:"space-between", padding:"12px 0", borderBottom:"1px solid #F5F5F5"}}>
                  <div>
                    <div style={{fontWeight:600, fontSize:14.5}}>{it.name}</div>
                    <div style={{fontSize:11, color:"#9CA3AF", letterSpacing:"0.1em", textTransform:"uppercase", marginTop:2}}>{it.category}</div>
                  </div>
                  <div style={{fontWeight:700}}>{formatINR(it.price_inr)}</div>
                </div>
              ))}
            </div>
          </>
        )}

        {tab === "vastu" && (
          <VastuTab p={p} reanalyze={reanalyze} reanalyzing={reanalyzing}/>
        )}
      </div>
    </Shell>
  );
}

function VastuTab({ p, reanalyze, reanalyzing }) {
  const r = p.vastu_report || {};
  const score = p.vastu_score || 80;
  const color = score >= 85 ? "#10B981" : score >= 70 ? "#F59E0B" : "#EF4444";
  const grade = score >= 90 ? "Excellent" : score >= 75 ? "Good" : score >= 60 ? "Average" : "Poor";

  return (
    <div>
      <div className="card-solid" style={{padding:28, position:"relative", overflow:"hidden"}}>
        <div style={{position:"absolute", inset:0, background:"radial-gradient(circle at 80% 20%, rgba(255,166,77,0.2), transparent 50%)"}}/>
        <div style={{position:"relative", display:"flex", gap:28, alignItems:"center", flexWrap:"wrap"}}>
          <div className="score-ring" style={{"--p": score, "--size":"180px", "--thickness":"16px", background:`conic-gradient(${color} calc(${score} * 1%), #F0F0F0 0)`}}>
            <div style={{textAlign:"center"}}>
              <div className="font-display" style={{fontSize:48, fontWeight:900, letterSpacing:"-0.04em"}}>{score}</div>
              <div style={{fontSize:11, letterSpacing:"0.15em", textTransform:"uppercase", fontWeight:700, color:"#6B7280"}}>/ 100</div>
            </div>
          </div>
          <div style={{flex:1, minWidth:240}}>
            <div className="kr-label" style={{color:"#FF7A00"}}>Vastu Score</div>
            <div className="font-display" style={{fontSize:32, fontWeight:900, color, letterSpacing:"-0.02em", marginTop:4}}>{grade}</div>
            <p style={{color:"#374151", fontSize:15, marginTop:8, lineHeight:1.55}}>{r.summary}</p>
            <button data-testid="vastu-reanalyze-btn" onClick={reanalyze} disabled={reanalyzing} className="btn-primary" style={{marginTop:14, padding:"10px 20px"}}>
              {reanalyzing ? <Loader2 size={14} className="spin-slow"/> : <><RefreshCw size={14}/> Re-analyze</>}
            </button>
          </div>
        </div>
      </div>

      <div style={{display:"grid", gridTemplateColumns:"repeat(auto-fit, minmax(280px, 1fr))", gap:18, marginTop:18}}>
        <VastuList title="Positive aspects" items={r.positive_aspects} color="#10B981"/>
        <VastuList title="Issues to address" items={r.issues} color="#EF4444"/>
        <VastuList title="Recommendations" items={r.recommendations} color="#FF7A00"/>
      </div>

      {r.energy_flow && (
        <div className="card-solid" style={{padding:24, marginTop:18}}>
          <div className="kr-label" style={{color:"#FF7A00"}}>Energy flow</div>
          <p style={{fontSize:15, color:"#374151", marginTop:8, lineHeight:1.6}}>{r.energy_flow}</p>
        </div>
      )}
    </div>
  );
}

function VastuList({ title, items, color }) {
  return (
    <div className="card-solid" style={{padding:20}}>
      <div style={{display:"flex", alignItems:"center", gap:8}}>
        <div style={{width:8, height:8, borderRadius:9999, background:color}}/>
        <div className="kr-label">{title}</div>
      </div>
      <ul style={{padding:0, listStyle:"none", margin:"12px 0 0"}}>
        {(items || []).map((it, i) => (
          <li key={i} style={{display:"flex", gap:10, fontSize:14, color:"#374151", padding:"6px 0", lineHeight:1.5}}>
            <Compass size={14} color={color} style={{marginTop:3, flexShrink:0}}/>{it}
          </li>
        ))}
      </ul>
    </div>
  );
}
