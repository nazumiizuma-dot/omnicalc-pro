import axios from "axios";
const API_BASE = (import.meta.env.VITE_API_BASE || "http://localhost:8000/api/v1");

export async function listModules() {
  const r = await axios.get(`${API_BASE}/calculator/modules`);
  return r.data;
}

export async function execModule(module: string, inputs: any) {
  const r = await axios.post(`${API_BASE}/calculator/${module}/exec`, { inputs });
  return r.data;
}
