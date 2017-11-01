from discord import Embed

from category import Category
from commands.ping import Ping
from commands.say import Say
from commands.translate import Translate


class CommandHandler:
    """CommandHandler is used to call the correct command and handle help"""
    commandlist = [
        Ping() ,
        Say() ,
        Translate() ,
		HelloWorld()
    ]

    def __init__(self , prefix , client):
        self.prefix = prefix
        self.client = client

    async def handle(self , message):
        if message.content.startswith(self.prefix + "help"):
            await self.help(message , self.get_args(message.content))
            return
        for command in self.commandlist:
            if message.content.startswith(self.prefix + command.name):
                await command.execute(self.client , message , self.get_args(message.content) , )

    @staticmethod
    def get_args(message):
        args = message.split(" ")
        args.pop(0)
        return args

    async def help(self , message , args):
        if len(args) > 1:
            await self.client.send_message(message.channel , content="Wrong usage! Usage: !help [command]")
            return

        # List all commands
        if len(args) == 0:
            # https://cog-creators.github.io/discord-embed-sandbox/
            helpembed = Embed(title="\n" , color=0xff8000)
            helpembed.set_author(name="Constantine Help")
            for cat in Category:
                cmds = ""
                for cmd in self.commandlist:
                    if cmd.category == cat:
                        cmds += self.prefix + cmd.getshortinfo() + "\n"
                helpembed.add_field(name=cat.value , value=cmds , inline=False)

            await self.client.send_message(message.channel , embed=helpembed)
            return

        # Give exact info about specific command
        found = False
        for cmd in self.commandlist:
            if cmd.name == args[0]:
                embed = Embed(title=self.prefix + cmd.name , color=0xff8000)
                embed.set_author(name="Constantine Help")
                embed.add_field(name="Description" , value=cmd.longdescription , inline=True)
                embed.add_field(name="Usage" , value=cmd.usage , inline=True)
                embed.add_field(name="Category" , value=cmd.category.value , inline=True)
                await self.client.send_message(message.channel , embed=embed)
                found = True
        if not found:
            await self.client.send_message(message.channel , content="No command found named " + args[0])
