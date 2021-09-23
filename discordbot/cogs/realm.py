import json
import os
import sys
from discord.ext import commands
from discord.utils import get

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


class realm(commands.Cog, name="r"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="r")
    @commands.guild_only()
    @commands.has_role('Unassigned')
    async def r(self, context, *, realm):
        """
        Join a realm
        """
        memberRole = get(context.guild.roles, name=f'R{realm}')
        removeRole = get(context.guild.roles, name='Unassigned')
        await context.author.add_roles(memberRole)
        await context.author.remove_roles(removeRole)
        await context.message.delete()

def setup(bot):
    bot.add_cog(realm(bot))