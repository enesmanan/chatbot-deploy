import base64
import json
import os
import tempfile
from uuid import uuid4

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, session

import database
import gemini
import utils

app = Flask(__name__)
app.secret_key = os.urandom(24)

load_dotenv()

database.init_db()

app_title = "Stil Danışmanı"


@app.route("/")
def home():
    if "session_id" not in session:
        session["session_id"] = str(uuid4())
        database.create_conversation(session["session_id"])

    conversations = database.get_all_conversations()
    conversation_history = database.get_conversation_history(session["session_id"])
    return render_template(
        "index.html",
        conversation_history=conversation_history,
        conversations=conversations,
        current_session=session["session_id"],
        renderMarkdown=utils.renderMarkdown,
    )


@app.route("/conversation/<session_id>")
def load_conversation(session_id):
    try:
        session["session_id"] = session_id
        conversation_history = database.get_conversation_history(session_id)
        conversations = database.get_all_conversations()
        return render_template(
            "index.html",
            conversation_history=conversation_history,
            conversations=conversations,
            current_session=session_id,
            renderMarkdown=utils.renderMarkdown,
        )
    except Exception as e:
        print(f"Error loading conversation: {e}")
        return "Konuşma yüklenirken bir hata oluştu", 500


@app.route("/new_chat", methods=["POST"])
def new_chat():
    try:
        session["session_id"] = str(uuid4())
        database.create_conversation(session["session_id"])
        return jsonify({"success": True})
    except Exception as e:
        print(f"Error creating new chat: {e}")
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/send_message", methods=["POST"])
def send_message():
    try:
        if "session_id" not in session:
            raise ValueError("No active session")

        user_message = request.json.get("message", "").strip()
        gender = request.json.get("gender", "erkek")
        image_data = request.json.get("image")

        if not user_message and not image_data:
            raise ValueError("Empty message and no image")

        # if first message, update conversation title
        database.update_conversation_title(
            session["session_id"], user_message[:50] or "Fotoğraf Analizi"
        )

        # if image exists, save to temporary file
        temp_image_path = None
        if image_data:
            try:
                # create image from base64 data
                image_data = image_data.split(",")[1]  # get base64 data
                image_bytes = base64.b64decode(image_data)

                # create temporary file
                fd, temp_image_path = tempfile.mkstemp(suffix=".jpg")
                with os.fdopen(fd, "wb") as f:
                    f.write(image_bytes)
            except Exception as e:
                print(f"Error processing image: {e}")
                temp_image_path = None

        # process message and get response
        response = utils.process_query(
            user_message,
            session["session_id"],
            database,
            gemini,
            gender,
            temp_image_path,
        )

        # delete temporary file
        if temp_image_path and os.path.exists(temp_image_path):
            os.remove(temp_image_path)

        # get conversation history
        conversation_history = database.get_conversation_history(session["session_id"])

        return jsonify(
            {
                "response": response,
                "conversation_history": conversation_history,
                "conversations": database.get_all_conversations(),
            }
        )
    except Exception as e:
        print(f"Error sending message: {e}")
        # delete temporary file (in case of error)
        if (
            "temp_image_path" in locals()
            and temp_image_path
            and os.path.exists(temp_image_path)
        ):
            os.remove(temp_image_path)

        return (
            jsonify(
                {"error": "Mesaj gönderilirken bir hata oluştu", "details": str(e)}
            ),
            500,
        )


if __name__ == "__main__":
    app.run(debug=True)
