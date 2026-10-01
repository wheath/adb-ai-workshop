# Fallback music bed generated with plain code (no AI model): chords, piano, bass, reverb.
# Run from the repo root: python3 scripts/music_bed_fallback.py  (needs numpy, scipy)
import os; os.makedirs("audio", exist_ok=True)
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 44100
DUR = 35.5
N = int(SR * DUR)
t = np.arange(N) / SR
rng = np.random.default_rng(3)

def midi(n): return 440.0 * 2 ** ((n - 69) / 12)

# Progression (C major, hopeful): C  G  Am  F | C  G  F  C(final, held)
chords = [
    [48, 55, 60, 64, 67],  # C
    [43, 55, 59, 62, 67],  # G
    [45, 52, 57, 60, 64],  # Am
    [41, 53, 57, 60, 65],  # F
    [48, 55, 60, 64, 67],  # C
    [43, 55, 59, 62, 67],  # G
    [41, 53, 57, 60, 65],  # F
    [48, 55, 60, 64, 72],  # C (title)
]
starts = [0, 3.4, 6.8, 10.2, 13.6, 17.0, 20.4, 24.6]  # last chord lands as the sunset/title begins

def env_ad(length, a, r):
    n = int(length * SR); e = np.ones(n)
    na = int(a * SR); nr = int(r * SR)
    e[:na] = np.linspace(0, 1, na)
    if nr: e[-nr:] *= np.linspace(1, 0, nr)
    return e

pad = np.zeros((N, 2))
for i, (ch, s) in enumerate(zip(chords, starts)):
    end = starts[i + 1] + 0.8 if i + 1 < len(starts) else DUR
    L = end - s; n0 = int(s * SR); n = min(int(L * SR), N - n0)
    tt = np.arange(n) / SR
    e = env_ad(L, 1.2, 1.0)[:n]
    for note in ch:
        f = midi(note)
        for det, pan in ((-0.12, 0.3), (0.12, 0.7)):  # detuned pair, panned
            ff = f * 2 ** (det / 12 / 4)
            w = (np.sin(2*np.pi*ff*tt) + 0.35*np.sin(2*np.pi*2*ff*tt) + 0.12*np.sin(2*np.pi*3*ff*tt))
            w *= (1 + 0.15*np.sin(2*np.pi*0.25*tt + note))  # slow shimmer
            pad[n0:n0+n, 0] += w * e * (1 - pan) * 0.05
            pad[n0:n0+n, 1] += w * e * pan * 0.05

# Soft piano-like arpeggio (decaying partials), 8th notes at ~84 bpm
piano = np.zeros((N, 2))
step = 60 / 84 / 2
def pluck(f, n):
    tt = np.arange(n) / SR
    e = np.exp(-tt * 3.2) * np.minimum(1, tt / 0.005)
    return e * (np.sin(2*np.pi*f*tt) + 0.5*np.sin(2*np.pi*2*f*tt)*np.exp(-tt*2) + 0.2*np.sin(2*np.pi*3*f*tt)*np.exp(-tt*4))
for i, (ch, s) in enumerate(zip(chords, starts)):
    end = starts[i + 1] if i + 1 < len(starts) else 31.5
    pattern = [ch[2], ch[3], ch[4], ch[3] + 12 if i in (3, 6) else ch[4] + 5 - 5, ch[2] + 12, ch[4], ch[3], ch[4]]
    k = 0; tm = s
    # piano enters after the opening line (sparser at the start)
    while tm < end - 0.05:
        if tm > 2.0 or k % 2 == 0:
            f = midi(pattern[k % len(pattern)] + 12)
            n0 = int(tm * SR); n = min(int(2.5 * SR), N - n0)
            p = pluck(f, n) * 0.06
            pan = 0.35 + 0.3 * ((k % 4) / 3)
            piano[n0:n0+n, 0] += p * (1 - pan); piano[n0:n0+n, 1] += p * pan
        tm += step; k += 1

# Bass (root, long notes)
bass = np.zeros(N)
for i, (ch, s) in enumerate(zip(chords, starts)):
    end = starts[i + 1] if i + 1 < len(starts) else DUR
    n0 = int(s * SR); n = min(int((end - s + 0.3) * SR), N - n0)
    tt = np.arange(n) / SR; f = midi(ch[0] - 12)
    bass[n0:n0+n] += np.sin(2*np.pi*f*tt) * env_ad(n / SR, 0.3, 0.6)[:n] * 0.09

# Gentle rising swell into the title (from ~22s), plus soft cymbal-like shimmer at 24s
swell = np.zeros(N)
ns = int(22.1 * SR); ne = int(24.6 * SR)
noise = rng.standard_normal(ne - ns)
sos = butter(2, [3000, 9000], btype='band', fs=SR, output='sos')
noise = sosfilt(sos, noise) * np.linspace(0, 1, ne - ns) ** 2 * 0.05
swell[ns:ne] = noise
n0 = int(24.6 * SR); n = N - n0
shim = sosfilt(sos, rng.standard_normal(n)) * np.exp(-np.arange(n) / SR * 1.2) * 0.04

mix = pad + piano
mix[:, 0] += bass + swell; mix[:, 1] += bass + swell
mix[n0:, 0] += shim; mix[n0:, 1] += shim

# Simple stereo reverb: a few feedback delays
def reverb(x):
    out = x.copy()
    for d, g in ((0.031, 0.35), (0.047, 0.3), (0.071, 0.25), (0.113, 0.2), (0.173, 0.15)):
        k = int(d * SR)
        y = np.zeros_like(x); y[k:] = x[:-k] * g
        out += y
    return out
mix[:, 0] = reverb(mix[:, 0]); mix[:, 1] = reverb(mix[:, 1])

# Master: fade in/out, normalise to -3 dBFS
fade = np.ones(N)
fi = int(1.0 * SR); fo = int(3.5 * SR)
fade[:fi] = np.linspace(0, 1, fi); fade[-fo:] = np.linspace(1, 0, fo)
mix *= fade[:, None]
rms=np.sqrt(np.mean(mix**2)); mix *= 0.12/rms; mix = np.tanh(mix*1.2)/1.2
wavfile.write("audio/adb_music_bed.wav", SR, (mix * 32767).astype(np.int16))
print("written", mix.shape[0] / SR, "s")
