import pyaudio
from vosk import Model, KaldiRecognizer
import json
import asyncio
import os
from datetime import datetime

# Modelin doğru yolunu belirtin
model = Model("vosk-model-small-tr-0.3")  # Modelin tam yolunu buraya yazın

# Mikrofon cihazlarını listele (sadece aktif olanları)
p = pyaudio.PyAudio()
device_count = p.get_device_count()

print("Aktif mikrofon cihazları:")
active_devices = []

for i in range(device_count):
    info = p.get_device_info_by_index(i)
    if info['maxInputChannels'] > 0:  # Sadece giriş (input) destekleyen cihazları listele
        active_devices.append((i, info['name']))
        print(f"{i}: {info['name']}")

if not active_devices:
    print("Aktif mikrofon bulunamadı.")

# Asenkron olarak ses tanıma ve yazma işlemi
async def recognize_and_write(device_index):
    # Dosya adı, programın başlatılma zamanına göre benzersiz yapılır
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"ses_kayit_{timestamp}.txt"

    # Ses kaynağını başlat
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4000, input_device_index=device_index)
    stream.start_stream()

    recognizer = KaldiRecognizer(model, 16000)

    # txt dosyasına yazma işlemi (Asenkron)
    async def write_to_file(text):
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(text + "\n")

    # Ses kaydetme ve tanıma döngüsü
    while True:
        data = stream.read(4000)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text = json.loads(result)["text"]
            print(text)  # Ekrana yazdır
            await write_to_file(text)  # Dosyaya asenkron yaz

# Kullanıcıdan mikrofon seçmesini isteyin ve asenkron fonksiyonu başlatın
if active_devices:
    device_index = int(input("Kullanmak istediğiniz mikrofon cihazının numarasını girin: "))
    asyncio.run(recognize_and_write(device_index))
