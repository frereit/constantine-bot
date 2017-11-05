from discord import Channel

from category import Category
from commands.command import Command


class Play(Command):
    def __init__(self):
        aliases = ["play", "yt", "youtube"]
        shortdescription = "Plays a YouTube video in a voice channel"
        longdescription = "Plays a YouTube video in a voice channel"
        usage = "/".join(aliases) + " <link> [voice-channel]"
        category = Category.MEDIA
        super().__init__(aliases , shortdescription , longdescription , usage , category)

    async def execute(self , client , message , args , **kwargs):
        if message.author.voice.voice_channel is None:
            await client.send_message(message.channel, content="You must be in a voice channel!")
            return True
        voice_channel = message.author.voice.voice_channel

        voice = await client.join_voice_channel(voice_channel)
        player = await voice.create_ytdl_player(args[0])
        player.start()
        return True
