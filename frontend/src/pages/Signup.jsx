import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { toast } from "sonner";
import api from "@/lib/api";
import { useAuth } from "@/contexts/AuthContext";
import { Mail, Lock, User, ArrowRight, Loader2 } from "lucide-react";
import { AuthLayout, Field, Divider, GIcon } from "@/pages/Login";

export default function Signup() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const { loginWithToken } = useAuth();
  const nav = useNavigate();

  const submit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const { data } = await api.post("/auth/signup", { email, password, full_name: name });
      loginWithToken(data.access_token, data.user);
      toast.success("Welcome to KRINTERIOR!");
      nav("/dashboard");
    } catch (err) {
      toast.error(err?.response?.data?.detail || "Signup failed");
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
    <AuthLayout title="Create your account" subtitle="3 free designs to start. No credit card.">
      <button data-testid="google-signup-btn" onClick={googleLogin} className="btn-secondary" style={{width:"100%", justifyContent:"center", padding:"14px"}}>
        <GIcon/> Continue with Google
      </button>

      <Divider/>

      <form onSubmit={submit} style={{display:"grid", gap:14}}>
        <Field icon={<User size={16}/>} placeholder="Full name" value={name} onChange={setName} testId="name-input"/>
        <Field icon={<Mail size={16}/>} placeholder="Email" type="email" value={email} onChange={setEmail} testId="email-input"/>
        <Field icon={<Lock size={16}/>} placeholder="Password (min 6 chars)" type="password" value={password} onChange={setPassword} testId="password-input"/>
        <button type="submit" disabled={loading} data-testid="signup-submit-btn" className="btn-primary" style={{justifyContent:"center", padding:"14px"}}>
          {loading ? <Loader2 size={16} className="spin-slow"/> : <>Create account <ArrowRight size={16}/></>}
        </button>
      </form>

      <div style={{textAlign:"center", marginTop:24, fontSize:14, color:"#6B7280"}}>
        Already have an account? <Link to="/login" data-testid="login-link" style={{color:"#FF7A00", fontWeight:600}}>Sign in</Link>
      </div>
    </AuthLayout>
  );
}
