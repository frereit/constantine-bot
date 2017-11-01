import discord  # Discord API Wrapper
import json  # JSON De/Encoder
from handler import CommandHandler  # Handles all the commands

# Read the config as json object
with open('config.json') as data_file:
    config = json.load(data_file)

# Get the different options from the json object
prefix = config['prefix']
discordtoken = config['discordtoken']

# Create new client and handler instance
client = discord.Client()
handler = CommandHandler(prefix , client)


# Log to console when the client is started
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


# Fires every time a new message is received
@client.event
async def on_message(message):
    # Make sure we don't handle messages that we sent, that would be VERY inefficient.
    if message.author == client.user:
        return

    # This easy test can be done here, makes it clear that the handler is handling commands and NOT checking if they
    # are commands
    if message.content.startswith(prefix):
        await handler.handle(message)

# Connect the client to Discord
client.run(discordtoken)
