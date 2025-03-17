import sqlite3
from datetime import datetime


def get_db():
    conn = sqlite3.connect("conversations.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        c = conn.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS conversations (
                session_id TEXT PRIMARY KEY,
                title TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        )
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT,
                role TEXT,
                content TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (session_id) REFERENCES conversations (session_id)
                ON DELETE CASCADE
            )
        """
        )
        conn.commit()


def get_conversation_history(session_id):
    try:
        with get_db() as conn:
            c = conn.cursor()
            c.execute(
                "SELECT role, content FROM messages WHERE session_id = ? ORDER BY created_at",
                (session_id,),
            )
            return [
                {"role": row["role"], "content": row["content"]} for row in c.fetchall()
            ]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []


def get_all_conversations():
    try:
        with get_db() as conn:
            c = conn.cursor()
            c.execute(
                "SELECT session_id, title, created_at FROM conversations ORDER BY created_at DESC"
            )
            return [
                {
                    "id": row["session_id"],
                    "title": row["title"],
                    "created_at": row["created_at"],
                }
                for row in c.fetchall()
            ]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []


def save_message(session_id, role, content):
    try:
        with get_db() as conn:
            c = conn.cursor()
            c.execute(
                "INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)",
                (session_id, role, content),
            )
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False


def create_conversation(session_id, title="Yeni Görüşme"):
    try:
        with get_db() as conn:
            c = conn.cursor()
            c.execute(
                "INSERT INTO conversations (session_id, title) VALUES (?, ?)",
                (session_id, title),
            )
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False


def update_conversation_title(session_id, title):
    try:
        with get_db() as conn:
            c = conn.cursor()
            c.execute(
                "UPDATE conversations SET title = ? WHERE session_id = ? AND title = ?",
                (title[:50], session_id, "Yeni Görüşme"),
            )
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
