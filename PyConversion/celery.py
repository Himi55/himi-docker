import os
from django.conf import settings
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PyConversion.settings')

app = Celery('PyConversion')
app.config_from_object('django.conf:settings', namespace='')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(settings.INSTALLED_APPS)

BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://redis:6379/1')
app.conf.broker_url = BASE_REDIS_URL
app.conf.result_backend = BASE_REDIS_URL
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
