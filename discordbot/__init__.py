import json
import os
import random
import sys

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.utils import get
from django.conf import settings
import os

intents = discord.Intents.default()

bot = Bot(settings.DISCORD_BOT_PREFIX, intents=intents)


# bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print("-------------------")
    status_task.start()


# game status task of the bot
@tasks.loop(minutes=1.0)
async def status_task():
    statuses = ["Kingdoms of Heckfire", f"{settings.DISCORD_BOT_PREFIX}help"]
    await bot.change_presence(activity=discord.Game(random.choice(statuses)))


# Removes the default help command of discord.py
bot.remove_command("help")

if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")

# everytime someone joins
@bot.event 
async def on_member_join(member):
  role_id = 881981915341676566
  role = get(member.guild.roles, id=role_id)
  await member.add_roles(role)


# every time someone sends a message, with or without the prefix
@bot.event
async def on_message(message):
    # Ignores if a command is being executed by a bot or by the bot itself
    if message.author == bot.user or message.author.bot:
        return
    # Ignores if a command is being executed by a non whitelisted user
    with open("whitelist.json") as file:
        whitelist = json.load(file)
    if not message.author.id in whitelist["ids"]:
        return
    await bot.process_commands(message)


# every time a command has been *successfully* executed
@bot.event
async def on_command_completion(ctx):
    fullCommandName = ctx.command.qualified_name
    split = fullCommandName.split(" ")
    executedCommand = str(split[0])
    print(
        f"Executed {executedCommand} command in {ctx.guild.name} (ID: {ctx.message.guild.id}) by {ctx.message.author} (ID: {ctx.message.author.id})")


# every time a valid commands catches an error
@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandOnCooldown):
        minutes, seconds = divmod(error.retry_after, 60)
        hours, minutes = divmod(minutes, 60)
        hours = hours % 24
        embed = discord.Embed(
            title="Hey, please slow down!",
            description=f"You can use this command again in {f'{round(hours)} hours' if round(hours) > 0 else ''} {f'{round(minutes)} minutes' if round(minutes) > 0 else ''} {f'{round(seconds)} seconds' if round(seconds) > 0 else ''}.",
            color=0xE02B2B
        )
        await context.send(embed=embed)
        print(f"Cooldown {context.message.author} (ID: {context.message.author.id})")
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Error!",
            description="You are missing the permission `" + ", ".join(
                error.missing_perms) + "` to execute this command!",
            color=0xE02B2B
        )
        await context.send(embed=embed)
        print(f"Missing Permission {context.message.author} (ID: {context.message.author.id})")
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Error!",
            description=str(error).capitalize(),
            # We need to capitalize because the command arguments have no capital letter in the code.
            color=0xE02B2B
        )
        await context.send(embed=embed)
        print(f"Missing Required Argument {context.message.author} (ID: {context.message.author.id})")
    elif isinstance(error, commands.NoPrivateMessage):
        embed = discord.Embed(
            title="Error!",
            description="You cannot execute this command in a private message!",
            color=0xE02B2B
        )
        await context.send(embed=embed)
        print(f"Private Message Attempted by {context.message.author} (ID: {context.message.author.id})")
    elif isinstance(error, commands.MaxConcurrencyReached):
        embed = discord.Embed(
            title="Error!",
            description="There is a queue, try again in a few seconds!",
            color=0xE02B2B
        )
        await context.send(embed=embed)
        print(f"Stuck in queue {context.message.author} (ID: {context.message.author.id})")


# Run the bot with the token
bot.run(settings.DISCORD_TOKEN)
