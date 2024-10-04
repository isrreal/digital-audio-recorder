import pyaudio
import wave

CHUNK = 1024  # Size of the audio chunk, used as an update rate in each iteration to record the digitalized audio.
QUANT = pyaudio.paInt16  # Audio quantization format (16 bits)
AUDIO_CHANNELS = 1  # Number of channels (1 = mono, 2 = stereo)
RATE = 44100  # Sampling rate
RECORD_SECONDS = 5  # Recording time in seconds
OUTPUT_FILENAME = "audio.wav"  # Output file name

audio = pyaudio.PyAudio()

# Open a stream to capture the audio
stream = audio.open(format=QUANT,
                    channels=AUDIO_CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
print("Recording audio...")

frames = []

# Record the audio in chunks
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("\n\nRecording finished")

# Stop the audio capture stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a WAV file
wf = wave.open(OUTPUT_FILENAME, 'wb')
wf.setnchannels(AUDIO_CHANNELS)
wf.setsampwidth(audio.get_sample_size(QUANT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
