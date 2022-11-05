#Pure Discord.py

import discord
from discord.ext import commands
from discord.utils import get
from io import BytesIO
import random
from discord.ext import commands
from discord_slash import SlashCommand
import os

#Token
TOKEN = 'Your Token'

#For intents
intents = discord.Intents().all()
client = commands.Bot(command_prefix='#the prefix you want', intents=intents)
slash = SlashCommand(client, sync_commands=True)

intents.members = True


@client.event
async def on_ready():
  # g is holding the count of number of servers
  g = 0

  for guild in client.guilds:
    g += 1
  await client.change_presence(activity=discord.Game(name=f"Type NAA_help for the vast commands you can use"))

  print('We have logged in as {0.user}'.format(client))
    
#commands begin from here


@slash.slash(name='ping', description='This is a test')
async def ping(ctx):
  await ctx.send("NICE works")
  
@slash.slash(name='Source', description='Github link to NAA AI code')
async def source(ctx):
  await ctx.send("")
  

#DM Commands

@client.command()
async def new_member(ctx, user: discord.Member, *, message=None):
    message = f"{ctx.message.author} looks like you are new to the server. Welcome {ctx.message.author}. Here are some basic things about me. 1. You can use my commands by using @Dplayz or d!. 2.use the help commands for all commands. You have learned the basics now. Have fun"
    embed = discord.Embed(title=message)
    await user.send(embed=embed)
    
@client.command()
async def myself(ctx, user: discord.Member, *, message=None):
  message = f"{ctx.message.author} this is your user name. You can also use the R_name command to see your registered usrname in any server with NAA AI"
  embed = discord.Embed(title=message)
  await user.send(embed=embed)
    
@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int):
    await ctx.channel.purge(limit=limit)
    
    # ---/---
    
    
    
@client.command()
async def R_name(ctx):
  await ctx.reply(f"You are Registered under the name of {ctx.message.author}")


@client.command()
async def updates(ctx):
  embed = discord.Embed(title='UPTADES',
                        color=0x66ffff,
                        description='Prefix now changed to NAA_ ')

  embed.add_field(name='New Command', value='Patreons Command now added, use NAA_patreons to check it out')
  embed.add_field(name='System Update', value='Now NAA_AI is acitve for 24 hours')
  embed.add_field(name='Downtime', value='Downtime completed. Security Patch improved.')
  embed.add_field(name='New Command', value='Bot DM commands')
  embed.add_field(name='New Command', value='New purge command')

  await ctx.send(embed=embed)
  
@client.command()
async def creator(ctx):
    ctx.reply("@DhinessPlayz#2112 is the creator")


@client.command()
async def patreons(ctx):
    embed = discord.Embed(title='Patreons', description='Contributers for NAA_AI')
    
    embed.add_field(name='@Dhinesslayz#2112', value='Creator of NAA_AI')
    embed.add_field(name='Want to become a Patreon', value='Contribute to NAA_AI in any kind of way, you can dm @DhinessPlayz#2112 your contributions')
    embed.add_field(name='Join DhinessPlayz Army', value='Join DhinessPlayz Army for an exclusive NAA User role')
    embed.add_field(name='Link to join DhinessPlayz Army', value='https://discord.gg/8QvTNuDPpU')
    await ctx.send(embed=embed)    


@client.command()
async def add(ctx):
  embed = discord.Embed(title='ADD NAA AI', color=0x66ffff, description='https://discord.com/api/oauth2/authorize?client_id=1037348641255465020&permissions=0&scope=bot%20applications.commands')

  await ctx.send(embed=embed)



# ---/---


client.run(TOKEN)
