import discord 
import aiohttp
import asyncio
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)

async def main():
    async with bot:
        print("Bot ready!")
        await bot.start("OTMxNTU0MjM4MDg0MDU1MTAy.GOAp7a.7IIFfazN7rgnEXeAO6sHyctLt1jZ0H3XPamjLw")

@bot.command()
async def supply(ctx):
    i = 0
    while i<=10: 
        members = [852797584812670996, 409994220309577729]
        mem1 = ctx.guild.get_member(members[0])
        mem2 = ctx.guild.get_member(members[1])
        url = "https://api.waifu.im/random/?" \
        "&gif=false" \
        "&is_nsfw=true"
        counter = 0 
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                res = await response.json()
                await mem1.send(f"|| {res['images'][0]['url']} ||")
                await mem2.send(f"|| {res['images'][0]['url']} ||") 

        await asyncio.sleep(5)


asyncio.run(main())
