web: newrelic-admin run-program gunicorn --pythonpath hackaway hackaway.wsgi -b 0.0.0.0:$PORT --max-requests 50 -t 30
worker: newrelic-admin run-program python hackaway/manage.py celeryd -E -B --loglevel=WARNING
redis: redis-server
