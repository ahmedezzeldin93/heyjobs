broker_url = 'pyamqp://localhost:5672'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Berlin'
enable_utc = True
CELERY_IMPORTS=("job_app.tasks")
CELERY_IGNORE_RESULT=False