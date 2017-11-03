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
        # At least 1 and at mose 2 arguments
        if len(args) < 1 or len(args) > 2:
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

        if args[0] == "info":
            args.pop(0)  # Pop 'info' from the argument list
            if len(args) != 1:
                return False

            for source in self.sources['sources']:
                if source['id'] == args[0]:
                    embed = Embed(title=source['name'] , url=source['url'] , description=source['description'] ,
                                  color=0xff8000)
                    embed.add_field(name="Category" , value=source['category'] , inline=True)
                    embed.add_field(name="Language" , value=source['language'] , inline=True)
                    embed.add_field(name="ID" , value=source['id'], inline=True)
                    await client.send_message(message.channel , embed=embed)
                    return True
            await client.send_message(message.channel , content="No news source with the name "
                                                                + args[0] + " is available!")
            return True
