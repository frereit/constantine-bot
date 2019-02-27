from discord import Embed

from commands.command import Command
from category import Category


class Queue(Command):
    def __init__(self, queuehelper):
        aliases = ["queue"]
        shortdescription = "List upcoming songs"
        longdescription = "Lists the next 10 upcoming songs"
        usage = "/".join(aliases) + " "
        category = Category.MEDIA
        self.queue = queuehelper
        super().__init__(aliases , shortdescription , longdescription , usage , category)

    async def execute(self , client , message , args , **kwargs):
        if len(args) != 0:
            return False
        if len(self.queue) == 0:
            await client.send_message(message.channel, content="No songs are currently enqueued!")

        embed = Embed(title="Music Queue" , color=0xff8000)
        for player in self.queue.queue:
            if len(embed.fields) < 10:
                embed.add_field(name=player.title, value=player.uploader, inline=False)
            else:
                break
        await client.send_message(message.channel, embed=embed)
        return True


