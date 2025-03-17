import os
import gradio as gr
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

chat = model.start_chat(history=[])

system_prompt = """
Sen bir film ve dizi öneri asistanısın. Kullanıcıların isteklerine göre film ve dizi önerileri sunarsın.

Öneriler yaparken şu kurallara uy:
- Kullanıcı film/dizi önerisi istediğinde 5 tane öneri sun
- Her öneri için kısa bir açıklama ve oyuncu kadrosunu (cast) belirt
- 3 tane popüler/iyi öneri, 1 tane niş öneri ve 1 tane benzersiz/unique öneri yap
- Kullanıcının sevdiği filmler hakkında bilgi verirse, bunu dikkate alarak öneriler sun
- Sohbet geçmişini dikkate alarak cevaplar ver

Cevaplarını Türkçe olarak ver.
"""

def respond(message, history):
    if not history:
        chat.send_message(system_prompt)
    
    response = chat.send_message(message)
    return response.text

demo = gr.ChatInterface(
    respond,
    title="Film ve Dizi Öneri Asistanı",
    description="Bana film veya dizi önerisi istediğinizi söyleyin. Sevdiğiniz filmleri de belirtebilirsiniz.",
    theme="soft",
    examples=[
        ["Aksiyon filmi önerir misin?"],
        ["Bilim kurgu türünde film önerileri istiyorum"],
        ["Christopher Nolan tarzı filmler seviyorum, bana ne önerirsin?"],
        ["Kore dizisi önerir misin?"]
    ]
)

if __name__ == "__main__":
    demo.launch() 