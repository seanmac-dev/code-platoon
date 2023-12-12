// HTTP utilities and such
import axios from "axios";

// Creating a little http client for ourselves
export const api = axios.create({
    baseURL: "http://127.0.0.1:8000/api/",
}); 