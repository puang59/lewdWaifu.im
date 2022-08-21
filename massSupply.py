from asyncio import tasks
import discord 
import aiohttp
import asyncio
import os
import sys
import random
from datetime import datetime
from discord.ext import commands, tasks

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=["!","?"], case_insensitive=True, intents=intents)

# with open('cred.txt', 'r') as f:
#     global token 
#     token = f.read()

token = os.environ['TOKEN']
async def main():
    async with bot:
        supply.start()
        print('Supply started!')
        await bot.start(token)

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.command()
async def restart(ctx): 
    if ctx.message.author.id == 852797584812670996: 
        await ctx.send("Restarted!")
        restart_bot()
    else: 
        await ctx.send("You cannot use this command!")

@tasks.loop(minutes=30)
async def supply():
    await bot.wait_until_ready()
    # putang = ctx.guild.get_member(852797584812670996)
    # deory = ctx.guild.get_member(409994220309577729)
    # if ctx.message.author.id == 852797584812670996:
    #     await ctx.message.delete()
    guild = bot.get_guild(1006254992648327290)
    pause_role = guild.get_role(1010788120511381524)
    i = 0
    while i < 10: 
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
                        if not pause_role in member.roles:
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
        log_channel = bot.get_channel(990523749721833532)
        txt = await channel.fetch_message(1006506210092122172)
        dt = datetime.now()
        embed = discord.Embed(description=f"✅  Latest supply sent <t:{int(dt.timestamp())}:R>\n```diff\n+ Successfully sent to everyone! +```")
        embed.set_footer(text="Supply interval: 30 mins")
        await txt.edit(embed=embed)
        await log_channel.send("Supplied successfully!!!")
        await asyncio.sleep(1800)
    # else: 
    #     await ctx.send("❌ Supply denied!")

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

@bot.command()
async def pause(ctx): 
    guild = bot.get_guild(1006254992648327290)
    pause_role = guild.get_role(1010788120511381524)

    if not pause_role in ctx.message.author.roles:
        await ctx.message.author.add_roles(pause_role)
        await ctx.message.add_reaction("✅")
        await ctx.message.author.send("I have paused your supply! Use command `?unpause` in <#1006267225432408155> to continue supplies")
    else: 
        await ctx.send("I have already paused your supply!\nIf you want to unpause then use the command `?unpause`")

@bot.command()
async def unpause(ctx): 
    guild = bot.get_guild(1006254992648327290)
    pause_role = guild.get_role(1010788120511381524)

    if pause_role in ctx.message.author.roles:
        await ctx.message.author.remove_roles(pause_role)
        await ctx.message.add_reaction('✅')
        await ctx.message.author.send("I'll be sending you supplies!")
    else: 
        await ctx.message.add_reaction('✅')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! `{0}ms`'.format(round(bot.latency, 1)))

asyncio.run(main())
