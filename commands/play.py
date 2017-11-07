from discord import Channel
from discord.voice_client import StreamPlayer

from category import Category
from commands.command import Command


class Play(Command):
    def __init__(self):
        aliases = ["play" , "yt" , "youtube"]
        shortdescription = "Plays a YouTube video in a voice channel"
        longdescription = "Plays a YouTube video in a voice channel"
        usage = "/".join(aliases) + " <link>"
        category = Category.MEDIA
        self.queue = []
        self.player = None
        self.idle = True
        super().__init__(aliases , shortdescription , longdescription , usage , category)

    async def execute(self , client , message , args , **kwargs):
        if message.author.voice.voice_channel is None:
            await client.send_message(message.channel , content="You must be in a voice channel!")
            return True
        if client.is_voice_connected(message.server):
            voice = client.voice_client_in(message.server)
        else:
            voice_channel = message.author.voice.voice_channel
            voice = await client.join_voice_channel(voice_channel)
        player = await voice.create_ytdl_player(args[0], ytdl_options=None, after=self.play_next)
        player.volume = 0.1
        if self.idle:
            player.start()
            self.idle = False
            return True
        await client.send_message(message.channel , content="Added " + player.title + " to queue!")
        self.queue.append(player)
        return True

    def play_next(self):
        if len(self.queue) != 0:
            self.idle = False
            player = self.queue.pop(0)
            player.start()
        else:
            self.idle = True
