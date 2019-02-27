from discord import Embed
from commands.command import Command
from category import Category


def get_id(url):
    return url[-11:]


class Playing(Command):
    def __init__(self , queuehelper):
        aliases = ["nowplaying" , "playing" , "currentsong" , "np"]
        shortdescription = "Shows information about the currently playing song"
        longdescription = "See detailed information about the current song"

        usage = "/".join(aliases) + " "
        category = Category.MEDIA
        self.queue = queuehelper
        super().__init__(aliases , shortdescription , longdescription , usage , category)

    async def execute(self , client , message , args , **kwargs):
        if len(args) != 0:
            return False
        player = self.queue.nowplaying
        if player is None:
            await client.send_message(message.channel ,
                                      content="No song is currently on air! Start a song using `play <url>`!")
            return True
        embed = Embed(title=player.uploader , description=player.description , color=0xff8000)
        embed.set_author(name=player.title , url=player.url ,
                         icon_url="https://www.google.com/s2/favicons?domain=www.youtube.com")
        embed.set_thumbnail(url="http://i4.ytimg.com/vi/" + get_id(player.url) + "/default.jpg")
        embed.set_footer(text=str(player.views) + " views | "
                              + str(player.likes) + " likes | "
                              + str(player.dislikes) + " dislikes")
        await client.send_message(message.channel , embed=embed)
        return True
