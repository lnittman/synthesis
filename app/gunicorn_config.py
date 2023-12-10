# gunicorn_config.py

bind = "192.168.1.210:8000"
workers = 2  # Adjust the number of workers to your needs
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 0
loglevel = "info"