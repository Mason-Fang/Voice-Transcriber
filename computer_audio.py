import pyaudiowpatch as pyaudio
import wave

p = pyaudio.PyAudio()

device_index = 13
device = p.get_device_info_by_index(device_index)

sample_rate = int(device["defaultSampleRate"])
channels = device["maxInputChannels"]

print("Recording computer audio...")

stream = p.open(
    format=pyaudio.paInt16,
    channels=channels,
    rate=sample_rate,
    input=True,
    input_device_index=device_index,
    frames_per_buffer=1024
)

frames = []

for i in range(int(sample_rate / 1024 * 5)):
    data = stream.read(1024)
    frames.append(data)

print("Done recording.")

stream.stop_stream()
stream.close()

p.terminate()

with wave.open("system_audio.wav", "wb") as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(sample_rate)
    wf.writeframes(b"".join(frames))

print("Saved as system_audio.wav")