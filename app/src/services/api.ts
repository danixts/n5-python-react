import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_APP_URL,
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

api.interceptors.request.use(
  (config) => {
    const auth = localStorage.getItem("auth");
    const token = JSON.parse(auth as string).state.token;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export default api;
