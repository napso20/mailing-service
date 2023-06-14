FROM python:3.11-slim-buster

WORKDIR /app

# Install Postgres build dependencies
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN chmod +x run_migrations.sh

EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
