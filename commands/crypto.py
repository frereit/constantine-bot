import urllib
import json
from discord import Embed
from category import Category
from commands.command import Command


class Crypto(Command):
    def __init__(self):
        aliases = ['stock' , 'crypto']
        shortdescription = "Check prices of cryptocurrencies"
        longdescription = "Get the prices of user-specified crypto currency from https://www.cryptocompare.com. "
        usage = "/".join(aliases) + " <available|<stock symbol (eg. BTC)>>"
        category = Category.UNSURE
        super().__init__(aliases , shortdescription , longdescription , usage , category)

    async def execute(self , client , message , args , **kwargs):
        if len(args) != 1:
            return False

        if args[0] == 'available':
            await client.send_message(message.channel ,
                                      content="You can see all available here: https://www.cryptocompare.com/coins/")
            """
            available = json.load(urllib.request.urlopen('https://min-api.cryptocompare.com/data/all/coinlist'))
            availablesmsg = ""
            for key, value in available['Data'].items():
                availablesmsg += value['Symbol'] + ","
            print(len(availablesmsg))
            await client.send_message(message.channel , content=availablesmsg)
            """
            return True

        # Alright, a stock symbol was supplied
        response = json.load(urllib.request.urlopen('https://min-api.cryptocompare.com/data/price?fsym='
                                                    + args[0] + '&tsyms=BTC,USD,EUR'))
        if 'Response' in response:
            await client.send_message(message.channel , content=response['Message'])
            return True
        await client.send_message(message.channel , content="1 " + args[0] + " is worth "
                                                            + str(response['BTC']) + " Bitcoin or "
                                                            + str(response['USD']) + " USD or "
                                                            + str(response['EUR']) + " EUR")
        return True
