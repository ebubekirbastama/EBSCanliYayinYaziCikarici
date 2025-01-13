
🎙️ **Sesli Tanıma Uygulaması (Speech Recognition Application)**

Bu proje, Python ve Vosk kütüphanesi kullanılarak geliştirilmiş bir sesli tanıma uygulamasıdır. Mikrofon girişini kullanarak gerçek zamanlı ses kaydı yapar ve metin dosyasına çevirir.

---

### 📋 **Gereksinimler**

Bu projeyi çalıştırmak için aşağıdaki gereksinimlerin yüklü olması gerekmektedir:

1. **Python 3.8+** - Python'un en az 3.8 sürümü yüklü olmalıdır.
2. **pyaudio** - Mikrofon girişini okumak için.
3. **vosk** - Ses tanıma kütüphanesi.
4. **asyncio** - Asenkron işlemler için (Python'un standart bir modülüdür).
5. **json** ve **datetime** - Veri işlemleri için (Python'un standart modülleridir).

---

### 🔧 **Kurulum Adımları**

1. **Gereksinimleri Yükleyin:**
   Aşağıdaki komutu çalıştırarak gerekli Python kütüphanelerini yükleyin:
   ```bash
   pip install vosk pyaudio
   ```

2. **Vosk Model Dosyasını İndirin:**
   Türkçe dil tanıma için gerekli modeli aşağıdaki bağlantıdan indirin:
   [👉 Modeli İndir](https://drive.google.com/file/d/1zrWxOLMIfnNLYnyzmg2TtGSK2lg0eur2/view?usp=sharing)

3. **Model Dosyasını Yerleştirin:**
   İndirilen dosyayı açın ve `vosk-model-small-tr-0.3` klasörünü Python dosyasının olduğu dizine yerleştirin.

4. **Kodun Çalıştırılması:**
   Python dosyasını şu şekilde çalıştırın:
   ```bash
   python dosya_adi.py
   ```

---

### 🖥️ **Kullanım Talimatları**

1. **Mikrofon Seçimi:**
   Program başlatıldığında aktif mikrofon cihazlarının bir listesini göreceksiniz. Kullanmak istediğiniz mikrofon cihazının numarasını girin.

2. **Ses Tanıma:**
   Konuşmaya başladığınızda, program gerçek zamanlı olarak konuşmanızı tanıyacak ve ekranda gösterecektir.

3. **Metin Dosyası:**
   Tanınan konuşmalar, programın çalıştırıldığı dizinde `ses_kayit_[timestamp].txt` formatında kaydedilecektir.

---

### 🌟 **Özellikler**

- Gerçek zamanlı konuşma tanıma.
- Tanınan konuşmaların .txt dosyasına kaydedilmesi.
- Türkçe dil desteği.
- Çoklu mikrofon seçeneği.

---

### 🚨 **Hata ve Çözümleri**

1. **Model Dosyasının Bulunamaması:**
   Model dosyasının Python dosyasının olduğu dizine yerleştirildiğinden emin olun. Aksi takdirde, `Model("vosk-model-small-tr-0.3")` kısmında belirtilen yolu düzenleyin.

---

