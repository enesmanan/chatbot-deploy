# Dizi & Film Öneri Asistanı

Bu proje, kullanıcıların dizi ve film önerileri alabileceği bir yapay zeka destekli chatbot uygulamasıdır. Google'ın Gemini 1.5 Flash modelini kullanan bu asistan, kullanıcıların tercihlerine göre kişiselleştirilmiş öneriler sunar.

## 🎬 Özellikler

- **Kişiselleştirilmiş Öneriler**: Kullanıcı tercihlerine ve geçmiş beğenilerine göre öneriler
- **Detaylı Bilgi**: Her öneri için kısa açıklama ve oyuncu kadrosu bilgisi
- **Çeşitlilik**: Her soruda 3 popüler, 1 niş ve 1 benzersiz öneri sunma
- **Sohbet Hafızası**: Sohbet geçmişini hatırlama ve buna göre öneriler yapma
- **Türkçe Destek**: Tamamen Türkçe arayüz ve yanıtlar
- **Kolay Kullanım**: Gradio arayüzü ile basit ve kullanıcı dostu deneyim

## 🚀 Kurulum

### Gereksinimler
- Python 3.10 veya daha yeni sürüm
- Gemini API anahtarı

### Adımlar

1. Gerekli kütüphaneleri yükleyin:
   ```
   pip install -r requirements.txt
   ```

2. `.env` dosyasını oluşturun ve Gemini API anahtarınızı ekleyin:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
   
   API anahtarını [Google AI Studio](https://aistudio.google.com/app/apikey) adresinden alabilirsiniz.

3. Uygulamayı çalıştırın:
   ```
   python app.py
   ```

## 💬 Kullanım

1. Uygulamayı başlattıktan sonra, tarayıcınızda Gradio arayüzü açılacaktır.
2. Metin kutusuna film veya dizi önerisi isteğinizi yazabilirsiniz.
3. Sevdiğiniz film ve dizileri belirterek daha kişiselleştirilmiş öneriler alabilirsiniz.
4. Arayüzdeki hazır örnekleri kullanarak hızlıca başlayabilirsiniz.

## 📝 Örnek Sorular

- "Aksiyon filmi önerir misin?"
- "Bilim kurgu türünde film önerileri istiyorum"
- "Christopher Nolan tarzı filmler seviyorum, bana ne önerirsin?"
- "Kore dizisi önerir misin?"
- "Inception ve Interstellar'ı çok sevdim, benzer filmler önerir misin?"
- "Son 5 yılda çıkan en iyi gerilim filmleri nelerdir?"

## 📂 Proje Yapısı

```
dizi-film-oneri-asistani/
├── app
├── requirements.txt       
├── .gitignore             
└── README.md  
```