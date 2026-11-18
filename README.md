# Buscador de Recursos – Vereadores de Campo Verde

Site para os 13 vereadores de Campo Verde-MT encontrarem fontes de recurso (emendas federais e estaduais, Pix, saúde fundo a fundo e programas), a partir das pautas de cada um na Câmara.

**Endereço:** https://semciteci-campoverde.github.io/buscador-de-recursos/

Desenvolvido por Rigoberto Ximenes Lopes.

## O que o site faz

- Abre em tela cheia, no computador e no celular.
- Cada vereador tem um card com foto oficial, partido e o tema em que mais atua.
- Ao abrir o card: 3 prioridades, mapa do poder, temas, oportunidades, pautas da Câmara (10 mais recentes; toque no tema para ver todas), checklist, ofício pronto (copiar / baixar .doc ou .txt), WhatsApp e impressão.
- Abas: Municipal, Estadual, Federal, Instituições, Glossário, Fontes e auditoria.
- Emendas impositivas dos vereadores **não** entram neste site.

Dados conferidos em 18/11/2026 (SAPL da Câmara, TSE, Câmara dos Deputados, Senado, ALMT, CMO e Transferegov).

## Como atualizar (rotina diária)

Na máquina em que o projeto foi gerado (`/workspace/buscador-de-recursos`):

```bash
./publicar.sh
```

O script:

1. Reimporta o canvas, se ele estiver neste computador.
2. Recopia as fotos de `/workspace/pente_fino_discricionarias_2026/dados_app/fotos`, se a pasta existir.
3. Gera de novo o `app.js`.
4. Envia para o GitHub (`main`) e o GitHub Pages atualiza o site.

Se você só mudou um texto ou um dado em `src/App.tsx`, o mesmo comando vale.

Para só gerar o site, sem enviar:

```bash
npm install
npm run build
```

Depois abra o `index.html` com um servidor local (não abra o arquivo direto no navegador, por causa dos módulos):

```bash
python3 -m http.server 8080
```

## Fonte do app

O conteúdo veio da página “Buscador de Recursos – Vereadores de Campo Verde” e foi adaptado para um site estático (React + esbuild), porque o kit `grok/canvas` só roda no ambiente original. O comportamento e os dados foram mantidos.
