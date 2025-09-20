FROM python:3.11-slim

WORKDIR /app

# Nur die Abhängigkeiten installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Nur den Bot-Code kopieren
COPY discord-dev-badge-bot.py .

# Standard-Startbefehl, der ENV-Variablen nutzt
CMD ["python", "discord-dev-badge-bot.py"]
