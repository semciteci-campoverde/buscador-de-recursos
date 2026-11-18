#!/usr/bin/env python3
"""Copia o source do canvas e troca só o que o kit grok/canvas não tem fora do host."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

OLD_IMPORT = '''import { Image, Page, useGrokTheme, useState } from "grok/canvas";
import type { ReactNode, CSSProperties } from "grok/canvas";'''

NEW_IMPORT = '''import { useState, type ReactNode, type CSSProperties } from "react";
import { Image, Page, useGrokTheme } from "./theme";'''

OLD_URL = 'https://cursor.com/canvas/store-320ae79f-e448-4286-945e-0be9da8cb636/c95e6322-6f0e-432a-b162-08bfe0b0e9ed'
DEFAULT_URL = "https://semciteci-campoverde.github.io/buscador-de-recursos/"

# Grade em tela cheia: 1 coluna no celular, até 5 no computador
OLD_GRID = 'gridTemplateColumns: "repeat(auto-fill, minmax(min(100%, 280px), 1fr))"'
NEW_GRID = 'gridTemplateColumns: "repeat(auto-fill, minmax(min(100%, max(260px, calc((100% - 56px) / 5))), 1fr))"'
OLD_MUN = 'gridTemplateColumns: "repeat(auto-fill, minmax(min(100%, 240px), 1fr))"'
NEW_MUN = 'gridTemplateColumns: "repeat(auto-fill, minmax(min(100%, max(240px, calc((100% - 56px) / 5))), 1fr))"'
OLD_TL = 'gridTemplateColumns: "repeat(auto-fill, minmax(min(100%, 230px), 1fr))"'
NEW_TL = 'gridTemplateColumns: "repeat(auto-fill, minmax(min(100%, max(220px, calc((100% - 56px) / 5))), 1fr))"'


def port(src: Path, dest: Path, app_url: str) -> None:
    text = src.read_text(encoding="utf-8")
    if OLD_IMPORT not in text:
        raise SystemExit(f"Imports inesperados em {src}. Abortei para não corromper o arquivo.")
    text = text.replace(OLD_IMPORT, NEW_IMPORT)
    text = text.replace(OLD_URL, app_url.rstrip("/") + "/")
    text = text.replace(OLD_GRID, NEW_GRID)
    text = text.replace(OLD_MUN, NEW_MUN)
    text = text.replace(OLD_TL, NEW_TL)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    print(f"Portado: {src} -> {dest}")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    p = argparse.ArgumentParser()
    p.add_argument("--src", default="/tmp/source.canvas.tsx")
    p.add_argument("--dest", default=str(root / "src" / "App.tsx"))
    p.add_argument("--url", default=DEFAULT_URL)
    args = p.parse_args()
    src = Path(args.src)
    # Prefer the live canvas if it is present on this machine
    live = Path("/cursor/stores/user/canvases/c95e6322-6f0e-432a-b162-08bfe0b0e9ed/source.canvas.tsx")
    if live.exists():
        src = live
        print(f"Usando canvas ao vivo: {live}")
    elif not src.exists():
        # already-ported App.tsx is the fallback
        if Path(args.dest).exists():
            print("Canvas não encontrado; mantendo src/App.tsx atual.")
            return
        raise SystemExit(f"Fonte do canvas não encontrada: {src}")
    port(src, Path(args.dest), args.url)


if __name__ == "__main__":
    main()
