import json
import os
import sys

import discord
from discord.ext import commands

from helpers import json_manager

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


class owner(commands.Cog, name="owner"):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="whitelist")
    async def whitelist(self, context):
        """
        Lets you add or remove a user from being able to use the bot.
        """
        if context.invoked_subcommand is None:
            with open("whitelist.json") as file:
                whitelist = json.load(file)
            embed = discord.Embed(
                title=f"There are currently {len(whitelist['ids'])} whitelisted IDs",
                description=f"{', '.join(str(id) for id in whitelist['ids'])}",
                color=0x0000FF
            )
            await context.send(embed=embed)

    @whitelist.command(name="add")
    async def whitelist_add(self, context, member: discord.Member = None):
        """
        Lets you add a user from not being able to use the bot.
        """
        if context.message.author.id in config["owners"]:
            userID = member.id
            try:
                with open("whitelist.json") as file:
                    whitelist = json.load(file)
                if (userID in whitelist['ids']):
                    embed = discord.Embed(
                        title="Error!",
                        description=f"**{member.name}** is already in the whitelist.",
                        color=0xE02B2B
                    )
                    await context.send(embed=embed)
                    return
                json_manager.add_user_to_whitelist(userID)
                embed = discord.Embed(
                    title="User Whitelistlisted",
                    description=f"**{member.name}** has been successfully added to the whitelist",
                    color=0x42F56C
                )
                with open("whitelist.json") as file:
                    whitelist = json.load(file)
                embed.set_footer(
                    text=f"There are now {len(whitelist['ids'])} users in the whitelist"
                )
                await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Error!",
                    description=f"An unknown error occurred when trying to add **{member.name}** to the whitelist.",
                    color=0xE02B2B
                )
                await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @whitelist.command(name="remove")
    async def whitelist_remove(self, context, member: discord.Member = None):
        """
        Lets you remove a user from being able to use the bot.
        """
        if context.message.author.id in config["owners"]:
            userID = member.id
            try:
                json_manager.remove_user_from_whitelist(userID)
                embed = discord.Embed(
                    title="User removed from whitelist",
                    description=f"**{member.name}** has been successfully removed from the whitelist",
                    color=0x42F56C
                )
                with open("whitelist.json") as file:
                    whitelist = json.load(file)
                embed.set_footer(
                    text=f"There are now {len(whitelist['ids'])} users in the whitelist"
                )
                await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Error!",
                    description=f"**{member.name}** is not in the whitelist.",
                    color=0xE02B2B
                )
                await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

def setup(bot):
    bot.add_cog(owner(bot))
