import os
import sys
import json

import aiohttp
import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import commands
from disnake.ext.commands import Context

try:
    with open("config.json", "r") as c:
        config = json.load(c)
except FileNotFoundError:
    print ("config.json is missing, please run the main fle.")

class General(commands.Cog, name="General"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(
        name="ping",
        description="Check if the bot is alive.",
        )
    async def ping(self, context: Context):
        embed = disnake.Embed(
            title="🏓 Pong! Successfully Responded!",
            description=f"The bot latency is {round(self.bot.latency * 1000)}ms.",
            colour=config["Embed_Colour"]
        )
        await context.send(embed=embed)

def setup(bot):
    bot.add_cog(General(bot))