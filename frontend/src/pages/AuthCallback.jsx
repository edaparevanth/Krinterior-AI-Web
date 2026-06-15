import { useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";
import api from "@/lib/api";
import { useAuth } from "@/contexts/AuthContext";
import { toast } from "sonner";

export default function AuthCallback() {
  const nav = useNavigate();
  const { loginWithToken } = useAuth();
  const processed = useRef(false);

  useEffect(() => {
    if (processed.current) return;
    processed.current = true;
    (async () => {
      try {
        const hash = window.location.hash || "";
        const params = new URLSearchParams(hash.replace(/^#/, ""));
        const sessionId = params.get("session_id");
        if (!sessionId) {
          nav("/login", { replace: true });
          return;
        }
        const { data } = await api.post("/auth/google/session", { session_id: sessionId });
        loginWithToken(data.access_token, data.user);
        // Clean hash & route to dashboard
        window.history.replaceState({}, "", "/dashboard");
        nav("/dashboard", { replace: true });
        toast.success(`Welcome ${data.user?.name || data.user?.email || ""}!`);
      } catch (e) {
        toast.error("Google sign-in failed");
        nav("/login", { replace: true });
      }
    })();
  }, [nav, loginWithToken]);

  return (
    <div style={{display:"grid", placeItems:"center", height:"100vh", background:"#F8F8F8"}}>
      <div style={{textAlign:"center"}}>
        <div className="spin-slow" style={{width:48, height:48, borderRadius:"50%", border:"4px solid #FFE6CC", borderTopColor:"#FF7A00", margin:"0 auto"}}/>
        <div className="font-display" style={{marginTop:18, fontWeight:800, fontSize:18}}>Signing you in…</div>
      </div>
    </div>
  );
}
