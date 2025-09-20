# Discord Developer Badge Bot 🎖️

Ein selbst-gehosteter Discord Bot, der automatisch an die monatliche Aktivität für den Discord Active Developer Badge erinnert.

[![Docker Build & Push](https://github.com/L0ine/Discord-Bot-Devoloper-Badge/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/L0ine/Discord-Bot-Devoloper-Badge/actions/workflows/docker-publish.yml)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/L0ine/Discord-Bot-Devoloper-Badge)](https://github.com/L0ine/Discord-Bot-Devoloper-Badge/releases)
[![Docker Pulls](https://img.shields.io/badge/docker-ghcr.io-blue)](https://github.com/L0ine/Discord-Bot-Devoloper-Badge/pkgs/container/discord-bot-devoloper-badge)

## 🚀 Features

- **Automatische Erinnerungen**: Sendet monatliche DM-Nachrichten
- **Slash Commands & Prefix Commands**: Unterstützt beide Command-Arten
- **Docker Support**: Einfache Bereitstellung mit Docker
- **Multi-Platform**: Läuft auf AMD64 und ARM64
- **Logging**: Ausführliche Protokollierung
- **Health Checks**: Überwachung des Bot-Status

## 📋 Commands

| Command | Prefix | Slash | Beschreibung |
|---------|--------|-------|-------------|
| ping | `!ping` | `/ping` | Bot-Latenz testen & Badge-Aktivität |
| uptime | `!uptime` | `/uptime` | Bot-Laufzeit anzeigen |
| status | `!status` | `/status` | Bot-Status Details |
| help | `!hilfe` | `/help` | Command-Übersicht |
| test | `!test` | `/test` | Test-Erinnerung senden |

## 🐳 Docker Installation (Empfohlen)

### Methode 1: Docker Compose (Einfach)

1. **Repository klonen**:
```bash
git clone https://github.com/L0ine/Discord-Bot-Devoloper-Badge.git
cd Discord-Bot-Devoloper-Badge
```

2. **Umgebungsvariablen einrichten**:
```bash
cp .env.example .env
# .env bearbeiten und Token eintragen
```

3. **Bot starten**:
```bash
docker-compose up -d
```

### Methode 2: Nur Docker

```bash
# Image herunterladen
docker pull ghcr.io/l0ine/discord-bot-devoloper-badge:latest

# Container starten
docker run -d \
  --name discord-dev-badge-bot \
  --restart unless-stopped \
  -e DISCORD_BOT_TOKEN="dein_token_hier" \
  -e CLIENT_ID="deine_client_id" \
  -e GUILD_ID="deine_guild_id" \
  -e YOUR_USER_ID="deine_user_id" \
  ghcr.io/l0ine/discord-bot-devoloper-badge:latest
```

## ⚙️ Setup

### 1. Discord Application erstellen

1. Gehe zu [Discord Developer Portal](https://discord.com/developers/applications)
2. Erstelle eine neue Application
3. Gehe zu "Bot" → "Add Bot"
4. Kopiere den **Token**
5. Notiere dir die **Client ID** (Application ID)

### 2. Bot zu Server hinzufügen

```
https://discord.com/api/oauth2/authorize?client_id=DEINE_CLIENT_ID&permissions=2048&scope=bot%20applications.commands
```

### 3. Umgebungsvariablen

Erstelle eine `.env` Datei:

```env
DISCORD_BOT_TOKEN=dein_discord_bot_token
CLIENT_ID=deine_client_id
GUILD_ID=deine_server_id_optional
YOUR_USER_ID=deine_user_id_optional
```

| Variable | Erforderlich | Beschreibung |
|----------|--------------|-------------|
| `DISCORD_BOT_TOKEN` | ✅ | Bot Token aus Discord Developer Portal |
| `CLIENT_ID` | ✅ | Application ID (für Slash Commands) |
| `GUILD_ID` | ❌ | Server ID (für lokale Slash Commands) |
| `YOUR_USER_ID` | ❌ | Deine User ID (für DM-Erinnerungen) |

## 🔧 Lokale Installation

### Voraussetzungen
- Python 3.11+
- pip

### Installation

1. **Repository klonen**:
```bash
git clone https://github.com/L0ine/Discord-Bot-Devoloper-Badge.git
cd Discord-Bot-Devoloper-Badge
```

2. **Virtual Environment erstellen**:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# oder
.venv\Scripts\activate  # Windows
```

3. **Dependencies installieren**:
```bash
pip install -r requirements.txt
```

4. **Bot starten**:
```bash
python discord-dev-badge-bot.py
```

## 📊 Monitoring

### Container Logs anzeigen
```bash
docker-compose logs -f discord-dev-badge-bot
```

### Container Status prüfen
```bash
docker-compose ps
```

### Health Check
```bash
docker inspect --format='{{.State.Health.Status}}' discord-dev-badge-bot
```

## 🛠️ Entwicklung

### Lokale Entwicklung

```bash
# Development setup
git clone https://github.com/L0ine/Discord-Bot-Devoloper-Badge.git
cd Discord-Bot-Devoloper-Badge
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Bot starten
python discord-dev-badge-bot.py
```

### Docker Build (Lokal)

```bash
# Image bauen
docker build -t discord-dev-badge-bot .

# Container starten
docker run -d --env-file .env discord-dev-badge-bot
```

## 📦 GitHub Container Registry

Das Docker Image wird automatisch bei jedem Push auf `main` erstellt und in der GitHub Container Registry veröffentlicht:

- **Registry**: `ghcr.io/l0ine/discord-bot-devoloper-badge`
- **Tags**: `latest`, `main`, version tags
- **Platforms**: `linux/amd64`, `linux/arm64`

## 🎯 Discord Developer Badge

Um den **Active Developer Badge** zu erhalten und zu behalten:

1. Erstelle eine Discord Application
2. Nutze mindestens **einmal pro Monat** einen Slash Command (`/ping`)
3. Der Bot erinnert dich automatisch per DM

## 📝 Changelog

### v1.2.0
- Multi-Platform Docker Support (AMD64 + ARM64)
- Verbessertes Docker Compose Setup
- GitHub Actions Workflow für automatische Builds
- Health Checks hinzugefügt
- Security Verbesserungen (Non-root User)

### v1.1.0
- Slash Commands hinzugefügt
- Automatische DM-Erinnerungen
- Docker Support

### v1.0.0
- Initiale Version
- Basic Ping Command

## 🤝 Mitwirken

1. Fork das Repository
2. Erstelle einen Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Committe deine Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Push zum Branch (`git push origin feature/AmazingFeature`)
5. Öffne eine Pull Request

## 📄 Lizenz

Dieses Projekt ist unter der MIT Lizenz lizenziert - siehe [LICENSE](LICENSE) Datei für Details.

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/L0ine/Discord-Bot-Devoloper-Badge/issues)
- **Discussions**: [GitHub Discussions](https://github.com/L0ine/Discord-Bot-Devoloper-Badge/discussions)

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=L0ine/Discord-Bot-Devoloper-Badge&type=Date)](https://star-history.com/#L0ine/Discord-Bot-Devoloper-Badge&Date)

---

**Wichtig**: Der Bot muss mindestens einmal pro Monat einen Slash Command ausführen, um den Developer Badge aktiv zu halten!