import json
import os
import sys
import aiohttp
import discord
import math
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
from prettytable import PrettyTable

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

class map(commands.Cog, name="map"):
    def __init__(self, bot):
        self.bot = bot
        self.api_token = config['api_token']
        self.headers = {'Authorization': f"Token {self.api_token}"}
        self.base_url = config['base_url']
        self.url = f"{self.base_url}/world/"
        self.buttons = ["◀️", "▶️"]

    @commands.command(name="find_player")
    @commands.guild_only()
    async def find_player(self, context, username: str):
        """
        Find player & nodes that the player is currently on
        """
        async with aiohttp.ClientSession() as session:
            page = 1
            raw_response = await session.get(f"{self.url}?name={username}", headers=self.headers)
            response = await raw_response.text()
            response = json.loads(response)
            if response.get('detail'):
                await context.send("Token Expired")
            else:
                map = response['results']
                count = math.ceil(response['count'] / 20)
                if not map:
                    await context.send("No results.")
                else:
                    t = PrettyTable()
                    t.left_padding_width = 0
                    t.right_padding_width = 0
                    t.align = "l"
                    t.field_names = ['Name', 'Clan', 'Owner', 'X', 'Y' , 'Realm']
                    t.align = "l"
                    for player in map:
                        name = player['name']
                        owner_group_name = player['owner_group_name']
                        owner_username = player['owner_username']
                        x = player['x']
                        y = player['y']
                        world_id = player['world_id']
                        t.add_row([name, owner_group_name, owner_username, x, y, world_id])
                    message = await context.send(f'```{t.get_string(sortby="Name")} \n Page {page} of {count}```')
                    for b in self.buttons:
                        await message.add_reaction(b)

                    while True:
                        try:
                            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=lambda r, u: r.message.id == message.id and u.id == context.author.id)
                            em = str(reaction.emoji)
                        except asyncio.TimeoutError:
                            return
                        
                        if user!=self.bot.user:
                            await message.remove_reaction(emoji=em, member=user)

                        if em == '▶️':
                            page = page+1
                            raw_response = await session.get(f"{self.url}?name={username}&page={page}", headers=self.headers)
                            response = await raw_response.text()
                            response = json.loads(response)
                            try:
                                map = response['results']
                                count = math.ceil(response['count'] / 20)
                                t = PrettyTable()
                                t.left_padding_width = 0
                                t.right_padding_width = 0
                                t.align = "l"
                                t.field_names = ['Name', 'Clan', 'Owner', 'X', 'Y' , 'Realm']
                                t.align = "l"
                                for player in map:
                                    name = player['name']
                                    owner_username = player['owner_username']
                                    owner_group_name = player['owner_group_name']
                                    x = player['x']
                                    y = player['y']
                                    world_id = player['world_id']
                                    t.add_row([name, owner_username, owner_group_name, x, y,world_id])
                            except KeyError:
                                pass
                            await message.edit(content=f'```{t.get_string(sortby="Name")} \n Page {page} of {count}```')

                        if em == '◀️':
                            page = page-1
                            raw_response = await session.get(f"{self.url}?search={username}&page={page}", headers=self.headers)
                            response = await raw_response.text()
                            response = json.loads(response)
                            try:
                                map = response['results']
                                count = math.ceil(response['count'] / 20)
                                t = PrettyTable()
                                t.left_padding_width = 0
                                t.right_padding_width = 0
                                t.align = "l"
                                t.field_names = ['Name', 'Clan', 'Owner', 'X', 'Y' , 'Realm']
                                t.align = "l"
                                for player in map:
                                    name = player['name']
                                    owner_username = player['owner_username']
                                    owner_group_name = player['owner_group_name']
                                    x = player['x']
                                    y = player['y']
                                    world_id = player['world_id']
                                    t.add_row([name, owner_username, owner_group_name, x, y,world_id])
                            except KeyError:
                                pass
                            await message.edit(content=f'```{t.get_string(sortby="Name")} \n Page {page} of {count}```')


    @commands.command(name="find_clan")
    @commands.guild_only()
    async def find_clan(self, context, clan: str):
        """
        Find clan & nodes that they are on
        """
        async with aiohttp.ClientSession() as session:
            page = 1
            raw_response = await session.get(f"{self.url}?owner_group_name={clan}", headers=self.headers)
            response = await raw_response.text()
            response = json.loads(response)
            if response.get('detail'):
                await context.send("Token Expired")
            else:
                map = response['results']
                count = math.ceil(response['count'] / 20)
                if not map:
                    await context.send("No results.")
                else:
                    t = PrettyTable()
                    t.left_padding_width = 0
                    t.right_padding_width = 0
                    t.align = "l"
                    t.field_names = ['Name', 'Clan', 'Owner', 'X', 'Y' , 'Realm']
                    t.align = "l"
                    for player in map:
                        name = player['name']
                        owner_group_name = player['owner_group_name']
                        owner_username = player['owner_username']
                        x = player['x']
                        y = player['y']
                        world_id = player['world_id']
                        t.add_row([name, owner_group_name, owner_username, x, y, world_id])
                    message = await context.send(f'```{t.get_string(sortby="Name")} \n Page {page} of {count}```')
                    for b in self.buttons:
                        await message.add_reaction(b)

                    while True:
                        try:
                            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=lambda r, u: r.message.id == message.id and u.id == context.author.id)
                            em = str(reaction.emoji)
                        except asyncio.TimeoutError:
                            await message.delete()
                            await context.message.delete()
                            return
                        
                        if user!=self.bot.user:
                            await message.remove_reaction(emoji=em, member=user)

                        if em == '▶️':
                            page = page+1
                            raw_response = await session.get(f"{self.url}?owner_group_name={clan}&page={page}", headers=self.headers)
                            response = await raw_response.text()
                            response = json.loads(response)
                            try:
                                map = response['results']
                                count = math.ceil(response['count'] / 20)
                                t = PrettyTable()
                                t.left_padding_width = 0
                                t.right_padding_width = 0
                                t.align = "l"
                                t.field_names = ['Name', 'Clan', 'Owner', 'X', 'Y' , 'Realm']
                                t.align = "l"
                                for player in map:
                                    name = player['name']
                                    owner_username = player['owner_username']
                                    owner_group_name = player['owner_group_name']
                                    x = player['x']
                                    y = player['y']
                                    world_id = player['world_id']
                                    t.add_row([name, owner_username, owner_group_name, x, y,world_id])
                            except KeyError:
                                pass
                            await message.edit(content=f'```{t.get_string(sortby="Name")} \n Page {page} of {count}```')

                        if em == '◀️':
                            page = page-1
                            raw_response = await session.get(f"{self.url}?owner_group_name={clan}&page={page}", headers=self.headers)
                            response = await raw_response.text()
                            response = json.loads(response)
                            try:
                                map = response['results']
                                count = math.ceil(response['count'] / 20)
                                t = PrettyTable()
                                t.left_padding_width = 0
                                t.right_padding_width = 0
                                t.align = "l"
                                t.field_names = ['Name', 'Clan', 'Owner', 'X', 'Y' , 'Realm']
                                t.align = "l"
                                for player in map:
                                    name = player['name']
                                    owner_username = player['owner_username']
                                    owner_group_name = player['owner_group_name']
                                    x = player['x']
                                    y = player['y']
                                    world_id = player['world_id']
                                    t.add_row([name, owner_username, owner_group_name, x, y,world_id])
                            except KeyError:
                                pass
                            await message.edit(content=f'```{t.get_string(sortby="Name")} \n Page {page} of {count}```')

    @commands.command(name="find_item")
    @commands.guild_only()
    async def find_item(self, context, item: str, level: int, realm: int):
        """
        Find items on the map:\n !find_item [gold,food,ore,swamp,bl,gl,gem] level realm \nExample: !find_item gold 12 23
        """

        if item.lower() == "gold":
            name = "gold"
            newname = "Level " + str(level) + " " + name.capitalize()
        elif item.lower() == "food":
            name = "food"
            newname = "Level " + str(level) + " " + name.capitalize()		   
        elif item.lower() == "ore":
            name = "ore"
            newname = "Level " + str(level) + " " + name.capitalize()		   
        elif item.lower() == "swamp":
            newname = "Swamp Titan [Lv" + str(level) + "]"
        elif item.lower() == "bl":
            newname = "Badlands Titan [Lv" + str(level) + "]"
        elif item.lower() == "gl":
            newname = "Grasslands Titan [Lv" + str(level) + "]"
        elif item.lower() == "gem":
            newname = "lv " + str(level) + " titan trove"
        else:
            await context.send(":no_entry_sign: Error: please use the following format:\n`!find_item [gold,food,ore,swamp,bl,gl,gem] level realm`\nExample: `!find_item gold 12 23`")

        async with aiohttp.ClientSession() as session:
            page=1
            raw_response = await session.get(f"{self.url}?name={newname}&world_id={realm}", headers=self.headers)
            response = await raw_response.text()
            response = json.loads(response)
            if response.get('detail'):
                await context.send("Token Expired")
            else:
                map = response['results']
                count = math.ceil(response['count'] / 20)
                if not map:
                    await context.send("No results.")
                else:
                    t = PrettyTable()
                    t.left_padding_width = 0
                    t.right_padding_width = 0
                    t.align = "l"
                    t.field_names = ['Name', 'Clan', 'Owner', 'X', 'Y' , 'Realm']
                    t.align = "l"
                    for player in map:
                        name = player['name']
                        owner_group_name = player['owner_group_name']
                        owner_username = player['owner_username']
                        x = player['x']
                        y = player['y']
                        world_id = player['world_id']
                        t.add_row([name, owner_group_name, owner_username, x, y, world_id])
                    message = await context.send(f'```{t.get_string(sortby="Name")} \n Page {page} of {count}```')
                    for b in self.buttons:
                        await message.add_reaction(b)

                    while True:
                        try:
                            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=lambda r, u: r.message.id == message.id and u.id == context.author.id)
                            em = str(reaction.emoji)
                        except asyncio.TimeoutError:
                            await message.delete()
                            await context.message.delete()
                            return
                        
                        if user!=self.bot.user:
                            await message.remove_reaction(emoji=em, member=user)

                        if em == '▶️':
                            page = page+1
                            raw_response = await session.get(f"{self.url}?name={newname}&world_id={realm}&page={page}", headers=self.headers)
                            response = await raw_response.text()
                            response = json.loads(response)
                            try:
                                map = response['results']
                                count = math.ceil(response['count'] / 20)
                                t = PrettyTable()
                                t.left_padding_width = 0
                                t.right_padding_width = 0
                                t.align = "l"
                                t.field_names = ['Name', 'Clan', 'Owner', 'X', 'Y' , 'Realm']
                                t.align = "l"
                                for player in map:
                                    name = player['name']
                                    owner_username = player['owner_username']
                                    owner_group_name = player['owner_group_name']
                                    x = player['x']
                                    y = player['y']
                                    world_id = player['world_id']
                                    t.add_row([name, owner_username, owner_group_name, x, y,world_id])
                            except KeyError:
                                pass
                            await message.edit(content=f'```{t.get_string(sortby="Name")} \n Page {page} of {count}```')

                        if em == '◀️':
                            page = page-1
                            raw_response = await session.get(f"{self.url}?name={newname}&world_id={realm}&page={page}", headers=self.headers)
                            response = await raw_response.text()
                            response = json.loads(response)
                            try:
                                map = response['results']
                                count = math.ceil(response['count'] / 20)
                                t = PrettyTable()
                                t.left_padding_width = 0
                                t.right_padding_width = 0
                                t.align = "l"
                                t.field_names = ['Name', 'Clan', 'Owner', 'X', 'Y' , 'Realm']
                                t.align = "l"
                                for player in map:
                                    name = player['name']
                                    owner_username = player['owner_username']
                                    owner_group_name = player['owner_group_name']
                                    x = player['x']
                                    y = player['y']
                                    world_id = player['world_id']
                                    t.add_row([name, owner_username, owner_group_name, x, y,world_id])
                            except KeyError:
                                pass
                            await message.edit(content=f'```{t.get_string(sortby="Name")} \n Page {page} of {count}```')

def setup(bot):
    bot.add_cog(map(bot))