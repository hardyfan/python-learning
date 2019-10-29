from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery_config import CELERY_BACKEND, CELERY_BROKER

app = Celery('tasks',
             broker=CELERY_BROKER,
             backend=CELERY_BACKEND
             )


@app.task
def add(x, y):
    return x + y
