import { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import App from "./App";

/** Atualiza a contagem dos prazos a cada 30s (o canvas só recalculava ao interagir). */
function Root() {
  const [, setTick] = useState(0);
  useEffect(() => {
    const id = window.setInterval(() => setTick((n) => n + 1), 30_000);
    return () => window.clearInterval(id);
  }, []);
  return <App />;
}

const el = document.getElementById("root");
if (!el) throw new Error("Elemento #root não encontrado");
createRoot(el).render(<Root />);
