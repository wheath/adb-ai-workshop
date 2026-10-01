# Applied AI for Institutional Capability

Workshop materials, Asian Development Bank, 2 October 2026 (Tim Heath).

This repo holds everything referenced in the slides: the two AI-made concept commercials, the brief and prompts used to build them with GitHub Copilot and Blender MCP, and the scripts for the local voice and music.

> **Concept demo · not an official ADB production.** The commercials use ADB's name in narration only, and contain no ADB logo or branding.

## What's here

| Path | What it is |
|---|---|
| `videos/adb_commercial_claude.mp4` | Commercial built by Claude through Blender MCP (opening video) |
| `videos/adb_commercial_copilot.mp4` | The same brief, built by GitHub Copilot through the same MCP server |
| `copilot_live/AGENTS.md` | The project brief Copilot reads automatically: scene rules, shot list, audio placement |
| `copilot_live/LIVE_PROMPTS.md` | The shot-by-shot prompts, plus correction prompts |
| `blender/` | The two finished Blender files |
| `audio/voice/` | Narration lines (Kokoro, British voice `bm_george`) |
| `audio/music/` | Music bed (Stable Audio 3) |
| `scripts/make_voiceover_kokoro.py` | Generates the narration locally with Kokoro |
| `scripts/music_bed_fallback.py` | A code-generated (non-AI) music bed, as a no-download fallback |
| `docs/setup.md` | Step-by-step setup: Blender MCP, GitHub Copilot, voice, music, recording |
| `docs/lessons.md` | What human review caught, and what it means for using AI at work |
| `docs/mcp-config.example.json` | Example MCP server config for the Copilot CLI |

## The pipeline in one line

You write a plain-English brief → GitHub Copilot (Claude Sonnet) writes Blender Python → the **Blender MCP server** runs it in Blender and sends back results and screenshots → you review and correct → voice (Kokoro) and music (Stable Audio 3) run locally → record with OBS.

Everything ran on a MacBook Air, with no data sent to third-party content services.

Start with [`docs/setup.md`](docs/setup.md).
