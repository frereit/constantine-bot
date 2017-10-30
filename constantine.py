#import discord
from discord.ext import commands
import json

with open('config.json') as data_file:
    config = json.load(data_file)

description = config['description']
prefix = config['prefix']
token = config['token']

'''There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def ping():
    """Check if bot is active"""
    await bot.say('Pong!')

bot.run(token)
