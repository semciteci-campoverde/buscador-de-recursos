import * as esbuild from "esbuild";
import { readFileSync, writeFileSync } from "node:fs";

const result = await esbuild.build({
  entryPoints: ["src/main.tsx"],
  bundle: true,
  outfile: "app.js",
  format: "esm",
  minify: true,
  target: ["es2020"],
  jsx: "automatic",
  sourcemap: false,
  legalComments: "none",
  define: { "process.env.NODE_ENV": '"production"' },
  logLevel: "info",
});

if (result.errors.length) {
  console.error(result.errors);
  process.exit(1);
}

const js = readFileSync("app.js", "utf8");
// GitHub Pages serve estático: o JS já vai pronto, sem build no servidor
writeFileSync("app.js", js);
console.log(`app.js gerado (${(js.length / 1024).toFixed(1)} KB)`);
