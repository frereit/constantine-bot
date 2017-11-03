from discord import Embed
import json
import urllib
from category import Category
from commands.command import Command


class News(Command):
    def __init__(self):
        self.aliases = ['news']
        self.shortdescription = "Get news from various sources. Uses https://newsapi.org/"
        self.longdescription = "Get the headlines from various news sources from https://newsapi.org/."
        self.usage = "news <[source]|info|available> [source]"
        self.category = Category.UNSURE
        self.sources = json.load(urllib.request.urlopen('https://newsapi.org/v1/sources?language=en'))
        super().__init__(self.aliases , self.shortdescription , self.longdescription , self.usage , self.category)

    async def execute(self , client , message , args , **kwargs):
        # User either uses news source OR available as subcommand => Exactly one argument needed
        if len(args) != 1:
            return False

        if args[0] == "available":
            # Create embed Frame
            embed = Embed(title="Get more info about each source using 'news info [source]" , color=0xff8000)
            embed.set_author(name="Available news sources")
            categories = []
            for source in self.sources['sources']:
                if not source['category'] in categories:
                    categories.append(source['category'])
            for category in categories:
                category_text = ""
                for source in self.sources['sources']:
                    if source['category'] == category:
                        category_text += source['id'] + "\n"
                embed.add_field(name=category , value=category_text , inline=True)
            # Send the embed
            await client.send_message(message.channel , embed=embed)
            return True
