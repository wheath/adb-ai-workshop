# British narration for the ADB concept commercial using Kokoro (open-source TTS, British voices).
# Run from the adb_bank folder (after: brew install espeak-ng):
#   uv run --python 3.12 --with kokoro --with soundfile --with pip make_voiceover_kokoro.py
import os, numpy as np, soundfile as sf
from kokoro import KPipeline

VOICES = ["bm_george", "bm_fable", "bf_emma"]   # British male, British male, British female
SPEED = 0.92                                     # slightly slower = calmer narration
LINES = [
    "Across Asia and the Pacific, progress starts with a connection.",
    "A bridge that gets children to school.",
    "Clean power that keeps the lights on.",
    "Projects that link communities to opportunity.",
    "Asian Development Bank.",
    "Building a prosperous, inclusive, resilient Asia and the Pacific.",
]
SR = 24000
pipe = KPipeline(lang_code="b")   # 'b' = British English

for voice in VOICES:
    out = f"audio/kokoro/{voice}"
    os.makedirs(out, exist_ok=True)
    clips = []
    for text in LINES:
        audio = np.concatenate([np.asarray(a, dtype=np.float32) for _, _, a in pipe(text, voice=voice, speed=SPEED)])
        clips.append(audio)
    # lines 5 + 6 become one file with a short pause (title, then tagline)
    pause = np.zeros(int(0.6 * SR), dtype=np.float32)
    lines = clips[:4] + [np.concatenate([clips[4], pause, clips[5]])]
    lead = np.zeros(int(0.2 * SR), dtype=np.float32)
    for i, a in enumerate(lines, 1):
        sf.write(f"{out}/line_{i}.wav", np.concatenate([lead, a, lead]), SR)
    # one preview file per voice, so you can compare quickly
    gap = np.zeros(int(0.5 * SR), dtype=np.float32)
    sf.write(f"audio/kokoro/preview_{voice}.wav", np.concatenate(sum([[a, gap] for a in lines], [])), SR)
    print(f"{voice}: " + ", ".join(f"line_{i} {len(a)/SR:.1f}s" for i, a in enumerate(lines, 1)))
print("Done. Listen to audio/kokoro/preview_*.wav and tell Claude which voice you like.")
