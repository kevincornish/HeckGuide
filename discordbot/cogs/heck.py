import json
import os
import sys
import aiohttp
import asyncio
import math
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from prettytable import PrettyTable

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


class allies(commands.Cog, name="allies"):
    def __init__(self, bot):
        self.bot = bot
        self.api_token = config['api_token']
        self.headers = {'Authorization': f"Token {self.api_token}"}
        self.base_url = config['base_url']
        self.url = f"{self.base_url}/allies/"

    @commands.command(name="allies")
    @commands.guild_only()
    async def allies(self, context, *, allyname):
        """
        Return a list of allies from given username.
        """
        buttons = ["◀️", "▶️"]
        async with aiohttp.ClientSession() as session:
            page = 1
            raw_response = await session.get(f"{self.url}?search={allyname}&page={page}", headers=self.headers)
            response = await raw_response.text()
            response = json.loads(response)
            if response.get('detail'):
                await context.send("Token Expired")
            else:
                allies = response['results']
                count = math.ceil(response['count'] / 20)
                if not allies:
                    await context.send("No results.")
                else:
                    t = PrettyTable()
                    t.left_padding_width = 0
                    t.right_padding_width = 0
                    t.align = "l"
                    t.field_names = ['Username', 'Clan', 'Cost', 'Grass' , 'Badlands','Swamp', 'Total']
                    t.align = "l"
                    for ally in allies:
                        username = ally['username']
                        group_tag = ally['group_tag']
                        cost = ally['cost']
                        grass = ally['biome3_attack_multiplier'] / 100
                        badlands = ally['biome4_attack_multiplier'] / 100
                        swamp = ally['biome5_attack_multiplier'] / 100
                        total = round(grass + badlands + swamp, 2)
                        t.add_row([username, group_tag, cost, grass, badlands,swamp,total])
                    message = await context.send(f'```{t.get_string(sortby="Total")} \n Page {page} of {count}```')
                    for b in buttons:
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
                            raw_response = await session.get(f"{self.url}?search={allyname}&page={page}", headers=self.headers)
                            response = await raw_response.text()
                            response = json.loads(response)
                            try:
                                allies = response['results']
                                count = math.ceil(response['count'] / 20)
                                t = PrettyTable()
                                t.left_padding_width = 0
                                t.right_padding_width = 0
                                t.align = "l"
                                t.field_names = ['Username', 'Clan', 'Cost', 'Grass' , 'Badlands','Swamp', 'Total']
                                t.align = "l"
                                for ally in allies:
                                    username = ally['username']
                                    group_tag = ally['group_tag']
                                    cost = ally['cost']
                                    grass = ally['biome3_attack_multiplier'] / 100
                                    badlands = ally['biome4_attack_multiplier'] / 100
                                    swamp = ally['biome5_attack_multiplier'] / 100
                                    total = round(grass + badlands + swamp, 2)
                                    t.add_row([username, group_tag, cost, grass, badlands,swamp,total])
                            except KeyError:
                                pass
                            await message.edit(content=f'```{t.get_string(sortby="Total")} \n Page {page} of {count}```')

                        if em == '◀️':
                            page = page-1
                            raw_response = await session.get(f"{self.url}?search={allyname}&page={page}", headers=self.headers)
                            response = await raw_response.text()
                            response = json.loads(response)
                            try:
                                allies = response['results']
                                count = math.ceil(response['count'] / 20)
                                t = PrettyTable()
                                t.left_padding_width = 0
                                t.right_padding_width = 0
                                t.align = "l"
                                t.field_names = ['Username', 'Clan', 'Cost', 'Grass' , 'Badlands','Swamp', 'Total']
                                t.align = "l"
                                for ally in allies:
                                    username = ally['username']
                                    group_tag = ally['group_tag']
                                    cost = ally['cost']
                                    grass = ally['biome3_attack_multiplier'] / 100
                                    badlands = ally['biome4_attack_multiplier'] / 100
                                    swamp = ally['biome5_attack_multiplier'] / 100
                                    total = round(grass + badlands + swamp, 2)
                                    t.add_row([username, group_tag, cost, grass, badlands,swamp,total])
                            except KeyError:
                                pass
                            await message.edit(content=f'```{t.get_string(sortby="Total")} \n Page {page} of {count}```')


    @commands.command(name="price")
    @commands.guild_only()
    async def price(self, context, *, price):
        """
        Return a list of allies from given price.
        """
        buttons = ["◀️", "▶️"]
        async with aiohttp.ClientSession() as session:
            page = 1
            raw_response = await session.get(f"{self.url}?cost={price}&page={page}", headers=self.headers)
            response = await raw_response.text()
            response = json.loads(response)
            if response.get('detail'):
                await context.send("Token Expired")
            else:
                allies = response['results']
                count = math.ceil(response['count'] / 20)
                if not allies:
                    await context.send("No results.")
                else:
                    t = PrettyTable()
                    t.left_padding_width = 0
                    t.right_padding_width = 0
                    t.align = "l"
                    t.field_names = ['Username', 'Clan', 'Cost', 'Grass' , 'Badlands','Swamp', 'Total']
                    t.align = "l"
                    for ally in allies:
                        username = ally['username']
                        group_tag = ally['group_tag']
                        cost = ally['cost']
                        grass = ally['biome3_attack_multiplier'] / 100
                        badlands = ally['biome4_attack_multiplier'] / 100
                        swamp = ally['biome5_attack_multiplier'] / 100
                        total = round(grass + badlands + swamp, 2)
                        t.add_row([username, group_tag, cost, grass, badlands,swamp,total])
                    message = await context.send(f'```{t.get_string(sortby="Total")} \n Page {page} of {count}```')
                    for b in buttons:
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
                            raw_response = await session.get(f"{self.url}?search={price}&page={page}", headers=self.headers)
                            response = await raw_response.text()
                            response = json.loads(response)
                            try:
                                allies = response['results']
                                count = math.ceil(response['count'] / 20)
                                t = PrettyTable()
                                t.left_padding_width = 0
                                t.right_padding_width = 0
                                t.align = "l"
                                t.field_names = ['Username', 'Clan', 'Cost', 'Grass' , 'Badlands','Swamp', 'Total']
                                t.align = "l"
                                for ally in allies:
                                    username = ally['username']
                                    group_tag = ally['group_tag']
                                    cost = ally['cost']
                                    grass = ally['biome3_attack_multiplier'] / 100
                                    badlands = ally['biome4_attack_multiplier'] / 100
                                    swamp = ally['biome5_attack_multiplier'] / 100
                                    total = round(grass + badlands + swamp, 2)
                                    t.add_row([username, group_tag, cost, grass, badlands,swamp,total])
                            except KeyError:
                                pass
                            await message.edit(content=f'```{t.get_string(sortby="Total")} \n Page {page} of {count}```')

                        if em == '◀️':
                            page = page-1
                            raw_response = await session.get(f"{self.url}?search={price}&page={page}", headers=self.headers)
                            response = await raw_response.text()
                            response = json.loads(response)
                            try:
                                allies = response['results']
                                count = math.ceil(response['count'] / 20)
                                t = PrettyTable()
                                t.left_padding_width = 0
                                t.right_padding_width = 0
                                t.align = "l"
                                t.field_names = ['Username', 'Clan', 'Cost', 'Grass' , 'Badlands','Swamp', 'Total']
                                t.align = "l"
                                for ally in allies:
                                    username = ally['username']
                                    group_tag = ally['group_tag']
                                    cost = ally['cost']
                                    grass = ally['biome3_attack_multiplier'] / 100
                                    badlands = ally['biome4_attack_multiplier'] / 100
                                    swamp = ally['biome5_attack_multiplier'] / 100
                                    total = round(grass + badlands + swamp, 2)
                                    t.add_row([username, group_tag, cost, grass, badlands,swamp,total])
                            except KeyError:
                                pass
                            await message.edit(content=f'```{t.get_string(sortby="Total")} \n Page {page} of {count}```')

    @commands.command(name="changes")
    @commands.guild_only()
    async def price(self, context, *, name):
        """
        Return a list of allies historical names/clans
        """
        buttons = ["◀️", "▶️"]
        async with aiohttp.ClientSession() as session:
            page = 1
            raw_response = await session.get(f"{self.base_url}/changes?search={name}&page={page}", headers=self.headers)
            response = await raw_response.text()
            response = json.loads(response)
            if response.get('detail'):
                await context.send("Token Expired")
            else:
                allies = response['results']
                count = math.ceil(response['count'] / 20)
                if not allies:
                    await context.send("No results.")
                else:
                    t = PrettyTable()
                    t.left_padding_width = 0
                    t.right_padding_width = 0
                    t.align = "l"
                    t.field_names = ['Username', 'Clan']
                    t.align = "l"
                    for ally in allies:
                        username = ally['username']
                        group_tag = ally['group_tag']
                        t.add_row([username, group_tag])
                    message = await context.send(f'```{t.get_string(sortby="Username")} \n Page {page} of {count}```')
                    for b in buttons:
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
                            raw_response = await session.get(f"{self.base_url}/changes?search={name}&page={page}", headers=self.headers)
                            response = await raw_response.text()
                            response = json.loads(response)
                            try:
                                allies = response['results']
                                count = math.ceil(response['count'] / 20)
                                t = PrettyTable()
                                t.left_padding_width = 0
                                t.right_padding_width = 0
                                t.align = "l"
                                t.field_names = ['Username', 'Clan']
                                t.align = "l"
                                for ally in allies:
                                    username = ally['username']
                                    group_tag = ally['group_tag']
                                    t.add_row([username, group_tag])
                            except KeyError:
                                pass
                            await message.edit(content=f'```{t.get_string(sortby="Username")} \n Page {page} of {count}```')

                        if em == '◀️':
                            page = page-1
                            raw_response = await session.get(f"{self.base_url}/changes?search={name}&page={page}", headers=self.headers)
                            response = await raw_response.text()
                            response = json.loads(response)
                            try:
                                allies = response['results']
                                count = math.ceil(response['count'] / 20)
                                t = PrettyTable()
                                t.left_padding_width = 0
                                t.right_padding_width = 0
                                t.align = "l"
                                t.field_names = ['Username', 'Clan']
                                t.align = "l"
                                for ally in allies:
                                    username = ally['username']
                                    group_tag = ally['group_tag']
                            except KeyError:
                                pass
                            await message.edit(content=f'```{t.get_string(sortby="Username")} \n Page {page} of {count}```')
                            
def setup(bot):
    bot.add_cog(allies(bot))