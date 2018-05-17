from discord.ext.commands import Bot
import discord
from discord.ext import commands
import asyncio
import random

BOT_PREFIX = ('!')  # prefix to use when calling bot commands
TOKEN = 'NDM2OTkxNDExMjI1ODg2NzIw.DbvjiQ.84bwfdO6b3KXLMBV6znJPacYoY0'
bot = Bot(command_prefix=BOT_PREFIX)  # initialise bot client


@bot.event
async def on_ready():
    global servers
    servers = bot.servers
    em = discord.Embed(title='Yoooo', color=0x777777)
    for server in servers:
        print(server)
        if server.id == '441600399477178369':
            global democrat
            democrat = server

        if server.id == '440034563423469578':
            global hypezone
            hypezone = server

@bot.command(name='hello',
             description='A simple greeting',
             brief='Hello',
             aliases=['hi', 'hey', 'yo'],
             pass_context=True)
async def greeting(context):
    embed = discord.Embed(title="Hi", color=0x777777)
    await bot.say(embed=embed)


@bot.command(description='dispays the rules of the server',
             pass_context=True)
async def rules(context):
    em = discord.Embed(title='Rules', color=0x777777)
    em.add_field(name='Rule 1', value='Dont abuse mod', inline=False)
    em.add_field(name='Rule 2', value='Abuse Nolan', inline=False)
    await bot.say(embed=em)


@bot.command()
@commands.has_permissions(kick_members=True)
# checks user for kick users permission
async def kick(username: discord.User):
    await bot.kick(username)
    await bot.say('User has been kicked')


@bot.command(pass_context=True)
async def purge(ctx, ammount: int):
    await bot.purge_from(ctx.message.channel, limit=ammount + 1)


@bot.command()
async def vote():
    members = democrat.members
    print(members)
    for member in members:
        nicknames = []
        print
        nicknames.append(member.id)
    print(nicknames)
    vote = random.choice(nicknames)
    em = discord.Embed(title='Voted', description=str(vote), color=0x777777)
    randoms = random.randint(1, 2)
    await bot.say(str(randoms))


bot.run(TOKEN)
