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

#
# command
#


# command class
class say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # print load message (not required)
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Loaded, say")

    # command 
    @commands.command()
    @has_permissions(manager_messages=True)
    async def say(self, ctx, qyc=None):

        if qyc == "None":
            await ctx.send("Please denife text")
        else: 
            await ctx.send(qyc)

        await ctx.message.delete()  # delete author message


# command setup
def setup(bot):
    bot.add_cog(say(bot))
