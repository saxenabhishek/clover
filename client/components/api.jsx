import Axios from "axios";

let urls = {
  dev: "http://localhost:3000/api",
  pro: "https://frappe.abhisheksaxenna.xyz/api",
};
const api = Axios.create({
  baseURL: urls[process.env.NEXT_PUBLIC_host],
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

export default api;
