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
class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # print load message (not required)
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Loaded, help")

    # command 
    @commands.command()
    async def help(self, ctx):

        embed = nextcord.Embed(title="Help",
                               description="Bot commands!",
                               color=color)

        embed.add_filed(name="Help",
         value=";help | see bot commands!")

        embed.add_filed(name="Say",
        value=";say <text> | say text!")

        embed.add_filed(name="Command name",
        value=";command <?> | What command to do?")


        embed.set_footer(text=footer)

        await ctx.reply("Reply")  # reply message
        await ctx.send(embed=embed)  # send embed
        await ctx.message.delete()  # delete author message


# command setup
def setup(bot):
    bot.add_cog(help(bot))
