import { Link, useNavigate, useLocation } from "react-router-dom";
import { useAuth } from "@/contexts/AuthContext";
import { LogOut, Sparkles, Compass, FolderOpen, Home } from "lucide-react";

export default function Shell({ children }) {
  const { user, logout } = useAuth();
  const nav = useNavigate();
  const loc = useLocation();

  const link = (to, icon, label, testId) => {
    const active = loc.pathname === to || (to !== "/dashboard" && loc.pathname.startsWith(to));
    return (
      <Link
        to={to}
        data-testid={testId}
        style={{
          display:"flex", alignItems:"center", gap:8, padding:"10px 16px",
          borderRadius:9999, fontWeight:500, fontSize:14, textDecoration:"none",
          color: active ? "#fff" : "#4B5563",
          background: active ? "#FF7A00" : "transparent",
          transition:"all .2s ease"
        }}
      >
        {icon} {label}
      </Link>
    );
  };

  return (
    <div style={{minHeight:"100vh", background:"#F8F8F8"}}>
      <header style={{
        position:"sticky", top:0, zIndex:50,
        background:"rgba(248,248,248,0.85)", backdropFilter:"blur(20px)",
        borderBottom:"1px solid #ECECEC"
      }}>
        <div style={{maxWidth:1280, margin:"0 auto", padding:"14px 24px", display:"flex", alignItems:"center", justifyContent:"space-between"}}>
          <Link to="/dashboard" data-testid="logo-link" style={{display:"flex", alignItems:"center", gap:10, textDecoration:"none"}}>
            <div style={{width:36, height:36, borderRadius:12, background:"linear-gradient(135deg,#FF7A00,#FFA64D)", display:"grid", placeItems:"center", color:"#fff", fontWeight:900, fontFamily:"Cabinet Grotesk"}}>K</div>
            <div className="font-display" style={{fontWeight:900, fontSize:18, color:"#0A0A0A", letterSpacing:"-0.04em"}}>
              KRINTERIOR<span style={{color:"#FF7A00"}}> AI</span>
            </div>
          </Link>
          <nav style={{display:"flex", alignItems:"center", gap:4}}>
            {link("/dashboard", <Home size={16}/>, "Home", "nav-home")}
            {link("/projects", <FolderOpen size={16}/>, "Projects", "nav-projects")}
            {link("/vastu", <Compass size={16}/>, "Vastu", "nav-vastu")}
            <Link to="/create" data-testid="nav-create" className="btn-primary" style={{padding:"10px 20px", fontSize:14, marginLeft:8}}>
              <Sparkles size={16}/> Create
            </Link>
            <button
              data-testid="nav-logout"
              onClick={() => { logout(); nav("/"); }}
              className="btn-ghost"
              style={{marginLeft:4}}
              title={user?.email}
            >
              <LogOut size={16}/>
            </button>
          </nav>
        </div>
      </header>
      <main style={{maxWidth:1280, margin:"0 auto", padding:"32px 24px"}}>
        {children}
      </main>
    </div>
  );
}
