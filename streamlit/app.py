import io
import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY or GOOGLE_API_KEY == "your_api_key_here":
    st.error("Lütfen .env dosyasında GOOGLE_API_KEY'i ayarlayın.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Mutfak Asistanı", page_icon="🍳")
st.title("🍳 Mutfak Asistanı")
st.subheader("Elinizde bulunan malzemelerle neler yapabileceğinizi keşfedin")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Merhaba! Elinizde bulunan malzemeleri yazabilir veya fotoğrafını yükleyebilirsiniz. Size uygun tarifler önereceğim.",
        }
    ]

system_instruction = """
Sen bir şef chatbotusun. Kullanıcıların elindeki malzemelere göre yemek tarifleri öneriyorsun.
Aşağıdaki kurallara uy:
1. Öncelikle Türk mutfağından tarifler öner, ancak istenirse diğer mutfaklardan da öneriler sunabilirsin.
2. Kullanıcı malzemeleri metin olarak girdiğinde veya resim yüklediğinde, bu malzemelerle yapılabilecek tarifleri öner.
3. Her tarif için malzeme listesi ve yapılış adımlarını detaylı olarak açıkla.
4. Eğer eksik malzemeler varsa, alternatif malzemeler veya basitleştirilmiş tarifler öner.
5. Cevaplarını Türkçe olarak ver.
6. Resim yüklendiğinde, resimdeki malzemeleri tanımla ve onlarla yapılabilecek tarifleri öner.
"""

# history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

input_option = st.radio(
    "Tarif önerisi alma yöntemi",
    ("Metin ile malzeme girin", "Malzemelerin fotoğrafını yükleyin"),
)

if input_option == "Metin ile malzeme girin":
    user_input = st.chat_input("Malzemelerinizi yazın...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        gemini_messages = []

        gemini_messages.append({"role": "user", "parts": [system_instruction]})
        gemini_messages.append(
            {"role": "model", "parts": ["Anladım, bu kurallara göre hareket edeceğim."]}
        )

        # gecmis mesajlar ile cevap ver
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                gemini_messages.append({"role": "user", "parts": [msg["content"]]})
            elif msg["role"] == "assistant":
                gemini_messages.append({"role": "model", "parts": [msg["content"]]})

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.text("Tarifler hazırlanıyor...")

            response = model.generate_content(gemini_messages)
            assistant_response = response.text

            message_placeholder.write(assistant_response)

        st.session_state.messages.append(
            {"role": "assistant", "content": assistant_response}
        )

else:
    uploaded_file = st.file_uploader(
        "Malzemelerin fotoğrafını yükleyin", type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Yüklenen fotoğraf", use_column_width=True)

        if st.button("Tarif öner"):
            user_message = "Bu fotoğraftaki malzemelerle neler yapabilirim?"
            st.session_state.messages.append({"role": "user", "content": user_message})
            with st.chat_message("user"):
                st.write(user_message)

            gemini_messages = []

            gemini_messages.append({"role": "user", "parts": [system_instruction]})
            gemini_messages.append(
                {
                    "role": "model",
                    "parts": ["Anladım, bu kurallara göre hareket edeceğim."],
                }
            )

            gemini_messages.append(
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": "Bu fotoğrafta hangi malzemeler var? Bu malzemelerle yapılabilecek tarifler önerir misin?"
                        },
                        {
                            "inline_data": {
                                "mime_type": "image/jpeg",
                                "data": uploaded_file.getvalue(),
                            }
                        },
                    ],
                }
            )

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                message_placeholder.text("Fotoğraf analiz ediliyor...")

                try:
                    response = model.generate_content(gemini_messages)
                    assistant_response = response.text

                    message_placeholder.write(assistant_response)

                    # yaniti mevcut mesajlara ekle
                    st.session_state.messages.append(
                        {"role": "assistant", "content": assistant_response}
                    )
                except Exception as e:
                    error_message = f"Bir hata oluştu. Lütfen tekrar deneyin."
                    message_placeholder.error(error_message)
                    st.error(f"Hata detayı: {str(e)}")
