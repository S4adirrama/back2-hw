from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.database import SessionLocal
from src.models.songs import Song
from src.assistants.openai_assistant import OpenAIAssistant
import random

router = APIRouter()
assistant = OpenAIAssistant()

@router.get("/explain")
def explain_random_song():
    db: Session = SessionLocal()
    songs = db.query(Song).all()
    db.close()

    if not songs:
        raise HTTPException(status_code=404, detail="No songs found")

    song = random.choice(songs)
    explanation = assistant.explain(song)
    return {
        "title": song.title,
        "artist": song.artist,
        "explanation": explanation,
    }
