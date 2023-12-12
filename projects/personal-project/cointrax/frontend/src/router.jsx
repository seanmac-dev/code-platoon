import React, { useState } from "react";
import { createBrowserRouter } from "react-router-dom"; 
import App from "./App";
// import UserContext from "./components/UserContext";
import { Crypto } from "./pages/Crypto";
import { Home } from "./pages/Home";
import { Register } from "./pages/RegisterPage";
import { Login } from "./pages/LoginPage";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
            { index: true, element: <Home /> },
            { path: "crypto", element: <Crypto /> },
            { path: "register", element: <Register /> },
            { path: "login", element: <Login /> },
          ],
        },
      ]);
export default router;
