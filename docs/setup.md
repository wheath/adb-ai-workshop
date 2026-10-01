# Setup: build the commercial with GitHub Copilot + Blender MCP

Tested on a MacBook Air (Apple Silicon), macOS, Blender 5.2, October 2026.

## 1. Blender MCP

```bash
brew install uv
uvx mcp-for-blender install-addon
```

1. Install Blender from blender.org.
2. In Blender: **Edit → Preferences → Add-ons**, enable **"MCP for Blender"**.
3. In the 3D view press **N** → **MCP for Blender** tab → **Start MCP Server**.
4. When the add-on asks to collect session data, choose **Decline**.

Project: <https://github.com/ahujasid/mcp-for-blender>

## 2. Connect GitHub Copilot

Any Copilot plan works. We used Copilot Pro+.

**GitHub Copilot app** (desktop): **Customize → MCP → Add server**

| Field | Value |
|---|---|
| Name | `blender` |
| Type | Local |
| Command | `/opt/homebrew/bin/uvx` (use the full path; find it with `which uvx`) |
| Arguments | `mcp-for-blender` |

Wait for the green **Connected** tick. Using plain `uvx` fails with "No such file or directory", because apps opened from the Dock don't see Homebrew's path.

**Copilot CLI** (terminal): `/mcp add` with the same values, or see [`mcp-config.example.json`](mcp-config.example.json).

Only one AI should drive Blender at a time. Quit other agents while Copilot is working.

## 3. Brief and prompts

1. Open `copilot_live/` as the project in the Copilot app. Copilot reads `AGENTS.md` automatically.
2. Start a new chat (model: Claude Sonnet) and check the connection:
   > What MCP tools do you have available? List the Blender ones.
3. Paste the prompts from `LIVE_PROMPTS.md`, one shot at a time.
4. Ask for evidence every time: screenshots at named frames, and framing checks with `world_to_camera_view`.
5. When Copilot reports "Compacted conversation", start a new chat. `AGENTS.md` carries the brief across.

## 4. Voice (Kokoro, local)

```bash
brew install espeak-ng
uv run --python 3.12 --with "kokoro>=0.9.4" --with "transformers>=4.44" \
  --with "tokenizers>=0.19" --with soundfile --with pip scripts/make_voiceover_kokoro.py
```

Downloads about 330 MB on first run. Writes previews for three British voices to `audio/kokoro/`. We used `bm_george`.

Pinning `transformers` and `tokenizers` avoids an old build that needs a Rust compiler.

## 5. Music (Stable Audio 3, local, Apple Silicon)

```bash
curl -LsSf https://raw.githubusercontent.com/Stability-AI/stable-audio-3/main/optimized/mlx/bootstrap.sh | bash
cd ~/stable-audio-3/optimized/mlx
./sa3 --prompt "cinematic orchestral score: soft solo piano opening, warm strings gradually join and build, full hopeful orchestral swell with timpani in the final third, peaceful ending, documentary film music, 80 BPM, instrumental" \
      --dit medium --seconds 36 --out music.wav
```

About 10–15 seconds per 36-second track on an M-series MacBook Air. Web UI: `./sa3-gradio --no-share`.

No AI model available? `python3 scripts/music_bed_fallback.py` makes a simple code-generated bed.

### Licences (check before commercial use)

| Tool | Licence |
|---|---|
| Kokoro | Apache 2.0 |
| ACE-Step 1.5 (alternative music model) | MIT |
| Stable Audio 3 | Stability AI Community License: free under US$1M annual revenue, enterprise licence above that |

This is not legal advice. Have your legal team review before using any output commercially.

## 6. Record and share (no long render needed)

1. Blender: camera view, Rendered shading, **Ctrl+Space** to fill the window, **Shift+←** to go to frame 1.
2. **OBS Studio**: Sources **+** → macOS Screen Capture → Window Capture → Blender. Window audio is captured automatically. Mute Mic/Aux.
3. Start Recording, press **Space** in Blender, stop at the end.
4. Crop to the camera frame and compress (about 32 MB down to 3 MB):

```bash
ffmpeg -i recording.mov -vf "crop=W:H:X:Y,scale=1280:720" \
  -c:v libx264 -crf 23 -preset slow -pix_fmt yuv420p \
  -c:a aac -b:a 128k -movflags +faststart commercial.mp4
```

Replace `W:H:X:Y` with the size and position of the camera frame in your recording.
