import { BrowserRouter, Routes, Route, Navigate, useLocation } from "react-router-dom";
import { AuthProvider, useAuth } from "@/contexts/AuthContext";
import Landing from "@/pages/Landing";
import Login from "@/pages/Login";
import Signup from "@/pages/Signup";
import AuthCallback from "@/pages/AuthCallback";
import Dashboard from "@/pages/Dashboard";
import CreateWizard from "@/pages/CreateWizard";
import Result from "@/pages/Result";
import Projects from "@/pages/Projects";
import ProjectDetail from "@/pages/ProjectDetail";
import Vastu from "@/pages/Vastu";
import { Toaster } from "sonner";
import "@/App.css";

function ProtectedRoute({ children }) {
  const { user, loading } = useAuth();
  if (loading) {
    return (
      <div style={{display:"grid", placeItems:"center", height:"100vh"}}>
        <div className="spin-slow" style={{width:48, height:48, borderRadius:"50%", border:"4px solid #FFE6CC", borderTopColor:"#FF7A00"}} />
      </div>
    );
  }
  if (!user) return <Navigate to="/login" replace />;
  return children;
}

function AppRouter() {
  const location = useLocation();
  // Synchronous check during render – handles Emergent Google Auth return
  if (location.hash?.includes("session_id=")) {
    return <AuthCallback />;
  }
  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Signup />} />
      <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
      <Route path="/create" element={<ProtectedRoute><CreateWizard /></ProtectedRoute>} />
      <Route path="/result" element={<ProtectedRoute><Result /></ProtectedRoute>} />
      <Route path="/projects" element={<ProtectedRoute><Projects /></ProtectedRoute>} />
      <Route path="/project/:id" element={<ProtectedRoute><ProjectDetail /></ProtectedRoute>} />
      <Route path="/vastu" element={<ProtectedRoute><Vastu /></ProtectedRoute>} />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <AppRouter />
        <Toaster position="top-center" richColors />
      </BrowserRouter>
    </AuthProvider>
  );
}
