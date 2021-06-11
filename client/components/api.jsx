import Axios from "axios";

let urls = {
  development: "http://localhost:8000/api",
  production: "",
};
const api = Axios.create({
  baseURL: urls["development"],
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

export default api;