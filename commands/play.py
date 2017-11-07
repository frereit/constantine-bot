from category import Category
from commands.command import Command
from commands.queuehelper import QueueHelper
import re


class Play(Command):
    def __init__(self, queuehelper):
        aliases = ["play" , "yt" , "youtube"]
        shortdescription = "Plays a YouTube video in a voice channel"
        longdescription = "Plays a YouTube video in a voice channel"
        usage = "/".join(aliases) + " <link>"
        category = Category.MEDIA
        self.player = None
        self.idle = True
        self.queue = queuehelper
        self.urlregex = re.compile(r'(?:https://)?(?:www\.)?youtube\.com/watch\?v=[a-zA-Z0-9]{11}')
        super().__init__(aliases , shortdescription , longdescription , usage , category)

    async def execute(self , client , message , args , **kwargs):
        if client.is_voice_connected(message.server):
            voice = client.voice_client_in(message.server)
        else:
            if message.author.voice.voice_channel is None:
                await client.send_message(message.channel , content="You must be in a voice channel!")
                return True
            voice_channel = message.author.voice.voice_channel
            voice = await client.join_voice_channel(voice_channel)
        if not self.urlregex.fullmatch(args[0]):
            await client.send_message(message.channel,
                                      content="Invalid URL! A search function will be implemented soon.")
            return True
        player = await voice.create_ytdl_player(args[0], ytdl_options=None, after=self.play_next)
        player.volume = 0.1
        if self.idle:
            player.start()
            self.queue.nowplaying = player
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
            self.queue.nowplaying = player
        else:
            self.queue.nowplaying = None
            self.idle = True
