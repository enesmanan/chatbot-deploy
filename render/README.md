# Stil Danışmanı

Yapay zeka destekli kişisel stil danışmanı uygulaması, kullanıcılara kişiselleştirilmiş moda ve stil tavsiyeleri sunmak için tasarlanmıştır.

## Özellikler

- 👔 Kişisel stil analizi ve öneriler
- 👗 Cinsiyet bazlı stil danışmanlığı (Kadın/Erkek)
- 📸 Fotoğraf yükleme ve analiz etme
- 🧥 Gardırop optimizasyon tavsiyeleri
- 👔 Özel durum stilleri (iş, davet, günlük)

## Teknik Altyapı

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **AI**: Google Gemini 1.5 Flash
- **Veritabanı**: SQLite

## 🚀 Kurulum

1. Repoyu klonlayın
```bash
git clone https://github.com/enesmanan/chatbot-deploy.git
cd chatbot-deploy\render
```

2. Sanal ortam oluşturun ve etkinleştirin
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Gereksinimleri yükleyin
```bash
pip install -r requirements.txt
```

4. Environment dosyasını yapılandırın
Kök dizinde bir `.env` dosyası oluşturun ve aşağıdakileri ekleyin:
```env
GOOGLE_API_KEY=your-google-api-key
```

5. Uygulamayı çalıştırın
```bash
python app.py
```

## 🎯 Kullanım

Tarayıcınızda `http://localhost:5000` adresini ziyaret ederek stil danışmanınızla sohbet etmeye başlayabilirsiniz.

## 📁 Proje Yapısı

```
stil-danismani/
├── app.py                # Ana uygulama dosyası ve Flask rotaları
├── gemini.py             # Google Gemini AI entegrasyonu
├── database.py           # Veritabanı işlemleri
├── utils.py              # Yardımcı fonksiyonlar
├── requirements.txt      # Bağımlılıklar
├── .env                  # Ortam değişkenleri
├── conversations.db      # SQLite veritabanı
├── static/               # Statik dosyalar
│   ├── style.css         # CSS stilleri
│   ├── images/           # Görsel dosyaları
│   └── uploads/          # Kullanıcı yüklemeleri
└── templates/            # HTML şablonları
    └── index.html        # Ana sayfa şablonu
```

## 📞 İletişim

Proje veya işbirliği hakkında sorularınız için:

- **E-posta**: [enesmanan768@gmail.com](mailto:enesmanan768@gmail.com)
- **GitHub**: [github.com/enesmanan](https://github.com/enesmanan)
- **LinkedIn**: [linkedin.com/in/enesfehmimanan](https://linkedin.com/in/enesfehmimanan)

Hata raporları ve öneriler için lütfen GitHub üzerinden issue açınız.





