import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { toast } from "sonner";
import api from "@/lib/api";
import { useAuth } from "@/contexts/AuthContext";
import { Mail, Lock, ArrowRight, Loader2 } from "lucide-react";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const { loginWithToken } = useAuth();
  const nav = useNavigate();

  const submit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const { data } = await api.post("/auth/login", { email, password });
      loginWithToken(data.access_token, data.user);
      toast.success("Welcome back!");
      nav("/dashboard");
    } catch (err) {
      toast.error(err?.response?.data?.detail || "Login failed");
    } finally {
      setLoading(false);
    }
  };

  const googleLogin = () => {
    // REMINDER: DO NOT HARDCODE THE URL, OR ADD ANY FALLBACKS OR REDIRECT URLS, THIS BREAKS THE AUTH
    const redirectUrl = window.location.origin + "/dashboard";
    window.location.href = `https://auth.emergentagent.com/?redirect=${encodeURIComponent(redirectUrl)}`;
  };

  return (
    <AuthLayout title="Welcome back" subtitle="Sign in to design your next room.">
      <button data-testid="google-login-btn" onClick={googleLogin} className="btn-secondary" style={{width:"100%", justifyContent:"center", padding:"14px"}}>
        <GIcon/> Continue with Google
      </button>

      <Divider/>

      <form onSubmit={submit} style={{display:"grid", gap:14}}>
        <Field icon={<Mail size={16}/>} placeholder="Email" type="email" value={email} onChange={setEmail} testId="email-input"/>
        <Field icon={<Lock size={16}/>} placeholder="Password" type="password" value={password} onChange={setPassword} testId="password-input"/>
        <button type="submit" disabled={loading} data-testid="login-submit-btn" className="btn-primary" style={{justifyContent:"center", padding:"14px"}}>
          {loading ? <Loader2 size={16} className="spin-slow"/> : <>Sign in <ArrowRight size={16}/></>}
        </button>
      </form>

      <div style={{textAlign:"center", marginTop:24, fontSize:14, color:"#6B7280"}}>
        New here? <Link to="/signup" data-testid="signup-link" style={{color:"#FF7A00", fontWeight:600}}>Create an account</Link>
      </div>
    </AuthLayout>
  );
}

export function AuthLayout({ title, subtitle, children }) {
  return (
    <div style={{minHeight:"100vh", display:"grid", gridTemplateColumns:"1fr 1fr"}} className="auth-layout">
      <div style={{position:"relative", background:"linear-gradient(155deg, #0A0A0A, #2A1505)", overflow:"hidden"}} className="auth-hero">
        <div style={{position:"absolute", inset:0, background:"radial-gradient(circle at 70% 20%, rgba(255,166,77,0.25), transparent 50%)"}}/>
        <img src="https://static.prod-images.emergentagent.com/jobs/44ee0fce-a68a-45fc-aa10-26ffee77de4f/images/d311bfc1ec2b88f34c9f1a6421bc4c09f61617182b93e09df97acf7cfdcaa3af.png"
             alt="" style={{position:"absolute", inset:0, width:"100%", height:"100%", objectFit:"cover", opacity:0.55, mixBlendMode:"luminosity"}}/>
        <div style={{position:"relative", padding:48, color:"#fff", height:"100%", display:"flex", flexDirection:"column", justifyContent:"space-between"}}>
          <Link to="/" data-testid="auth-logo" style={{display:"flex", alignItems:"center", gap:10, color:"#fff", textDecoration:"none"}}>
            <div style={{width:38, height:38, borderRadius:12, background:"linear-gradient(135deg,#FF7A00,#FFA64D)", display:"grid", placeItems:"center", color:"#fff", fontWeight:900}} className="font-display">K</div>
            <div className="font-display" style={{fontWeight:900, fontSize:20, letterSpacing:"-0.04em"}}>KRINTERIOR AI</div>
          </Link>
          <div>
            <div className="kr-label" style={{color:"#FFA64D"}}>Indian Luxury Interiors · AI</div>
            <div className="font-display" style={{fontSize:42, fontWeight:900, letterSpacing:"-0.03em", lineHeight:1.05, marginTop:12, maxWidth:480}}>
              Empty rooms in. Magazine-grade interiors out.
            </div>
          </div>
        </div>
      </div>
      <div style={{display:"grid", placeItems:"center", padding:24, background:"#F8F8F8"}}>
        <div style={{width:"100%", maxWidth:420}}>
          <h1 className="font-display" style={{fontSize:38, fontWeight:900, letterSpacing:"-0.03em", margin:0}}>{title}</h1>
          <p style={{color:"#6B7280", marginTop:8, marginBottom:28}}>{subtitle}</p>
          {children}
        </div>
      </div>
      <style>{`
        @media (max-width: 900px) {
          .auth-layout { grid-template-columns: 1fr !important; }
          .auth-hero { display: none; }
        }
      `}</style>
    </div>
  );
}

export function Field({ icon, placeholder, type="text", value, onChange, testId }) {
  return (
    <div style={{position:"relative"}}>
      <div style={{position:"absolute", left:14, top:"50%", transform:"translateY(-50%)", color:"#9CA3AF"}}>{icon}</div>
      <input
        type={type}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={placeholder}
        required
        data-testid={testId}
        className="input-kr"
        style={{paddingLeft:42}}
      />
    </div>
  );
}

export function Divider() {
  return (
    <div style={{display:"flex", alignItems:"center", gap:12, margin:"24px 0", color:"#9CA3AF"}}>
      <div style={{flex:1, height:1, background:"#E5E7EB"}}/>
      <div style={{fontSize:11, letterSpacing:"0.2em", textTransform:"uppercase", fontWeight:700}}>or</div>
      <div style={{flex:1, height:1, background:"#E5E7EB"}}/>
    </div>
  );
}

export function GIcon() {
  return (
    <svg width="18" height="18" viewBox="0 0 24 24"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.99.66-2.25 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.1c-.22-.66-.35-1.36-.35-2.1s.13-1.44.35-2.1V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.83z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.83C6.71 7.31 9.14 5.38 12 5.38z"/></svg>
  );
}
