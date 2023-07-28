FROM python:3.11.4-slim-bookworm
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY django-gunicorn-nginx django-gunicorn-nginx
RUN bash -c 'mkdir -p /var/{log,run}/gunicorn/'
RUN bash -c 'chown -R root:root /var/{log,run}/gunicorn/'
WORKDIR /app/django-gunicorn-nginx
#CMD ["gunicorn", "--config", "./config/gunicorn/dev.py"]