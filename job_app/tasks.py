from celery import Celery

from settings import CELERY_SETTINGS
from testing import test_model


"""
Configure the following:
- project: name of project, usually a module to identify namespace
- config_from_object: import path to kipp_celery_config
"""

app = Celery("job_app")
app.config_from_object(CELERY_SETTINGS)
app = Celery()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5.0, predict_new_created_jobs.s(), name='Predict every 1 min')


@app.task
def predict_new_created_jobs():
    test_model()