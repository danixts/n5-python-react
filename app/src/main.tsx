import React from "react";
import ReactDOM from "react-dom/client";
import "./App.css";
import App from "./App";
import { AuthProvider } from "@/context/AuthProvider";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    {/* <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme"> */}
      <AuthProvider>
        <App />
      </AuthProvider>
    {/* </ThemeProvider> */}
  </React.StrictMode>
);
