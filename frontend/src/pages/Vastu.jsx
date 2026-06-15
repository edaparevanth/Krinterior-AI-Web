import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Shell from "@/components/Shell";
import api from "@/lib/api";
import { Compass, Loader2, RefreshCw, ArrowRight, Sparkles } from "lucide-react";
import { toast } from "sonner";

const BANNER = "https://static.prod-images.emergentagent.com/jobs/44ee0fce-a68a-45fc-aa10-26ffee77de4f/images/154ac31cf00edc705b727520fcfca1d519b5fa0c302a2d14dbeedf7a1419be9d.png";

export default function Vastu() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selected, setSelected] = useState(null);
  const [report, setReport] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);

  useEffect(() => {
    (async () => {
      try {
        const { data } = await api.get("/projects");
        setProjects(data);
        if (data[0]) setSelected(data[0].id);
      } catch {}
      setLoading(false);
    })();
  }, []);

  const analyze = async (id = selected) => {
    if (!id) return;
    setAnalyzing(true);
    try {
      const { data } = await api.post("/vastu/analyze", { project_id: id });
      setReport(data);
      toast.success("Vastu analysis updated");
    } catch (e) { toast.error("Failed to analyze"); }
    setAnalyzing(false);
  };

  return (
    <Shell>
      <div style={{position:"relative", overflow:"hidden", borderRadius:32, padding:"40px 36px", color:"#fff",
        background:"linear-gradient(120deg, #0a0a0a 0%, #2a1505 80%)"}}>
        <img src={BANNER} alt="" style={{position:"absolute", right:-40, bottom:-40, width:380, opacity:0.45, mixBlendMode:"screen"}}/>
        <div style={{position:"relative"}}>
          <div className="kr-label" style={{color:"#FFA64D"}}>Vastu Shastra</div>
          <h1 className="font-display" style={{fontSize:"clamp(30px, 4vw, 46px)", fontWeight:900, letterSpacing:"-0.03em", margin:"4px 0 12px"}}>Energy & alignment for your home.</h1>
          <p style={{color:"rgba(255,255,255,0.85)", maxWidth:560, lineHeight:1.55}}>Select a saved project to re-evaluate it through ancient Indian Vastu principles. Get a fresh 0-100 score, positive aspects, issues, and concrete corrections.</p>
        </div>
      </div>

      <div style={{display:"grid", gridTemplateColumns:"320px 1fr", gap:24, marginTop:24}} className="vastu-grid">
        <div className="card-solid" style={{padding:18, alignSelf:"start"}}>
          <div className="kr-label" style={{color:"#FF7A00", marginBottom:10}}>Your projects</div>
          {loading ? (
            <div style={{padding:14}}><Loader2 className="spin-slow" color="#FF7A00"/></div>
          ) : projects.length === 0 ? (
            <div style={{padding:14, textAlign:"center"}}>
              <div style={{fontSize:14, color:"#6B7280"}}>No projects yet.</div>
              <Link to="/create" data-testid="vastu-empty-create" className="btn-primary" style={{marginTop:14, display:"inline-flex"}}><Sparkles size={14}/> Create</Link>
            </div>
          ) : (
            <div style={{display:"grid", gap:6}}>
              {projects.map(p => (
                <button key={p.id} data-testid={`vastu-proj-${p.id}`} onClick={() => { setSelected(p.id); setReport(null); }} style={{
                  textAlign:"left", padding:"12px 14px", borderRadius:14, border:"1px solid " + (selected === p.id ? "#FF7A00" : "transparent"),
                  background: selected === p.id ? "#FFF8F1" : "transparent", cursor:"pointer"
                }}>
                  <div style={{fontWeight:700, fontSize:14}}>{p.name}</div>
                  <div style={{fontSize:12, color:"#6B7280", marginTop:2}}>{p.room_type} · Vastu {p.vastu_score}</div>
                </button>
              ))}
            </div>
          )}
        </div>

        <div className="card-solid" style={{padding:28}}>
          {!selected ? (
            <div style={{textAlign:"center", padding:30}}>
              <Compass size={36} color="#FF7A00" style={{margin:"0 auto"}}/>
              <div className="font-display" style={{fontWeight:800, fontSize:22, marginTop:14}}>Select a project</div>
              <div style={{color:"#6B7280", marginTop:6}}>Save a design first to run Vastu analysis.</div>
            </div>
          ) : (
            <>
              <div style={{display:"flex", justifyContent:"space-between", alignItems:"center", flexWrap:"wrap", gap:12}}>
                <div className="font-display" style={{fontSize:22, fontWeight:900, letterSpacing:"-0.02em"}}>
                  {projects.find(p => p.id === selected)?.name}
                </div>
                <div style={{display:"flex", gap:8}}>
                  <Link to={`/project/${selected}`} data-testid="vastu-open-project" className="btn-secondary">Open project <ArrowRight size={14}/></Link>
                  <button onClick={() => analyze()} disabled={analyzing} className="btn-primary" data-testid="vastu-analyze-btn">
                    {analyzing ? <Loader2 size={14} className="spin-slow"/> : <><RefreshCw size={14}/> Analyze</>}
                  </button>
                </div>
              </div>

              {report ? (
                <VastuReport report={report.vastu_report} score={report.vastu_score}/>
              ) : (
                <div style={{textAlign:"center", padding:"60px 20px", color:"#6B7280"}}>
                  <Compass size={28} color="#FF7A00" style={{margin:"0 auto"}}/>
                  <div className="font-display" style={{fontSize:18, fontWeight:800, marginTop:14, color:"#0A0A0A"}}>Click Analyze to refresh insights</div>
                </div>
              )}
            </>
          )}
        </div>
      </div>

      <style>{`@media (max-width: 900px) { .vastu-grid { grid-template-columns: 1fr !important; } }`}</style>
    </Shell>
  );
}

