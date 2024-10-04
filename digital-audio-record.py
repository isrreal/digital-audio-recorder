import pyaudio
import wave

CHUNK = 1024 # Tamanho do chunk de áudio, usado como uma taxa de atualização, a cada iteração, para cada gravar o áudio digitalizado.
QUANT = pyaudio.paInt # Formato de quantização do áudio (16 bits)
CANAIS_DE_AUDIO = 1 # Número de canais (1 = mono, 2 = estéreo)
RATE = 44100 # Taxa de amostragem 
RECORD_SECONDS = 5 # Tempo de gravação em segundos
NOME_DO_ARQUIVO = "audio.wav" # Nome do arquivo de saída

audio = pyaudio.PyAudio()

# Abre um stream para capturar o áudio
stream = audio.open(format = QUANT,
                channels = CANAIS_DE_AUDIO,
                rate = RATE,
                input = True,
                frames_per_buffer = CHUNK)
print("Gravando áudio...")

frames = []

# Grava o áudio em chunks
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("\n\nGravação finalizada")

# Para o stream de captura
stream.stop_stream()
stream.close()
audio.terminate()

# Salva o áudio gravado em um arquivo WAV
wf = wave.open(NOME_DO_ARQUIVO, 'wb')
wf.setnchannels(CANAIS_DE_AUDIO)
wf.setsampwidth(audio.get_sample_size(QUANT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

