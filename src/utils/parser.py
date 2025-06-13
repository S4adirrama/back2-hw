import requests
from bs4 import BeautifulSoup
from src.models import Song
from src.database import SessionLocal

def fetch_billboard_hot100():
    url = "https://www.billboard.com/charts/hot-100/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    db = SessionLocal()

    songs = soup.select("li.o-chart-results-list__item h3")
    artists = soup.select("li.o-chart-results-list__item span.c-label")

    for i in range(min(len(songs), len(artists))):
        title = songs[i].get_text(strip=True)
        artist = artists[i].get_text(strip=True)
        song = Song(title=title, artist=artist)
        db.add(song)

    db.commit()
    db.close()
