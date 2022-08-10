import discord 
import aiohttp
import asyncio
import os
import random
from datetime import datetime
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
    if ctx.message.author.id == 852797584812670996:
        i = 0
        while i < 10: 
            guild = bot.get_guild(1006254992648327290)
            wpic = "https://api.waifu.pics/nsfw/waifu" #waifu.pics url
            wim = "https://api.waifu.im/random/?" \
            "&gif=false" \
            "&is_nsfw=true" # waifu.im url
            url = random.choice([wim, wpic])
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    res = await response.json()
                    for member in guild.members: 
                        if not member.bot: 
                            try: 
                                try: 
                                    await member.send(f"|| {res['images'][0]['url']} ||") #waifu.im
                                except: 
                                    await member.send(f"|| {res['url']} ||") #waifu.pics
                            except: 
                                ch = bot.get_channel(1006267225432408155)
                                em = discord.Embed(description="I cannot send you your supply, please check your Privacy & Saftey settings.", color=discord.Colour.red())
                                await ch.send(f"oii senpai!!! {member.mention}", embed=em)

            channel = bot.get_channel(1006254993227137188)
            txt = await channel.fetch_message(1006506210092122172)
            dt = datetime.now()
            embed = discord.Embed(description=f"✅  Latest supply sent <t:{int(dt.timestamp())}:R>")
            embed.set_footer(text="Supply interval: 30 mins")
            await txt.edit(embed=embed)
            await asyncio.sleep(1800)
    else: 
        await ctx.send("❌ Supply denied!")

@bot.event
async def on_member_join(member): 
    url = "https://api.waifu.im/random/?" \
    "&gif=false" \
    "&is_nsfw=true"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            res = await response.json()
            if not member.bot: 
                try: 
                    await member.send(f"|| {res['images'][0]['url']} || (Wait for your next supply uwu)")
                except: 
                    ch = bot.get_channel(1006267225432408155)
                    em = discord.Embed(description="I cannot send you your supply, please check your Privacy & Saftey settings.", color=discord.Colour.red())
                    await ch.send(f"oii senpai!!! {member.mention}", embed=em)  

asyncio.run(main())
