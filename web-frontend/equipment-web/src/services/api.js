import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
});

api.interceptors.request.use((config) => {
  const username = "jaysh";
  const password = "Jassu2309!";
  const token = btoa(`${username}:${password}`);
  config.headers.Authorization = `Basic ${token}`;
  return config;
});

export default api;
