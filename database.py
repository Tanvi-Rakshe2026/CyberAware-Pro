"""SQLite persistence for anonymized assessment summaries."""
import sqlite3
from pathlib import Path
from datetime import datetime, timezone

DB_PATH = Path(__file__).with_name("cyberaware.db")

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS assessments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                participant_id TEXT NOT NULL,
                assessment_type TEXT NOT NULL CHECK(assessment_type IN ('pre', 'post')),
                total_questions INTEGER NOT NULL,
                correct_answers INTEGER NOT NULL,
                score REAL NOT NULL,
                category_scores TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)
        conn.commit()

def save_assessment(participant_id, assessment_type, total_questions, correct_answers, score, category_scores):
    import json
    safe_id = (participant_id or "").strip()
    if not safe_id:
        raise ValueError("Enter an anonymous participant ID.")
    if assessment_type not in ("pre", "post"):
        raise ValueError("Assessment type must be pre or post.")
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with get_connection() as conn:
        cursor = conn.execute("""
            INSERT INTO assessments
            (participant_id, assessment_type, total_questions, correct_answers, score, category_scores, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (safe_id[:40], assessment_type, total_questions, correct_answers, score,
              json.dumps(category_scores, ensure_ascii=False), timestamp))
        conn.commit()
        return cursor.lastrowid

def fetch_assessments():
    import pandas as pd
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT id, participant_id, assessment_type, total_questions,
                   correct_answers, score, category_scores, created_at
            FROM assessments ORDER BY created_at DESC
        """).fetchall()
    return pd.DataFrame([dict(row) for row in rows])

def delete_all_assessments():
    with get_connection() as conn:
        conn.execute("DELETE FROM assessments")
        conn.commit()
