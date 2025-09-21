# <img width="40" height="40" alt="discord-logo" src="https://github.com/user-attachments/assets/adabd300-70df-4847-9b34-e51d207d254d" /> <img width="40" height="40" alt="grafik" src="https://github.com/user-attachments/assets/478efc93-83c4-46bc-acb7-94e81883d652" /> discord dev badge bot


<div align="left">

![Discord Developer Badge](https://img.shields.io/badge/Discord-Developer%20Badge-5865F2?style=for-the-badge&logo=discord&logoColor=white)
[![Docker Build](https://img.shields.io/github/actions/workflow/status/L0ine/Discord-Bot-Devoloper-Badge/docker-publish.yml?style=for-the-badge&logo=docker)](https://github.com/L0ine/Discord-Bot-Devoloper-Badge/actions/workflows/docker-publish.yml)
</div>

---

### what's this about?
**literally just want that shiny dev badge? I got you =)**

This is a Tutorial for Discord's **active developer badge**


## ⚡ speedrun setup (literally 2 minutes)

### step 1: make a discord bot
1. hit up [discord dev portal](https://discord.com/developers/applications)
2. smash **"new application"**
3. name it whatever
4. grab your **application id** 
5. go to **"bot"** → reset token → copy that token

### step 2: permissions (don't skip!)
- bot settings → **privileged gateway intents** (check em all tbh)
- **oauth2** → **url generator** → scopes: `bot` + permissions: `administrator`

### step 3: invite your Bot
```
https://discord.com/api/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=2048&scope=bot%20applications.commands
```
*replace YOUR_CLIENT_ID with your actual application id (obviously)*

---

## 🐳 choose your setup method

<details>
<summary><h3>🚀 OPTION 1: Docker One-Liner (recommended for beginners)</h3></summary>

**step 1: run the container**
```bash
docker run -d \
  --name discord-dev-badge-bot \
  --restart unless-stopped \
  -e DISCORD_BOT_TOKEN="your_token_here" \
  -e CLIENT_ID="your_client_id_here" \
  ghcr.io/l0ine/discord-bot-devoloper-badge:latest
```

**step 2: check if it's running**
```bash
docker logs discord-dev-badge-bot
```
you should see "bot is ready" or similar

**step 3: test in discord**
- wait 5-10 minutes for slash commands to register
- go to your discord server where you invited the bot
- type `/ping` and hit enter
- bot should respond with pong + some info

**what happens next:**
- bot will dm you every 25 days reminding you to ping
- just run `/ping` when reminded to keep your dev status active
- after 24h of first ping: go get your badge from dev portal

</details>

<details>
<summary><h3>🛠️ OPTION 2: Docker Compose (for the organized)</h3></summary>

**step 1: download the project**
```bash
git clone https://github.com/L0ine/Discord-Bot-Devoloper-Badge.git
cd Discord-Bot-Devoloper-Badge
```

**step 2: configure your settings**
```bash
cp .env.example .env
nano .env  # or use any text editor
```
fill in your bot token and client id in the .env file

**step 3: start the bot**
```bash
docker-compose up -d
```

**step 4: monitor logs**
```bash
docker-compose logs -f
```

**step 5: test in discord**
- wait 5-10 minutes for slash commands to register
- go to your discord server 
- type `/ping` - bot should respond
- you're all set! bot will remind you every 25 days

**what happens next:**
- bot runs in background automatically
- sends dm reminders so you never lose the badge
- just `/ping` when reminded, that's literally it

</details>

<details>
<summary><h3>💻 OPTION 3: Local Development (touch grass edition)</h3></summary>

**step 1: get the code**
```bash
git clone https://github.com/L0ine/Discord-Bot-Devoloper-Badge.git
cd Discord-Bot-Devoloper-Badge
```

**step 2: setup python environment**
```bash
python -m venv .venv
source .venv/bin/activate  # linux/mac
# .venv\Scripts\activate  # windows users
```

**step 3: install dependencies**
```bash
pip install -r requirements.txt
```

**step 4: configure bot**
```bash
cp .env.example .env
# edit .env with your discord bot token and client id
```

**step 5: run the bot**
```bash
python discord-dev-badge-bot.py
```
keep this terminal window open - bot stops when you close it

**step 6: test in discord**
- wait 10 minutes for commands to sync
- go to your server and type `/ping`
- bot should respond with pong

**what happens next:**
- bot only runs when your computer is on
- you'll get dm reminders every 25 days
- just `/ping` to stay active, ez clap

</details>

---

## ⚙️ config stuff

### environment variables (required or we riot)
| variable | required? | what it does |
|----------|-----------|-------------|
| `DISCORD_BOT_TOKEN` | ✅ yes | your bot's secret sauce |
| `CLIENT_ID` | ✅ yes | for slash commands to work | 
| `GUILD_ID` | ❌ nah | server id (optional) | 
| `YOUR_USER_ID` | ❌ nah | for dm reminders | 

---

### claim your badge 🎖️
1. 24 hours after the first /ping you go back to [discord dev portal](https://discord.com/developers/applications)
2. **select your app** → click **"active developer"** tab
3. **click "get badge"** button
4. **badge appears** in your profile (may take a few minutes)

### phase 4: maintenance (automated) 🤖
- **bot sends dm reminders** every 25 days
- **just run `/ping`** when reminded
- **never lose your badge** again (unless you ignore reminders)

---

<div align="center">

**[⭐ star if this badge is now on your Profile](https://github.com/L0ine/Discord-Bot-Devoloper-Badge) • [🔄 fork for modifications](https://github.com/L0ine/Discord-Bot-Devoloper-Badge/fork)**

*made with ❤️ and too much energy*

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://choosealicense.com/licenses/mit/)

</div>
