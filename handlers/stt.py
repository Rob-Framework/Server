import struct
import wave
import whisper
import ssl
from pvrecorder import PvRecorder

ssl._create_default_https_context = ssl._create_unverified_context

for index, device in enumerate(PvRecorder.get_audio_devices()):
    print(f"[{index}] {device}")
# 1

recorder = PvRecorder(device_index=-1, frame_length=512)

recorder = PvRecorder(device_index=-1, frame_length=512)
audio = []

model = whisper.load_model("base")
c = 0

recorder.start()
print("recording started")

while True:
    frame = recorder.read()
    audio.extend(frame)
    c += 1
    print(c)

    if (c > 100):
        print("done")
        recorder.stop()
        with wave.open("test.wav", 'w') as f:
            f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(audio), *audio))
        result = model.transcribe("test.wav", fp16=False)
        print(result['text'])
