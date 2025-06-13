from celery.schedules import crontab
from src.worker import celery

celery.conf.beat_schedule = {
    "fetch-billboard-every-day": {
        "task": "src.tasks.billboard.fetch_billboard_task",
        "schedule": crontab(hour=10, minute=40),  
    }
}
