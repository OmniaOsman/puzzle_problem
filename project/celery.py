import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')


app = Celery('project', broker='redis://localhost', backend='db+sqlite:///results.sqlite')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.retry = 360
app.conf.timeout = 300

# Load task modules from all registered Django apps.
app.autodiscover_tasks()



