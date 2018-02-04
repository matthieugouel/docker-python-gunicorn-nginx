"""Gunicorn configuration."""

bind = '127.0.0.1:5000'

workers = 4
worker_class = 'gevent'

accesslog = '-'
