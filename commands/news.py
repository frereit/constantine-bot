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
        self.usage = "news <[source (default:google-news)]|info|available> [source]"
        self.category = Category.UNSURE

        # Get the key from config.json
        with open('config.json') as data_file:
            config = json.load(data_file)
        self.newskey = config['newskey']
        self.sources = json.load(urllib.request.urlopen('https://newsapi.org/v1/sources?language=en'))  # Get all available news sources
        super().__init__(self.aliases , self.shortdescription , self.longdescription , self.usage , self.category)

    def parse_time(self , unparsed):
        # Example unparsed string: 2017-11-03T13:46:07Z
        time = unparsed.split("T")[1][:-4]  # Get time and remove seconds
        date = unparsed.split("T")[0]  # Get complete date
        year = date.split("-")[0]
        month = date.split("-")[1]
        day = date.split("-")[2]
        return time + " on " + day + "." + month + "." + year  # Example return: "13:46 on 03.11.2017"

    async def execute(self , client , message , args , **kwargs):
        # at most 2 arguments
        if len(args) > 2:
            return False
        if len(args) != 0:
            if args[0] == "available":
                """ Lists all available news sources ids"""

                # Create embed Frame
                embed = Embed(title="Get more info about each source using 'news info [source]" , color=0xff8000)
                embed.set_author(name="Available news sources")
                categories = []  # All categories
                for source in self.sources['sources']:
                    if not source['category'] in categories:
                        categories.append(source['category'])  # Search for categories
                for category in categories:
                    category_text = ""  # For each category create a new field with this value
                    for source in self.sources['sources']:  # Add every news source with this value to the category value
                        if source['category'] == category:
                            category_text += source['id'] + "\n"
                    embed.add_field(name=category , value=category_text , inline=True)  # Add the category field
                await client.send_message(message.channel , embed=embed)  # Send the embed
                return True  # Command done

            if args[0] == "info":
                args.pop(0)  # Pop 'info' from the argument list
                if len(args) != 1:  # We need one more argument
                    return False

                for source in self.sources['sources']:
                    if source['id'] == args[0]:  # User wanted info about this source
                        # Create embed
                        embed = Embed(title=source['name'] , url=source['url'] , description=source['description'] ,
                                      color=0xff8000)
                        embed.add_field(name="Category" , value=source['category'] , inline=True)
                        embed.add_field(name="Language" , value=source['language'] , inline=True)
                        embed.add_field(name="ID" , value=source['id'] , inline=True)

                        # Send the embed
                        await client.send_message(message.channel , embed=embed)
                        return True  # Command done

                # No news source with the name was found
                await client.send_message(message.channel , content="No news source with the name "
                                                                    + args[0] + " is available!")
                return True
            if len(args) != 1:
                # If the first argument is not info we don't need a second argument, thus throw syntax
                return False
            srcid = args[0]
        else:
            srcid = "google-news"

        for source in self.sources['sources']:
            if source['id'] == srcid:  # User wants news of this source
                api_url = "https://newsapi.org/v1/articles?source=" + source['id'] + "&apiKey=" + self.newskey
                news = json.load(urllib.request.urlopen(api_url))
                # Create embed with no title, title is basically the author, but author looks nicer and we can use
                # the favicon with that
                embed = Embed(title="", color=0xff8000)
                embed.set_author(name=source['name'] , url=source['url'] ,
                                 icon_url="https://s2.googleusercontent.com/s2/favicons?domain=" + source['url'])
                for article in news['articles']:  # Add the articles as fields to the embed
                    embed = embed.add_field(name=article['title'] ,
                                            value=article['description'] + "\nPublished " + self.parse_time(
                                                article['publishedAt']) + "\n" + article['url'] ,
                                            inline=False)
                # Send the embed
                await client.send_message(message.channel , embed=embed)
                return True  # Done

        # No news source with the name was found
        await client.send_message(message.channel ,
                                  content="No news source with the name " + srcid + " is available!")
        return True  # Return true, we don't need to print syntax
