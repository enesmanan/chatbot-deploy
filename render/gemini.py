import base64
import os
import time

import requests


def call_gemini(messages, gender="erkek", image_path=None):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

    system_prompt = f"""
    Sen bir yapay zeka destekli stil danışmanısın. Kullanıcılara kişisel stil, giyim, moda ve gardırop düzenleme konularında yardımcı oluyorsun.
    
    Kendini tanıtırken sadece "Ben stil danışmanınızım" veya "Stil Danışmanı" olarak tanıt, başka isim kullanma.
    
    Kullanıcıların sorularına nazik, bilgilendirici ve yardımcı bir şekilde yanıt ver.
    
    ÖNEMLİ: Kullanıcının cinsiyeti: {gender.upper()}. Tüm önerilerini ve tavsiyeleri bu cinsiyete uygun olarak sunmalısın.
    """

    # simplified message format
    gemini_messages = []

    # add system prompt as first message
    gemini_messages.append({"role": "user", "parts": [{"text": system_prompt}]})

    # add user messages
    for msg in messages:
        role = "user" if msg["role"] == "user" else "model"
        gemini_messages.append({"role": role, "parts": [{"text": msg["content"]}]})

    # add image to last user message
    if image_path and os.path.exists(image_path):
        try:
            with open(image_path, "rb") as img_file:
                image_bytes = img_file.read()

            # convert to base64
            image_base64 = base64.b64encode(image_bytes).decode("utf-8")

            # determine MIME type
            mime_type = "image/jpeg"  # default is JPEG
            if image_path.lower().endswith(".png"):
                mime_type = "image/png"
            elif image_path.lower().endswith(".gif"):
                mime_type = "image/gif"

            # replace last user message with image
            last_user_message = gemini_messages[-1]
            if last_user_message["role"] == "user":
                # get existing text
                text_content = last_user_message["parts"][0]["text"]

                # create new parts - use user's own question
                new_parts = [
                    {"inline_data": {"mime_type": mime_type, "data": image_base64}},
                    {"text": text_content},
                ]

                # update message
                last_user_message["parts"] = new_parts
        except Exception as e:
            print(f"Error processing image for Gemini: {e}")

    # request body
    body = {
        "contents": gemini_messages,
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 2048,
            "topP": 0.95,
            "topK": 40,
        },
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        response_json = response.json()

        # extract response
        if "candidates" in response_json and len(response_json["candidates"]) > 0:
            candidate = response_json["candidates"][0]
            if "content" in candidate and "parts" in candidate["content"]:
                parts = candidate["content"]["parts"]
                if parts and "text" in parts[0]:
                    return parts[0]["text"]

        # if response is not in expected format
        return "Üzgünüm, yanıt oluşturulamadı. Lütfen tekrar deneyin."

    except Exception as e:
        print(f"Gemini API error: {e}")
        return "Üzgünüm, bir hata oluştu. Lütfen tekrar deneyin."
