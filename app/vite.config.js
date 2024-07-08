import react from "@vitejs/plugin-react";
import { resolve as rs } from "path";
import AutoImport from "unplugin-auto-import/vite";
import { defineConfig } from "vite";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    AutoImport({
      imports: ["react", "react-router-dom"],
      dts: "./src/auto-imports.d.ts",
      dirs: ["src/components", "src/pages"],
      eslintrc: {
        enabled: true,
      },
    }),
  ],
  resolve: {
    alias: [{ find: "@", replacement: rs(__dirname, "src") }],
  },
  preview: {
    port: 3000,
    strictPort: true,
  },
  server: {
    port: 3000,
    strictPort: true,
    host: true,
    origin: "http://0.0.0.0:3000",
  },
});
