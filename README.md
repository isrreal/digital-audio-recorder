# Audio Recording Script

This repository contains a Python script that captures audio from a microphone and saves it to a WAV file. The script uses the `PyAudio` and `wave` libraries to record and process the audio.

## Features

- **Audio Recording**: Captures audio input from a microphone using the PyAudio library.
- **WAV File Output**: Saves the recorded audio as a `.wav` file, which is widely supported across different platforms.
- **Customizable Settings**: You can easily adjust the recording time, sample rate, and output file name.

## How It Works

1. The script initializes a PyAudio stream to capture audio input.
2. Audio is recorded in chunks, with each chunk representing a small portion of the audio data.
3. After the specified recording time (in seconds), the stream stops, and the captured data is written to a `.wav` file.
4. The final output file is saved with the name specified in the script.

## Prerequisites

Before running the script, you need to install the following libraries:

- `PyAudio`: Used for capturing audio.
- `wave`: Used for saving the audio as a WAV file.

You can install the required packages using `pip`:

```bash
pip install pyaudio
