from src.worker import celery
from src.utils.parser import fetch_billboard_hot100

@celery.task
def fetch_billboard_task():
    fetch_billboard_hot100()
