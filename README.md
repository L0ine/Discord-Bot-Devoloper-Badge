# <img width="40" height="40" alt="discord-logo" src="https://github.com/user-attachments/assets/adabd300-70df-4847-9b34-e51d207d254d" /> <img width="40" height="40" alt="grafik" src="https://github.com/user-attachments/assets/478efc93-83c4-46bc-acb7-94e81883d652" /> Discord Developer Badge Bot

<div align="center">

![Discord Developer Badge](https://img.shields.io/badge/Discord-Developer%20Badge-5865F2?style=for-the-badge&logo=discord&logoColor=white)
[![Docker Build](https://img.shields.io/github/actions/workflow/status/L0ine/Discord-Bot-Devoloper-Badge/docker-publish.yml?style=for-the-badge&logo=docker)](https://github.com/L0ine/Discord-Bot-Devoloper-Badge/actions/workflows/docker-publish.yml)
[![GitHub Release](https://img.shields.io/github/v/release/L0ine/Discord-Bot-Devoloper-Badge?style=for-the-badge&logo=github)](https://github.com/L0ine/Discord-Bot-Devoloper-Badge/releases)
[![Docker Pulls](https://img.shields.io/badge/Docker-Available-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://github.com/L0ine/Discord-Bot-Devoloper-Badge/pkgs/container/discord-bot-devoloper-badge)


**🚀 Self-hosted bot that gives you the Developer Badge in Discord ! 🚀**

[📋 Quick Start](#-quick-start) • [🎯 Badge Anleitung](#-discord-developer-badge-erhalten) • [🐳 Docker Setup](#-installation) 

</div>

---

## 🎯 Getting the Discord Developer Badge

### ❓ Was ist der Active Developer Badge?

What is the **Active Developer Badge?** The Discord Active Developer Badge is an **exclusive profile badge** for developers actively creating and running Discord bots. It shows others you’re a real Discord developer.


| This is what you get! | 
|-------|
 <img width="296" height="397" alt="grafik" src="https://github.com/user-attachments/assets/b5ba47e6-f01e-4429-95e6-a02b5e75d053" />


### 📋 Badge Requirements (Full Guide):

#### ** Step 1: Discord Application **
1. 🌐 Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. 🆕 Click on **"New Application"**
3. 📝 Name Your Bot
4. 🆔 Copy the Application Key 
5. 🤖 Go to **"Bot"** Click Reset Token and copy

#### **Step 2: Bot Permission Config**
1. ⚙️ In Bot Settings → **"Privileged Gateway Intents"**:
   - ✅ Message Content Intent (optional)
   - ✅ Server Members Intent (optional)
2. 🛡️ In **"OAuth2"** → **"URL Generator"**:
   - ✅ Scopes: `bot`
   - ✅ Permissions: `Administrator`
  
#### **Step 3: Invite Bot to Server**
```
🔗 Invite Link Template:
https://discord.com/api/oauth2/authorize?client_id=DEINE_CLIENT_ID&permissions=2048&scope=bot%20applications.commands
```
**Replace `YOUR_CLIENT_ID` with your real Application ID!**

Or if you want to make your Bot privat   Disable Public Bot - Go to Installation > Install Link and select none

---

## 🐳 Installation

### 🚀 Option 1: Ein-Zeiler (Schnellste Methode)

```bash
docker run -d \
  --name discord-dev-badge-bot \
  --restart unless-stopped \
  -e DISCORD_BOT_TOKEN="dein_bot_token" \
  -e CLIENT_ID="deine_client_id" \
  ghcr.io/l0ine/discord-bot-devoloper-badge:latest
```

### 🛠️ Option 2: Docker Compose (Empfohlen für Production)

```bash
# Repository klonen
git clone https://github.com/L0ine/Discord-Bot-Devoloper-Badge.git
cd Discord-Bot-Devoloper-Badge

# Umgebung konfigurieren
cp .env.example .env
# Editiere .env mit deinen Discord-Werten

# Bot starten
docker-compose up -d

# Status prüfen
docker-compose logs -f
```

### 🔧 Option 3: Lokale Installation (Entwickler)

```bash
# Python 3.11+ benötigt
git clone https://github.com/L0ine/Discord-Bot-Devoloper-Badge.git
cd Discord-Bot-Devoloper-Badge

# Virtual Environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# Dependencies
pip install -r requirements.txt

# Bot starten
python discord-dev-badge-bot.py
```

---

## ⚙️ Konfiguration

### 📋 Erforderliche Umgebungsvariablen

| Variable | Erforderlich | Beschreibung |
|----------|--------------|-------------|
| `DISCORD_BOT_TOKEN` | ✅ **JA** | Bot Token aus Developer Portal |
| `CLIENT_ID` | ✅ **JA** | Application ID für Slash Commands | 
| `GUILD_ID` | ❌ Optional | Server ID (für lokale Commands) | 
| `YOUR_USER_ID` | ❌ Optional | Deine User ID (für DMs) | 

### 📄 .env Datei Beispiel

```env
# Discord Bot Configuration
DISCORD_BOT_TOKEN=
CLIENT_ID=
GUILD_ID=  
YOUR_USER_ID=  
```



#### **Step 4: Bot aktivieren (Das macht dieser Bot!)**
- 🏓 **Mindestens 1x pro Monat** einen Slash Command ausführen
- ✅ **Unser Bot erinnert dich automatisch** per DM
- 📱 **Ein einfaches `/ping`** reicht schon aus!
- ⏰ **25-Tage Erinnerungsintervall** (sicher vor Ablauf)

#### **Phase 5: Badge beantragen**
1. 🌐 Zurück zum [Developer Portal](https://discord.com/developers/applications)
2. 🎖️ Deine App auswählen → **"Active Developer"**
3. ✅ Auf **"Get Badge"** klicken
4. 🎉 **Badge erscheint in deinem Profil!**






---

## 📊 Monitoring & Wartung

### 🔍 Container Status prüfen

```bash
# Container Status
docker ps | grep discord-dev-badge-bot

# Live Logs anzeigen
docker logs -f discord-dev-badge-bot

# Resource Verbrauch
docker stats discord-dev-badge-bot
```

### 🛠️ Troubleshooting

<details>
<summary>🚨 Bot startet nicht</summary>

**Mögliche Ursachen:**
- ❌ Falscher/abgelaufener Bot Token
- ❌ Fehlende Umgebungsvariablen
- ❌ Bot nicht in Server eingeladen

**Lösungen:**
```bash
# Logs prüfen
docker logs discord-dev-badge-bot

# Container neu starten
docker restart discord-dev-badge-bot

# Token validieren
# Neuen Token aus Developer Portal holen
```
</details>

<details>
<summary>⚡ Slash Commands funktionieren nicht</summary>

**Mögliche Ursachen:**
- ❌ `CLIENT_ID` nicht gesetzt
- ❌ Bot hat keine `applications.commands` Permission
- ❌ Commands brauchen 5-10 Minuten zum Registrieren

**Lösungen:**
```bash
# CLIENT_ID überprüfen
echo $CLIENT_ID

# Bot mit korrekten Permissions neu einladen
https://discord.com/api/oauth2/authorize?client_id=DEINE_ID&permissions=2048&scope=bot%20applications.commands

# 10 Minuten warten, dann /ping testen
```
</details>

<details>
<summary>📱 Keine DM-Erinnerungen</summary>

**Mögliche Ursachen:**
- ❌ DMs deaktiviert
- ❌ Bot kennt deine User ID nicht
- ❌ Bot offline

**Lösungen:**
```bash
# Einmal /ping ausführen (registriert deine ID)
# DM-Einstellungen in Discord prüfen
# YOUR_USER_ID manuell in .env setzen
```
</details>

---

### 💡 Community Ideen

<details>
<summary>🎖️ Badge Achievement System</summary>

```javascript
// Beispiel: Badge Streak Tracking
{
  "user": "123456789",
  "badges": {
    "current_streak": 12,        // 12 Monate in Folge
    "longest_streak": 24,        // Rekord: 24 Monate
    "total_pings": 156,          // Gesamt /ping Commands
    "badge_since": "2023-01-15"  // Badge erhalten am
  }
}
```
</details>


### 🎉 Contributors


<div align="center">

[![Contributors](https://contrib.rocks/image?repo=L0ine/Discord-Bot-Devoloper-Badge)](https://github.com/L0ine/Discord-Bot-Devoloper-Badge/graphs/contributors)

</div>

---

## 📄 Lizenz & Support

<div align="center">

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://choosealicense.com/licenses/mit/)
[![Support](https://img.shields.io/badge/Support-GitHub%20Issues-red?style=for-the-badge&logo=github)](https://github.com/L0ine/Discord-Bot-Devoloper-Badge/issues)

**MIT License** - Kostenlos für alle! 🎉

</div>

### 🆘 Support erhalten

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/L0ine/Discord-Bot-Devoloper-Badge/issues)
- 💬 **Fragen**: [GitHub Discussions](https://github.com/L0ine/Discord-Bot-Devoloper-Badge/discussions)
- 💌 **Discord**: [Support Server](https://discord.gg/UP3PRuHZBe) 

---

<div align="center">

### 🎖️ **Vergiss nie wieder deinen Developer Badge!** 🎖️

**[⭐ Star das Projekt](https://github.com/L0ine/Discord-Bot-Devoloper-Badge) • [🔄 Fork für eigene Anpassungen](https://github.com/L0ine/Discord-Bot-Devoloper-Badge/fork) • [📢 Teile mit Freunden](https://twitter.com/intent/tweet?text=Nie%20wieder%20Discord%20Developer%20Badge%20verlieren!%20🎖️&url=https://github.com/L0ine/Discord-Bot-Devoloper-Badge)**

![Star History](https://api.star-history.com/svg?repos=L0ine/Discord-Bot-Devoloper-Badge&type=Date)

*Made with ❤️ for the Discord Developer Community*

</div>
