# 🍳 Mutfak Asistanı

Mutfak Asistanı, elinizde bulunan malzemelere göre yemek tarifleri öneren akıllı bir yardımcıdır. Malzemelerinizi yazılı olarak girebilir veya malzemelerin fotoğrafını yükleyerek AI destekli öneriler alabilirsiniz.


## ✨ Özellikler

- 📝 Metin tabanlı malzeme girişi
- 📸 Malzemelerin fotoğrafını yükleme ve otomatik tanıma
- 🇹🇷 Öncelikli olarak Türk mutfağı odaklı tarif önerileri
- 🌍 Dünya mutfaklarından alternatif öneriler
- 📋 Detaylı tarif ve malzeme listeleri
- 💡 Eksik malzemeler için alternatif öneriler

## 🚀 Kurulum

### Ön Koşullar

- Python 3.10 veya üzeri

### Adımlar

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

2. `.env` dosyasını oluşturun ve Gemini API anahtarınızı ekleyin:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
   
   > API anahtarını [Google AI Studio](https://aistudio.google.com/app/apikey) adresinden alabilirsiniz.

3. Uygulamayı çalıştırın:
   ```bash
   streamlit run app.py
   ```

## 📖 Kullanım

1. Uygulamayı başlattıktan sonra, web tarayıcınızda otomatik olarak açılacaktır (genellikle http://localhost:8501).
2. İki seçenekten birini kullanabilirsiniz:
   - **Metin ile malzeme girin**: Elinizdeki malzemeleri yazarak girebilirsiniz.
   - **Malzemelerin fotoğrafını yükleyin**: Malzemelerin bir fotoğrafını çekip yükleyebilirsiniz.
3. Asistan, girdiğiniz malzemelere göre size en uygun tarifleri sunacaktır.
4. Her tarif için detaylı malzeme listesi ve yapılış adımlarını görebilirsiniz.



## 📂 Proje Yapısı

```mutfak-asistani/
├── app.py                 
├── requirements.txt       
├── .gitignore             
└── README.md 
```
