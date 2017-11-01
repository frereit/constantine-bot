import discord
import json
from handler import CommandHandler


with open('config.json') as data_file:
    config = json.load(data_file)


prefix = config['prefix']
token = config['token']
client = discord.Client()
handler = CommandHandler(prefix, client)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(prefix):
        await handler.handle(message)


client.run(token)
