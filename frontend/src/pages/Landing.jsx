import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "@/contexts/AuthContext";
import { ArrowRight, Sparkles, Wand2, Compass, Wallet, ShieldCheck, PlayCircle } from "lucide-react";
import { useEffect } from "react";

const HERO = "https://static.prod-images.emergentagent.com/jobs/44ee0fce-a68a-45fc-aa10-26ffee77de4f/images/d311bfc1ec2b88f34c9f1a6421bc4c09f61617182b93e09df97acf7cfdcaa3af.png";

export default function Landing() {
  const { user } = useAuth();
  const nav = useNavigate();

  useEffect(() => { if (user) nav("/dashboard"); }, [user, nav]);

  return (
    <div style={{minHeight:"100vh", background:"#F8F8F8"}} className="bg-radial-glow">
      {/* Nav */}
      <header style={{position:"sticky", top:0, zIndex:50, background:"rgba(248,248,248,0.8)", backdropFilter:"blur(16px)"}}>
        <div style={{maxWidth:1280, margin:"0 auto", padding:"18px 24px", display:"flex", alignItems:"center", justifyContent:"space-between"}}>
          <div style={{display:"flex", alignItems:"center", gap:10}}>
            <div style={{width:38, height:38, borderRadius:12, background:"linear-gradient(135deg,#FF7A00,#FFA64D)", display:"grid", placeItems:"center", color:"#fff", fontWeight:900}} className="font-display">K</div>
            <div className="font-display" style={{fontWeight:900, fontSize:20, letterSpacing:"-0.04em"}}>KRINTERIOR<span style={{color:"#FF7A00"}}> AI</span></div>
          </div>
          <nav style={{display:"flex", gap:10}}>
            <Link to="/login" data-testid="nav-login" className="btn-ghost">Sign in</Link>
            <Link to="/signup" data-testid="nav-signup" className="btn-primary" style={{padding:"10px 20px", fontSize:14}}>
              Get started <ArrowRight size={16}/>
            </Link>
          </nav>
        </div>
      </header>

      {/* Hero */}
      <section style={{maxWidth:1280, margin:"0 auto", padding:"40px 24px 80px"}}>
        <div style={{display:"grid", gridTemplateColumns:"1.05fr 1fr", gap:48, alignItems:"center"}} className="hero-grid">
          <div className="fade-in-up">
            <div style={{display:"inline-flex", alignItems:"center", gap:8, padding:"7px 14px", background:"#fff", borderRadius:9999, border:"1px solid #FFE6CC", marginBottom:24}}>
              <Sparkles size={14} color="#FF7A00"/>
              <span style={{fontSize:12, fontWeight:600, letterSpacing:"0.15em", textTransform:"uppercase", color:"#FF7A00"}}>AI Interior Studio</span>
            </div>
            <h1 className="font-display" style={{fontSize:"clamp(40px, 6vw, 76px)", fontWeight:900, lineHeight:1.02, margin:0, letterSpacing:"-0.045em"}}>
              Design your <span className="gradient-text">dream space</span> with AI.
            </h1>
            <p style={{fontSize:18, color:"#4B5563", marginTop:22, maxWidth:520, lineHeight:1.55}}>
              Upload an empty room. Choose your style, budget, and palette. KRINTERIOR AI returns a
              photorealistic Indian-luxury interior, a furniture cost estimate in ₹, and a Vastu report
              — in minutes.
            </p>
            <div style={{display:"flex", gap:12, marginTop:32, flexWrap:"wrap"}}>
              <Link to="/signup" data-testid="hero-create-btn" className="btn-primary">
                <Wand2 size={18}/> Create design — free
              </Link>
              <a href="#features" data-testid="hero-demo-btn" className="btn-secondary">
                <PlayCircle size={18}/> See how it works
              </a>
            </div>
            <div style={{display:"flex", gap:32, marginTop:48, flexWrap:"wrap"}}>
              {[
                ["12,400+", "rooms designed"],
                ["98%", "preserve original room"],
                ["< 60s", "average generation"],
              ].map(([k, v]) => (
                <div key={k}>
                  <div className="font-display" style={{fontSize:28, fontWeight:900, color:"#0A0A0A"}}>{k}</div>
                  <div style={{fontSize:13, color:"#6B7280", letterSpacing:"0.05em"}}>{v}</div>
                </div>
              ))}
            </div>
          </div>

          <div className="fade-in-up delay-200" style={{position:"relative"}}>
            <div style={{position:"absolute", inset:-20, background:"radial-gradient(circle at 60% 30%, rgba(255,122,0,0.18), transparent 60%)", filter:"blur(40px)"}}/>
            <div style={{
              position:"relative",
              borderRadius:32, overflow:"hidden",
              boxShadow:"0 30px 80px rgba(0,0,0,0.18)",
              aspectRatio:"4/5", background:"#000"
            }}>
              <img src={HERO} alt="Luxury Indian interior" style={{width:"100%", height:"100%", objectFit:"cover"}}/>
              <div style={{position:"absolute", left:20, bottom:20, right:20, padding:18, borderRadius:20, background:"rgba(255,255,255,0.88)", backdropFilter:"blur(20px)"}}>
                <div className="kr-label" style={{color:"#FF7A00"}}>Generated · Living Room · ₹2,15,000</div>
                <div className="font-display" style={{fontSize:20, fontWeight:800, marginTop:4, color:"#0A0A0A"}}>Modern Indian Luxury · Warm Beige</div>
              </div>
            </div>
            <div style={{
              position:"absolute", top:-18, right:-18, padding:"14px 18px", borderRadius:18,
              background:"#fff", boxShadow:"0 12px 30px rgba(0,0,0,0.08)", display:"flex", alignItems:"center", gap:12
            }}>
              <div className="score-ring" style={{"--p":92, "--size":"58px", "--thickness":"6px"}}>
                <div style={{fontSize:14, fontWeight:800, color:"#0A0A0A"}}>92</div>
              </div>
              <div>
                <div style={{fontSize:11, color:"#6B7280", letterSpacing:"0.1em", textTransform:"uppercase", fontWeight:700}}>Vastu Score</div>
                <div className="font-display" style={{fontSize:14, fontWeight:800}}>Excellent</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section id="features" style={{maxWidth:1280, margin:"0 auto", padding:"40px 24px 100px"}}>
        <div style={{textAlign:"center", maxWidth:680, margin:"0 auto 56px"}}>
          <div className="kr-label" style={{color:"#FF7A00", marginBottom:12}}>How it works</div>
          <h2 className="font-display" style={{fontSize:"clamp(32px, 4vw, 52px)", fontWeight:900, letterSpacing:"-0.03em", margin:0}}>
            From empty room to fully furnished — in 5 steps.
          </h2>
        </div>
        <div style={{display:"grid", gridTemplateColumns:"repeat(auto-fit, minmax(260px, 1fr))", gap:20}}>
          {[
            { icon: <Wand2/>, title: "Photo-realistic AI", desc: "Gemini Nano Banana preserves walls, windows & perspective while adding luxury Indian furniture." },
            { icon: <Wallet/>, title: "Cost in ₹", desc: "Get a real furniture estimate matched to your budget with Indian-market prices." },
            { icon: <Compass/>, title: "Vastu Shastra", desc: "A 0-100 Vastu score with positive aspects, issues, and concrete recommendations." },
            { icon: <ShieldCheck/>, title: "Save & share", desc: "Save your designs, rename them, and revisit Vastu insights any time." },
          ].map((f, i) => (
            <div key={f.title} className="card-solid fade-in-up" style={{padding:24, animationDelay: `${i*100}ms`}}>
              <div style={{width:46, height:46, borderRadius:14, display:"grid", placeItems:"center", background:"#FFF1E0", color:"#FF7A00"}}>
                {f.icon}
              </div>
              <div className="font-display" style={{fontSize:20, fontWeight:800, marginTop:18, letterSpacing:"-0.02em"}}>{f.title}</div>
              <p style={{color:"#6B7280", fontSize:14.5, marginTop:8, lineHeight:1.6}}>{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section style={{maxWidth:1280, margin:"0 auto 80px", padding:"0 24px"}}>
        <div style={{
          position:"relative", overflow:"hidden",
          borderRadius:32, padding:"64px 40px", textAlign:"center",
          background:"linear-gradient(135deg, #0A0A0A 0%, #2A1505 70%, #FF7A00 130%)",
          color:"#fff"
        }} className="grain">
          <div className="kr-label" style={{color:"#FFA64D", marginBottom:14}}>Ready when you are</div>
          <h3 className="font-display" style={{fontSize:"clamp(28px, 4vw, 48px)", fontWeight:900, letterSpacing:"-0.03em", maxWidth:760, margin:"0 auto"}}>
            Your next room is one upload away.
          </h3>
          <Link to="/signup" data-testid="cta-signup-btn" className="btn-primary" style={{marginTop:28}}>
            Start free <ArrowRight size={18}/>
          </Link>
        </div>
      </section>

      <footer style={{maxWidth:1280, margin:"0 auto", padding:"24px 24px 48px", color:"#6B7280", fontSize:13, display:"flex", justifyContent:"space-between", flexWrap:"wrap", gap:12}}>
        <div>© 2026 KRINTERIOR AI · Mumbai · Bengaluru</div>
        <div>Made with Indian craftsmanship + Gemini AI</div>
      </footer>

      <style>{`
        @media (max-width: 900px) {
          .hero-grid { grid-template-columns: 1fr !important; }
        }
      `}</style>
    </div>
  );
}
