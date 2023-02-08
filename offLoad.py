from asyncio import tasks
import discord 
import aiohttp
import asyncio
import os
import time
import logging
import logging.handlers
from datetime import datetime
from discord.ext import commands, tasks

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)

with open('cred.txt', 'r') as f:
    global token 
    token = f.read()

async def main():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.ERROR)

    handler = logging.handlers.RotatingFileHandler(
        filename='discord.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=5,  # Rotate through 5 files
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    async with bot:
        await bot.start(token)
        
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


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

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! `{0}ms`'.format(round(bot.latency, 1)))
    
## Basic Error handler ##
@bot.event
async def on_command_error(ctx, error):
    em = discord.Embed(description=f"Command: `{ctx.command}`\n```{error}```")
    await ctx.send(embed=em)
    raise error
    
asyncio.run(main())
