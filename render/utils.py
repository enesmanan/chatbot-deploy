from markdown import markdown


def renderMarkdown(text):
    """Convert markdown to HTML"""
    return markdown(text, extensions=["fenced_code", "tables"])


def process_query(query, session_id, database, gemini, gender="erkek", image_path=None):
    """Process user query and generate response"""
    try:
        conversation_history = database.get_conversation_history(session_id)
        messages = conversation_history + [{"role": "user", "content": query}]

        # get response from Gemini
        response = gemini.call_gemini(messages, gender, image_path)

        # save messages
        if not database.save_message(
            session_id, "user", query + (" [Fotoğraf içeriyor]" if image_path else "")
        ):
            raise Exception("Failed to save user message")
        if not database.save_message(session_id, "assistant", response):
            raise Exception("Failed to save assistant message")

        return response
    except Exception as e:
        print(f"Error processing query: {e}")
        return "Üzgünüm, bir hata oluştu. Lütfen tekrar deneyin."
