import sounddevice as sd
import soundfile as sf

sample_rate = 44100
duration = 5

print("Recording...")
audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    device=1
)

sd.wait()

sf.write("mic_test.wav", audio, sample_rate)

print("Done! Saved as mic_test.wav")