# Imports
import nextcord, os
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions, MissingPermissions, CommandNotFound

# Config #
# Embed
footer = "Embed footer | qycelo#2202"
color = 0x03fc41 # green
wcolor = 0xfc0303 # red
# Command admin
admin = ["920008899216683068", "Discord_id"]

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
        name="qycelo#2202"))

    print(f"{qyc.user} is online!")

# Commands here #
@qyc.command()
async def test(ctx):
  await ctx.reply("Test ;D")

# Error messages
@qyc.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Command not found, do ;help to see all commands!")
    elif isinstance(error, MissingPermissions):
        await ctx.send("You don't have permissions to execute this command!")
    return

qyc.run(TOKEN)
