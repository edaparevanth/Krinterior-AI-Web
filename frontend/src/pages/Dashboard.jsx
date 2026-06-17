import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Shell from "@/components/Shell";
import api from "@/lib/api";
import { useAuth } from "@/contexts/AuthContext";
import { Wand2, Compass, Lightbulb, ArrowRight, Sparkles } from "lucide-react";
import { formatINR } from "@/lib/constants";

export default function Dashboard() {
  const { user } = useAuth();
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    (async () => {
      try {
        const { data } = await api.get("/projects");
        setProjects(data);
      } catch {}
      setLoading(false);
    })();
  }, []);

  const greeting = (() => {
    const h = new Date().getHours();
    if (h < 12) return "Good morning";
    if (h < 18) return "Good afternoon";
    return "Good evening";
  })();

  return (
    <Shell>
      {/* Hero banner */}
      <section className="fade-in-up" style={{position:"relative", overflow:"hidden", borderRadius:32, padding:"40px 36px", color:"#fff",
        background:"linear-gradient(120deg, #1a0f04 0%, #3a1f08 50%, #ff7a00 130%)"}}>
        <div className="kr-label" style={{color:"#FFA64D"}}>{greeting}</div>
        <h1 className="font-display" style={{fontSize:"clamp(30px, 4vw, 48px)", fontWeight:900, margin:"6px 0 18px", letterSpacing:"-0.03em"}}>
          {user?.name || user?.full_name || "There"} — design your dream space.
        </h1>
        <p style={{color:"rgba(255,255,255,0.85)", maxWidth:540, fontSize:15.5, lineHeight:1.5}}>
          Upload an empty room and get a photorealistic furnished design, ₹ cost estimate and Vastu report — in under a minute.
        </p>
        <div style={{marginTop:24, display:"flex", gap:12, flexWrap:"wrap"}}>
          <Link to="/create" data-testid="dash-create-btn" className="btn-primary"><Wand2 size={18}/> Create design</Link>
          <Link to="/projects" data-testid="dash-projects-btn" className="btn-secondary" style={{background:"rgba(255,255,255,0.12)", color:"#fff", borderColor:"rgba(255,255,255,0.25)"}}>
            My projects <ArrowRight size={16}/>
          </Link>
        </div>
        <div style={{position:"absolute", right:-40, bottom:-60, width:280, height:280, borderRadius:"50%", background:"radial-gradient(circle, rgba(255,166,77,0.5), transparent 70%)", filter:"blur(20px)"}}/>
      </section>

      {/* Tool tiles */}
      <section style={{marginTop:32, display:"grid", gridTemplateColumns:"repeat(auto-fit, minmax(260px, 1fr))", gap:18}}>
        {[
          { to: "/create", icon: <Wand2/>, label: "AI Generator", desc: "5-step wizard → photorealistic room.", color:"#FFEAD3", iconBg:"#FF7A00", testId:"tile-generator" },
          { to: "/vastu", icon: <Compass/>, label: "Vastu Shastra", desc: "Re-analyze saved designs for energy flow.", color:"#FFF1E0", iconBg:"#0A0A0A", testId:"tile-vastu" },
          { to: "/projects", icon: <Lightbulb/>, label: "Ideas & Library", desc: "Browse your saved designs.", color:"#F4F4F4", iconBg:"#FFA64D", testId:"tile-ideas" },
        ].map((t, i) => (
          <Link key={t.label} to={t.to} data-testid={t.testId} className="fade-in-up" style={{textDecoration:"none", animationDelay:`${i*80}ms`}}>
            <div className="card-solid" style={{padding:24, position:"relative", overflow:"hidden", height:"100%"}}>
              <div style={{position:"absolute", inset:0, background:t.color, opacity:0.4}}/>
              <div style={{position:"relative"}}>
                <div style={{width:46, height:46, borderRadius:14, background:t.iconBg, color:"#fff", display:"grid", placeItems:"center"}}>{t.icon}</div>
                <div className="font-display" style={{fontWeight:800, fontSize:20, marginTop:18, color:"#0A0A0A", letterSpacing:"-0.02em"}}>{t.label}</div>
                <div style={{color:"#6B7280", fontSize:14, marginTop:6}}>{t.desc}</div>
              </div>
            </div>
          </Link>
        ))}
      </section>

      {/* Recent projects */}
      <section style={{marginTop:48}}>
        <div style={{display:"flex", alignItems:"center", justifyContent:"space-between", marginBottom:18}}>
          <div>
            <div className="kr-label" style={{color:"#FF7A00"}}>Recent</div>
            <h2 className="font-display" style={{fontSize:28, fontWeight:900, letterSpacing:"-0.02em", margin:"2px 0 0"}}>Your projects</h2>
          </div>
          <Link to="/projects" data-testid="see-all-projects" className="btn-ghost">See all <ArrowRight size={14}/></Link>
        </div>

        {loading ? (
          <div style={{display:"grid", gridTemplateColumns:"repeat(auto-fit, minmax(240px, 1fr))", gap:16}}>
            {[1,2,3].map(i => <div key={i} className="card-solid" style={{aspectRatio:"4/3", background:"#f0f0f0"}}/>)}
          </div>
        ) : projects.length === 0 ? (
          <div className="card-solid" style={{padding:48, textAlign:"center"}}>
            <Sparkles size={28} color="#FF7A00" style={{margin:"0 auto"}}/>
            <div className="font-display" style={{fontWeight:800, fontSize:20, marginTop:14}}>No projects yet</div>
            <div style={{color:"#6B7280", marginTop:6, fontSize:14}}>Upload an empty room to create your first design.</div>
            <Link to="/create" className="btn-primary" data-testid="empty-create-btn" style={{marginTop:20, display:"inline-flex"}}><Wand2 size={16}/> Create now</Link>
          </div>
        ) : (
          <div style={{display:"grid", gridTemplateColumns:"repeat(auto-fit, minmax(260px, 1fr))", gap:18}}>
            {projects.slice(0, 6).map((p) => (
              <Link key={p.id} to={`/project/${p.id}`} data-testid={`project-card-${p.id}`} style={{textDecoration:"none"}}>
                <div className="card-solid" style={{overflow:"hidden"}}>
                  <div style={{aspectRatio:"4/3", background:"linear-gradient(135deg,#FFEAD3,#FFA64D)", display:"grid", placeItems:"center", color:"#fff"}}>
                    <div className="font-display" style={{fontWeight:900, fontSize:24}}>{p.room_type}</div>
                  </div>
                  <div style={{padding:18}}>
                    <div style={{display:"flex", alignItems:"center", justifyContent:"space-between"}}>
                      <div className="font-display" style={{fontWeight:800, fontSize:18, color:"#0A0A0A"}}>{p.name}</div>
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
      </section>
    </Shell>
  );
}
