FROM python:3.11-slim-buster

WORKDIR /app

# Install Postgres build dependencies
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev postgresql-client \
    && apt-get install -y nginx

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Nginx configuration
COPY /ops/nginx/nginx.conf /etc/nginx/nginx.conf

# Custom initialization script
COPY init.sql /docker-entrypoint-initdb.d/init.sql

COPY . /app
RUN chmod +x run_migrations.sh && chmod +x entrypoint.sh

EXPOSE 8080 80

# Run the application
CMD ["/bin/bash", "/app/entrypoint.sh"]
