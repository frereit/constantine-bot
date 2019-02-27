import wikipedia
from discord import Embed

from category import Category
from commands.command import Command


class Wiki(Command):
    def __init__(self):
        aliases = ["wikipedia" , "wiki"]
        shortdescription = "A command that shows the most relevant Wikipedia article"
        longdescription = "A command that shows the most relevant Wikipedia article"

        usage = "/".join(aliases) + " [Amount of Sentences] <Article>"
        category = Category.UTIL
        super().__init__(aliases , shortdescription , longdescription , usage , category)

    async def execute(self , client , message , args , **kwargs):
        if len(args) == 0:
            return False
        if args[0].isdigit():
            sentences = args.pop(0)
        else:
            sentences = 2
        user_input = " ".join(args)
        search = wikipedia.page(user_input)
        page_title = search.title
        page_url = search.url
        page_summary = wikipedia.summary(user_input , sentences=sentences)
        embed = Embed(title=page_title , description=page_summary, url=page_url, color=0xff8000)
        embed.set_author(name="Wikipedia" , url="https://en.wikipedia.org" ,
                         icon_url="https://s2.googleusercontent.com/s2/favicons?domain=" + page_url)
        await client.send_message(message.channel , embed=embed)
        return True
