# Beat tracking example
import librosa
import matplotlib.pyplot as plt
import numpy as np

# 1. Get the file path to an included audio example
y, sr = librosa.load("assignments\\assign01\\example.wav")

rms = librosa.feature.rms(y=y)

fig, ax = plt.subplots(nrows=2, sharex=True)
times = librosa.times_like(rms)
ax[0].set_title("RMS (Loudness)")
ax[0].semilogy(times, rms[0], label="RMS Energy")
ax[0].set(xticks=[])
ax[0].legend()
ax[0].label_outer()

ax[1].set_title("Fundamental Frequency - F0 (Pitch)")
f0, voicing, voicing_p = librosa.pyin(y=y, sr=sr, fmin=200, fmax=11000)
S = np.abs(librosa.stft(y))

librosa.display.specshow(
    librosa.amplitude_to_db(S, ref=np.max), x_axis="time", y_axis="log", ax=ax[1]
)
freqs = librosa.fft_frequencies(sr=sr)
harmonics = np.arange(1,13)
f0_harm = librosa.f0_harmonics(S, freqs=freqs, f0=f0, harmonics=harmonics)

times = librosa.times_like(f0)
for h in harmonics:
    ax[1].plot(times, h * f0, label=f"{h}*f0")

ax[1].legend(ncols=4, loc='lower right')

plt.savefig("feqandintens.jpg")
