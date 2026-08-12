import os
from celery import Celery

# Set default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bulk.settings')

app = Celery('bulk')

# Read config from Django settings using the 'CELERY_' namespace prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks.py inside all installed Django apps
app.autodiscover_tasks()