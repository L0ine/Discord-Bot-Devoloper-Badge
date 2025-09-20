#!/usr/bin/env python3


# Trigger für neuen Docker-Build




Discord Developer Badge Bot - Mit direkten DM-Erinnerungen
Erinnert dich jeden Monat per Direktnachricht
"""

import discord
from discord.ext import commands, tasks
import os
import time
from datetime import datetime
import logging

import os

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")
GUID_ID = os.getenv("GUID_ID")
YOUR_USER_ID = os.getenv("YOUR_USER_ID")

if not all([DISCORD_BOT_TOKEN, CLIENT_ID, GUID_ID, YOUR_USER_ID]):
    raise Exception("Bitte setze die Umgebungsvariablen: DISCORD_BOT_TOKEN, CLIENT_ID, GUID_ID, YOUR_USER_ID")




# .env Datei laden (falls vorhanden)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Logging Setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Bot Configuration
TOKEN = os.getenv('DISCORD_BOT_TOKEN') or os.getenv('TOKEN')
CLIENT_ID = os.getenv('CLIENT_ID') or os.getenv('APP_ID')
GUILD_ID = os.getenv('GUILD_ID')

# Deine User ID für DM-Erinnerungen
YOUR_USER_ID = os.getenv('YOUR_USER_ID')  # Optional - wird automatisch erkannt

# Bot Setup
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)
start_time = time.time()
bot_owner_id = None  # Wird beim ersten /ping gesetzt

@bot.event
async def on_ready():
    """Bot ist bereit"""
    logger.info(f'Bot ist bereit! Eingeloggt als {bot.user}')
    logger.info(f'Verbunden mit {len(bot.guilds)} Server(n)')
    
    # Bot Status setzen
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, 
        name="!ping | /ping"
    ))
    
    # Slash Commands registrieren
    try:
        if CLIENT_ID:
            if GUILD_ID:
                guild = discord.Object(id=int(GUILD_ID))
                bot.tree.copy_global_to(guild=guild)
                await bot.tree.sync(guild=guild)
                logger.info("Slash Commands registriert (guild-scoped)")
            else:
                await bot.tree.sync()
                logger.info("Slash Commands registriert (global)")
        else:
            logger.warning("CLIENT_ID nicht gesetzt - Slash Commands übersprungen")
    except Exception as e:
        logger.error(f"Fehler beim Registrieren der Slash Commands: {e}")
    
    # Monatliche Erinnerung starten
    if not monthly_reminder.is_running():
        monthly_reminder.start()
        logger.info("Monatliche DM-Erinnerungen aktiviert")

async def send_dm_reminder():
    """Sendet DM-Erinnerung an den Bot-Owner"""
    global bot_owner_id
    
    # User ID verwenden (entweder aus ENV oder die gespeicherte)
    user_id = YOUR_USER_ID or bot_owner_id
    
    if not user_id:
        logger.warning("Keine User ID für Erinnerungen verfügbar")
        return
    
    try:
        user = await bot.fetch_user(int(user_id))
        if user:
            embed = discord.Embed(
                title="🎖️ Discord Developer Badge Erinnerung",
                description="Zeit für deinen monatlichen `/ping` um den Active Developer Badge zu behalten!",
                color=0x00ff00,
                timestamp=datetime.utcnow()
            )
            
            embed.add_field(
                name="Was du tun musst:",
                value="Gehe zu einem Server mit dem Bot und nutze `/ping` oder `!ping`",
                inline=False
            )
            
            embed.add_field(
                name="Warum?",
                value="Discord braucht monatliche Aktivität um den Developer Badge zu behalten",
                inline=False
            )
            
            await user.send(embed=embed)
            logger.info(f"Monatliche Badge-Erinnerung gesendet an {user.name}")
        else:
            logger.error("User nicht gefunden für DM-Erinnerung")
    except discord.Forbidden:
        logger.error("Kann keine DM senden - User hat DMs deaktiviert")
    except Exception as e:
        logger.error(f"DM-Erinnerung fehlgeschlagen: {e}")

@tasks.loop(hours=24*25)  # Alle 25 Tage
async def monthly_reminder():
    """Sendet monatliche DM-Erinnerung"""
    await send_dm_reminder()

def format_uptime(seconds):
    """Formatiert Uptime in lesbarem Format"""
    days, remainder = divmod(int(seconds), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    parts = []
    if days: parts.append(f"{days}d")
    if hours: parts.append(f"{hours}h")
    if minutes: parts.append(f"{minutes}m")
    if seconds: parts.append(f"{seconds}s")
    
    return " ".join(parts) or "0s"

def get_latency_status(latency_ms):
    """Gibt Status basierend auf Latenz zurück"""
    if latency_ms < 100:
        return "🟢 Ausgezeichnet"
    elif latency_ms < 200:
        return "🟡 Gut"
    elif latency_ms < 500:
        return "🟠 Okay"
    else:
        return "🔴 Schlecht"

# Prefix Commands
@bot.command(name='ping')
async def ping_command(ctx):
    """Ping Command - wichtig für Developer Badge!"""
    global bot_owner_id
    
    # User ID beim ersten Ping speichern (falls nicht in ENV gesetzt)
    if not bot_owner_id and not YOUR_USER_ID:
        bot_owner_id = str(ctx.author.id)
        logger.info(f"Bot-Owner ID gesetzt: {bot_owner_id}")
    
    logger.info(f"Prefix-Ping ausgelöst von: {ctx.author}")
    
    message = await ctx.send("🏓 Pinging...")
    api_latency = round(bot.latency * 1000)
    
    embed = discord.Embed(
        title="🏓 Pong!",
        color=0x00ff00,
        timestamp=datetime.utcnow()
    )
    
    embed.add_field(name="📡 API Latenz", value=f"{api_latency}ms", inline=True)
    embed.add_field(name="📊 Status", value=get_latency_status(api_latency), inline=True)
    embed.add_field(name="🎖️ Badge", value="Aktivität registriert!", inline=True)
    
    await message.edit(content="", embed=embed)

@bot.command(name='uptime')
async def uptime_command(ctx):
    """Zeigt Bot Uptime"""
    uptime_seconds = time.time() - start_time
    
    embed = discord.Embed(
        title="⏰ Bot Uptime",
        description=f"🔄 **Aktuelle Uptime:** {format_uptime(uptime_seconds)}",
        color=0x0099ff,
        timestamp=datetime.utcnow()
    )
    
    embed.add_field(name="🚀 Gestartet", value=f"<t:{int(start_time)}:F>", inline=True)
    embed.add_field(name="📊 Status", value="🟢 Online", inline=True)
    
    await ctx.send(embed=embed)

@bot.command(name='status')
async def status_command(ctx):
    """Zeigt Bot Status"""
    embed = discord.Embed(
        title="📊 Bot Status",
        color=0x9932cc,
        timestamp=datetime.utcnow()
    )
    
    embed.add_field(name="🔗 Verbindung", value="🟢 Verbunden", inline=True)
    embed.add_field(name="📡 API Latenz", value=f"{round(bot.latency * 1000)}ms", inline=True)
    embed.add_field(name="🏠 Server", value=f"{len(bot.guilds)}", inline=True)
    embed.add_field(name="⏰ Uptime", value=format_uptime(time.time() - start_time), inline=True)
    
    # Zeige ob Erinnerungen aktiv sind
    reminder_status = "✅ Aktiv" if monthly_reminder.is_running() else "❌ Inaktiv"
    embed.add_field(name="🔔 Erinnerungen", value=reminder_status, inline=True)
    
    await ctx.send(embed=embed)

@bot.command(name='hilfe')
async def help_command(ctx):
    """Zeigt alle verfügbaren Commands"""
    embed = discord.Embed(
        title="❓ Commands",
        description="**Prefix:** `!` | **Slash:** `/`",
        color=0xffa500,
        timestamp=datetime.utcnow()
    )
    
    embed.add_field(name="🏓 ping", value="`!ping` / `/ping`", inline=True)
    embed.add_field(name="⏰ uptime", value="`!uptime` / `/uptime`", inline=True)
    embed.add_field(name="📊 status", value="`!status` / `/status`", inline=True)
    embed.add_field(name="❓ hilfe", value="`!hilfe` / `/help`", inline=True)
    embed.add_field(name="🧪 test", value="`!test` (Test-Erinnerung)", inline=True)
    
    embed.add_field(
        name="🎖️ Developer Badge", 
        value="Nutze `/ping` mindestens einmal pro Monat!\nIch erinnere dich automatisch per DM.", 
        inline=False
    )
    
    await ctx.send(embed=embed)

@bot.command(name='test')
async def test_reminder(ctx):
    """Sendet Test-Erinnerung sofort"""
    global bot_owner_id
    
    if not bot_owner_id and not YOUR_USER_ID:
        bot_owner_id = str(ctx.author.id)
    
    await ctx.send("📤 Sende Test-Erinnerung...")
    await send_dm_reminder()
    await ctx.send("✅ Test-Erinnerung gesendet (check deine DMs)!")

# Slash Commands
@bot.tree.command(name='ping', description='Antwortet mit pong - wichtig für Developer Badge!')
async def ping_slash(interaction: discord.Interaction):
    """Slash Ping Command"""
    global bot_owner_id
    
    if not bot_owner_id and not YOUR_USER_ID:
        bot_owner_id = str(interaction.user.id)
        logger.info(f"Bot-Owner ID gesetzt: {bot_owner_id}")
    
    logger.info(f"Slash-Ping ausgelöst von: {interaction.user}")
    
    await interaction.response.send_message("🏓 Pinging...")
    
    api_latency = round(bot.latency * 1000)
    embed = discord.Embed(
        title="🏓 Pong!",
        color=0x00ff00,
        timestamp=datetime.utcnow()
    )
    
    embed.add_field(name="📡 API Latenz", value=f"{api_latency}ms", inline=True)
    embed.add_field(name="📊 Status", value=get_latency_status(api_latency), inline=True)
    embed.add_field(name="🎖️ Badge", value="Aktivität registriert!", inline=True)
    
    await interaction.edit_original_response(content="", embed=embed)

@bot.tree.command(name='uptime', description='Zeigt Bot-Uptime')
async def uptime_slash(interaction: discord.Interaction):
    """Slash Uptime Command"""
    uptime_seconds = time.time() - start_time
    
    embed = discord.Embed(
        title="⏰ Bot Uptime",
        description=f"🔄 **Aktuelle Uptime:** {format_uptime(uptime_seconds)}",
        color=0x0099ff,
        timestamp=datetime.utcnow()
    )
    
    embed.add_field(name="🚀 Gestartet", value=f"<t:{int(start_time)}:F>", inline=True)
    embed.add_field(name="📊 Status", value="🟢 Online", inline=True)
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name='status', description='Zeigt Bot-Status')
async def status_slash(interaction: discord.Interaction):
    """Slash Status Command"""
    embed = discord.Embed(
        title="📊 Bot Status",
        color=0x9932cc,
        timestamp=datetime.utcnow()
    )
    
    embed.add_field(name="🔗 Verbindung", value="🟢 Verbunden", inline=True)
    embed.add_field(name="📡 API Latenz", value=f"{round(bot.latency * 1000)}ms", inline=True)
    embed.add_field(name="🏠 Server", value=f"{len(bot.guilds)}", inline=True)
    embed.add_field(name="⏰ Uptime", value=format_uptime(time.time() - start_time), inline=True)
    
    reminder_status = "✅ Aktiv" if monthly_reminder.is_running() else "❌ Inaktiv"
    embed.add_field(name="🔔 Erinnerungen", value=reminder_status, inline=True)
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name='help', description='Zeigt alle verfügbaren Commands')
async def help_slash(interaction: discord.Interaction):
    """Slash Help Command"""
    embed = discord.Embed(
        title="❓ Commands",
        description="**Prefix:** `!` | **Slash:** `/`",
        color=0xffa500,
        timestamp=datetime.utcnow()
    )
    
    embed.add_field(name="🏓 ping", value="`!ping` / `/ping`", inline=True)
    embed.add_field(name="⏰ uptime", value="`!uptime` / `/uptime`", inline=True)
    embed.add_field(name="📊 status", value="`!status` / `/status`", inline=True)
    embed.add_field(name="❓ hilfe", value="`!hilfe` / `/help`", inline=True)
    
    embed.add_field(
        name="🎖️ Developer Badge", 
        value="Nutze `/ping` mindestens einmal pro Monat!\nIch erinnere dich automatisch per DM.", 
        inline=False
    )
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name='test', description='Sendet Test-Erinnerung per DM')
async def test_slash(interaction: discord.Interaction):
    """Test-Erinnerung senden"""
    global bot_owner_id
    
    if not bot_owner_id and not YOUR_USER_ID:
        bot_owner_id = str(interaction.user.id)
    
    await interaction.response.send_message("📤 Sende Test-Erinnerung...", ephemeral=True)
    await send_dm_reminder()
    await interaction.edit_original_response(content="✅ Test-Erinnerung gesendet (check deine DMs)!")

# Error Handling
@bot.event
async def on_command_error(ctx, error):
    """Behandelt Command-Fehler"""
    logger.error(f"Command-Fehler: {error}")

def main():
    """Hauptfunktion"""
    if not TOKEN:
        logger.error("DISCORD_BOT_TOKEN nicht gefunden!")
        logger.error("Erstelle eine .env Datei oder setze Umgebungsvariablen")
        return
    
    try:
        logger.info("Discord Bot wird gestartet...")
        bot.run(TOKEN, log_handler=None)  # Verwende unser eigenes Logging
    except discord.LoginFailure:
        logger.error("Bot Login fehlgeschlagen! Token überprüfen.")
    except Exception as e:
        logger.error(f"Bot Startfehler: {e}")

if __name__ == "__main__":
    main()