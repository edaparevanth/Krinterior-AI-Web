import axios from "axios";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
export const API = `${BACKEND_URL}/api`;
const E2E_MOCKS = process.env.REACT_APP_E2E_MOCKS === "true";
const TINY_PNG_B64 =
  "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=";

const mockUser = {
  id: "selenium-user",
  email: "rev@example.com",
  full_name: "Selenium Test",
  name: "Selenium Test",
};

const mockDesign = {
  furniture_estimate: [
    { name: "Walnut sofa", category: "seating", price_inr: 72000 },
    { name: "Coffee table", category: "table", price_inr: 18000 },
    { name: "Floor lamp", category: "lighting", price_inr: 12000 },
  ],
  total_cost: 102000,
  space_analysis: {
    estimated_size_sqft: 180,
    available_zones: ["Seating", "Storage", "Accent corner"],
    design_opportunities: ["Layered lighting", "Warm textiles"],
    optimization_suggestions: ["Use a large rug", "Keep walkways open"],
  },
  vastu_report: {
    score: 84,
    summary: "Balanced layout with warm, grounding finishes.",
    recommendations: ["Add greenery in the east", "Use warm lighting"],
  },
  vastu_score: 84,
};

function mockResponse(config, data, status = 200) {
  return Promise.resolve({
    data,
    status,
    statusText: status === 200 ? "OK" : "Error",
    headers: {},
    config,
  });
}

const api = axios.create({
  baseURL: API,
  withCredentials: true,
});

if (E2E_MOCKS) {
  api.defaults.adapter = async (config) => {
    const rawUrl = config.url || "";
    const url = rawUrl.replace(/^https?:\/\/[^/]+\/api/, "");
    const method = (config.method || "get").toLowerCase();
    const token = localStorage.getItem("kr_token");

    if (method === "post" && url === "/auth/login") {
      return mockResponse(config, {
        access_token: "selenium-token",
        token_type: "bearer",
        user: mockUser,
      });
    }
    if (method === "post" && url === "/auth/signup") {
      return mockResponse(config, {
        access_token: "selenium-token",
        token_type: "bearer",
        user: { ...mockUser, email: "signup.selenium@example.com" },
      });
    }
    if (method === "post" && url === "/auth/logout") {
      return mockResponse(config, { ok: true });
    }
    if (method === "get" && url === "/auth/me") {
      return token
        ? mockResponse(config, mockUser)
        : Promise.reject({ response: { status: 401, data: { detail: "Not authenticated" } } });
    }
    if (method === "get" && url === "/projects") {
      return mockResponse(config, []);
    }
    if (method === "post" && url === "/design/generate") {
      return mockResponse(config, { job_id: "selenium-job", status: "pending" });
    }
    if (method === "get" && url === "/design/status/selenium-job") {
      return mockResponse(config, { status: "done", generated_image: TINY_PNG_B64 });
    }
    if (method === "post" && url === "/design/analyze") {
      return mockResponse(config, mockDesign);
    }
    if (method === "post" && url === "/projects") {
      return mockResponse(config, { id: "selenium-project", ...mockDesign });
    }
    return mockResponse(config, {});
  };
}

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("kr_token");
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default api;