function VastuReport({ report, score }) {
  const color = score >= 85 ? "#10B981" : score >= 70 ? "#F59E0B" : "#EF4444";
  const grade = score >= 90 ? "Excellent" : score >= 75 ? "Good" : score >= 60 ? "Average" : "Poor";
  return (
    <div style={{marginTop:22}}>
      <div style={{display:"flex", gap:24, alignItems:"center", flexWrap:"wrap"}}>
        <div className="score-ring" style={{"--p": score, "--size":"150px", "--thickness":"14px", background:`conic-gradient(${color} calc(${score} * 1%), #F0F0F0 0)`}}>
          <div style={{textAlign:"center"}}>
            <div className="font-display" style={{fontSize:38, fontWeight:900, letterSpacing:"-0.03em"}}>{score}</div>
            <div style={{fontSize:11, color:"#6B7280", letterSpacing:"0.1em", textTransform:"uppercase"}}>/ 100</div>
          </div>
        </div>
        <div style={{flex:1, minWidth:200}}>
          <div className="font-display" style={{fontSize:24, fontWeight:900, color, letterSpacing:"-0.02em"}}>{grade}</div>
          <p style={{fontSize:14, color:"#374151", marginTop:6, lineHeight:1.55}}>{report.summary}</p>
        </div>
      </div>

      <div style={{display:"grid", gridTemplateColumns:"repeat(auto-fit, minmax(220px, 1fr))", gap:14, marginTop:24}}>
        {[
          ["Positive", report.positive_aspects, "#10B981"],
          ["Issues", report.issues, "#EF4444"],
          ["Recommendations", report.recommendations, "#FF7A00"],
        ].map(([t, arr, c]) => (
          <div key={t} style={{padding:16, borderRadius:18, background:"#F8F8F8"}}>
            <div className="kr-label" style={{color:c}}>{t}</div>
            <ul style={{padding:0, listStyle:"none", margin:"10px 0 0"}}>
              {(arr || []).map((it, i) => (
                <li key={i} style={{fontSize:13.5, color:"#374151", padding:"5px 0", display:"flex", gap:8, lineHeight:1.5}}>
                  <Compass size={12} color={c} style={{marginTop:4, flexShrink:0}}/>{it}
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>

      {report.energy_flow && (
        <div style={{marginTop:18, padding:18, borderRadius:18, background:"#FFF8F1", border:"1px solid #FFE6CC"}}>
          <div className="kr-label" style={{color:"#FF7A00"}}>Energy Flow</div>
          <p style={{fontSize:14, color:"#374151", marginTop:6, lineHeight:1.55}}>{report.energy_flow}</p>
        </div>
      )}
    </div>
  );
}
