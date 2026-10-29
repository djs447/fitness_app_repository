import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_app.settings')

app = Celery('fitness_app', broker='redis://127.0.0.1:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(['fitness_app'])

if __name__ == '__main__':
    app.start()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')