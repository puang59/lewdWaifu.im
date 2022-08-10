import discord 
import aiohttp
import asyncio
import os
import time
from datetime import datetime
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)

with open('cred.txt', 'r') as f:
    global token 
    token = f.read()

async def main():
    async with bot:
        print("Bot ready!")
        await bot.start(token)

@bot.command()
async def ts(ctx):
    dt = datetime.now()
    em = discord.Embed(description=f"<t:{int(dt.timestamp())}:R>")
    await ctx.send(embed=em)

@bot.command()
async def wp(ctx): 
    url = "https://api.waifu.pics/nsfw/waifu"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response: 
            res = await response.json()
            await ctx.send(f"|| {res['url']} ||")

@bot.event
async def on_command_error(ctx, error):
    em = discord.Embed(description=f"Command: `{ctx.command}`\n```{error}```")
    await ctx.send(embed=em)
    raise error

asyncio.run(main())
