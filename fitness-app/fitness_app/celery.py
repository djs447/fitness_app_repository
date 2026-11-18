import os

from celery import Celery

from .settings import CELERY_BROKER_URL

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fitness_app.settings")

app = Celery("fitness_app", broker=CELERY_BROKER_URL)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(["fitness_app"])

if __name__ == "__main__":
    app.start()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
