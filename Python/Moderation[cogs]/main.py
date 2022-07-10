# Imports
# Neekeri
import nextcord
from nextcord.ext import commands

# Config #
# Embed
footer = "Embed footer | qycelo#2202"
color = 0x03fc41 # green
wcolor = 0xfc0303 # red
# Command admin
admin = ["Discord_id", "Discord_id"]

# Token
# Discord developer portal
TOKEN = ""

# Intents, prefix, remove help
# Discord devreloper portal trun on intents
intents = nextcord.Intents.default()
qyc = commands.Bot(command_prefix=";", intents=nextcord.Intents.all())
qyc.remove_command("help")

# On ready, status
# Playing, listening, streaming
@qyc.event
async def on_ready():
    await qyc.change_presence(status=nextcord.Status.online,
    activity=nextcord.Activity(
        type=nextcord.ActivityType.listening,
        name="qycelo#2202 "))

    print(f"{qyc.user} is online!")

qyc.run(TOKEN)
