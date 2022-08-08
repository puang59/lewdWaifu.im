import discord 
import aiohttp
import asyncio
import os
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)

# with open('cred.txt', 'r') as f:
#     global token 
#     token = f.read()

token = os.environ['TOKEN']
async def main():
    async with bot:
        print("Bot ready!")
        await bot.start(token)

@bot.command()
async def supply(ctx):
    i = 0
    while i<=10: 
        members = [852797584812670996, 409994220309577729]
        for z in members: 
            mem = ctx.guild.get_member(z)
            url = "https://api.waifu.im/random/?" \
            "&gif=false" \
            "&is_nsfw=true"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    res = await response.json()
                    await mem.send(f"|| {res['images'][0]['url']} ||")

        await asyncio.sleep(43200)


asyncio.run(main())
