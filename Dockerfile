# Python-Image
FROM python:3.11-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Dependencies installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code reinkopieren
COPY . .

# Startkommando
CMD ["python", "discord-dev-badge-bot.py"]
