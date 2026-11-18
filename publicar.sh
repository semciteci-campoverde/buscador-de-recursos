#!/usr/bin/env bash
# Reconstrói o site a partir dos dados/canvas e envia para o GitHub Pages.
set -euo pipefail
cd "$(dirname "$0")"

APP_URL="${APP_URL:-https://semciteci-campoverde.github.io/buscador-de-recursos/}"
REPO="${REPO:-semciteci-campoverde/buscador-de-recursos}"
BRANCH="${BRANCH:-main}"

echo "==> Portando o canvas (se estiver disponível)"
python3 scripts/portar.py --url "$APP_URL"

FOTOS_ORIG="/workspace/pente_fino_discricionarias_2026/dados_app/fotos"
if [[ -d "$FOTOS_ORIG" ]]; then
  echo "==> Atualizando fotos"
  mkdir -p fotos
  cp -a "$FOTOS_ORIG"/*.jpg fotos/
fi

if [[ ! -d node_modules/esbuild || ! -d node_modules/react ]]; then
  echo "==> Instalando dependências de build"
  npm install --no-fund --no-audit
fi

echo "==> Gerando app.js"
node build.mjs

echo "==> Conferindo o JavaScript"
node --check app.js

if [[ ! -d .git ]]; then
  echo "Este diretório ainda não é um repositório git. Inicialize e configure o remote antes de publicar."
  exit 1
fi

git add -A
if git diff --cached --quiet; then
  echo "Nada novo para enviar."
else
  git commit -m "Atualiza Buscador de Recursos ($(date +%Y-%m-%d))"
  git push origin "$BRANCH"
  echo "Enviado para https://github.com/${REPO}"
fi

if ! gh api "repos/${REPO}/pages" >/dev/null 2>&1; then
  echo "==> Ativando GitHub Pages"
  gh api -X POST "repos/${REPO}/pages" -f "source[branch]=${BRANCH}" -f "source[path]=/" || true
fi

echo "Site: $APP_URL"
