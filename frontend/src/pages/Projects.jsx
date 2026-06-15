import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Shell from "@/components/Shell";
import api from "@/lib/api";
import { formatINR } from "@/lib/constants";
import { Wand2, Trash2, Sparkles } from "lucide-react";
import { toast } from "sonner";

export default function Projects() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);

  const load = async () => {
    setLoading(true);
    try {
      const { data } = await api.get("/projects");
      setProjects(data);
    } catch {}
    setLoading(false);
  };

  useEffect(() => { load(); }, []);

  const del = async (id, e) => {
    e.preventDefault();
    e.stopPropagation();
    if (!window.confirm("Delete this project?")) return;
    try {
      await api.delete(`/projects/${id}`);
      setProjects(projects.filter(p => p.id !== id));
      toast.success("Deleted");
    } catch {
      toast.error("Failed to delete");
    }
  };

  return (
    <Shell>
      <div style={{display:"flex", justifyContent:"space-between", alignItems:"flex-end", marginBottom:24, flexWrap:"wrap", gap:16}}>
        <div>
          <div className="kr-label" style={{color:"#FF7A00"}}>Library</div>
          <h1 className="font-display" style={{fontSize:"clamp(28px, 4vw, 44px)", fontWeight:900, letterSpacing:"-0.03em", margin:"4px 0"}}>Your projects</h1>
          <div style={{color:"#6B7280"}}>{projects.length} design{projects.length === 1 ? "" : "s"}</div>
        </div>
        <Link to="/create" data-testid="projects-new-btn" className="btn-primary"><Wand2 size={16}/> New design</Link>
      </div>

      {loading ? (
        <div style={{display:"grid", gridTemplateColumns:"repeat(auto-fit, minmax(260px, 1fr))", gap:18}}>
          {[1,2,3,4].map(i => <div key={i} className="card-solid" style={{aspectRatio:"4/3"}}/>)}
        </div>
      ) : projects.length === 0 ? (
        <div className="card-solid" style={{padding:60, textAlign:"center"}}>
          <Sparkles size={32} color="#FF7A00" style={{margin:"0 auto"}}/>
          <div className="font-display" style={{fontWeight:800, fontSize:22, marginTop:14}}>No projects yet</div>
          <div style={{color:"#6B7280", marginTop:6}}>Create your first AI-designed room.</div>
          <Link to="/create" className="btn-primary" style={{marginTop:20, display:"inline-flex"}}><Wand2 size={16}/> Create</Link>
        </div>
      ) : (
        <div style={{display:"grid", gridTemplateColumns:"repeat(auto-fit, minmax(280px, 1fr))", gap:18}}>
          {projects.map(p => (
            <Link key={p.id} to={`/project/${p.id}`} data-testid={`project-${p.id}`} style={{textDecoration:"none"}}>
              <div className="card-solid fade-in-up" style={{overflow:"hidden"}}>
                <div style={{aspectRatio:"4/3", background:"linear-gradient(135deg,#FFEAD3,#FFA64D)", display:"grid", placeItems:"center", color:"#fff", position:"relative"}}>
                  <div className="font-display" style={{fontWeight:900, fontSize:26, letterSpacing:"-0.02em"}}>{p.room_type}</div>
                  <button data-testid={`del-${p.id}`} onClick={(e) => del(p.id, e)} style={{position:"absolute", top:12, right:12, width:34, height:34, borderRadius:9999, border:"none", background:"rgba(0,0,0,0.5)", color:"#fff", cursor:"pointer", display:"grid", placeItems:"center"}}>
                    <Trash2 size={14}/>
                  </button>
                </div>
                <div style={{padding:18}}>
                  <div style={{display:"flex", justifyContent:"space-between", alignItems:"center"}}>
                    <div className="font-display" style={{fontWeight:800, fontSize:18, color:"#0A0A0A", letterSpacing:"-0.02em"}}>{p.name}</div>
                    <div style={{
                      padding:"4px 10px", borderRadius:9999, fontSize:11, fontWeight:700,
                      background: p.vastu_score >= 85 ? "#DCFCE7" : p.vastu_score >= 70 ? "#FEF3C7" : "#FEE2E2",
                      color: p.vastu_score >= 85 ? "#166534" : p.vastu_score >= 70 ? "#92400E" : "#991B1B",
                    }}>Vastu {p.vastu_score}</div>
                  </div>
                  <div style={{display:"flex", justifyContent:"space-between", marginTop:8, fontSize:13, color:"#6B7280"}}>
                    <span>{p.color_palette}</span>
                    <span style={{fontWeight:700, color:"#0A0A0A"}}>{formatINR(p.total_cost)}</span>
                  </div>
                </div>
              </div>
            </Link>
          ))}
        </div>
      )}
    </Shell>
  );
}
