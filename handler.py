from discord import Embed  # used to create tables (e.g !help)
from category import Category  # Category Enum with all the different Categories

# Import all commands
from commands.ping import Ping
from commands.say import Say
from commands.translate import Translate


class CommandHandler:
    """CommandHandler is used to call the correct command and handle help"""

    # Used to keep track of all commands available
    commandlist = [
        Ping() ,
        Say() ,
        Translate()
    ]

    # Command Prefix and Client are passed on by constantine.py so that the commands can send messages
    def __init__(self , prefix , client):
        self.prefix = prefix
        self.client = client

    # Searches for the correct command and calls it.
    async def handle(self , message):
        # Help is managed inside of handler.py, we should move this out of here and
        # transform it into a regular command (Just overwrite __init__ with extra argument for commandlist
        # so that it can access all the other commands.
        if message.content.lower().startswith(self.prefix + "help"):
            await self.help(message , self.get_args(message.content))
            return

        # Search for the command with the correct name, ignores case
        for command in self.commandlist:
            if message.content.startswith(self.prefix + command.name.lower()):
                if not await command.execute(self.client , message , self.get_args(message.content)):
                    await self.client.send_message(message.channel , content=command.get_wrong_usage())

    # Arguments are parsed in the handler so that creating a new command is even easier (of courses we could just
    # parse in the __init__ of command.py but it both works.
    @staticmethod
    def get_args(message):
        args = message.split(" ")
        args.pop(0)
        return args

    # Help command, we should transform this to normal command with extra argument
    async def help(self , message , args):
        # Maximum amount of arguments is 1
        if len(args) > 1:
            await self.client.send_message(message.channel , content="Wrong usage! Usage: !help [command]")
            return

        # If no command was specified list all commands
        if len(args) == 0:
            # Create embed frame
            helpembed = Embed(title="\n" , color=0xff8000)
            helpembed.set_author(name="Constantine Help")

            # Loop through each category and create a new field for it. Append all commands with that category to the
            #  fields value
            for cat in Category:
                cmds = ""
                for cmd in self.commandlist:
                    if cmd.category == cat:
                        cmds += self.prefix + cmd.getshortinfo() + "\n"
                helpembed.add_field(name=cat.value , value=cmds , inline=False)

            # Send the embed
            await self.client.send_message(message.channel , embed=helpembed)
            return

        # One argument was given => Give exact info about that command
        for cmd in self.commandlist:
            # If we found the command user is looking for (Ignores case)
            if cmd.name.lower() == args[0].lower():
                # Create embed Frame
                embed = Embed(title=self.prefix + cmd.name , color=0xff8000)
                embed.set_author(name="Constantine Help")

                # Create 3 embed fields
                embed.add_field(name="Description" , value=cmd.longdescription , inline=True)
                embed.add_field(name="Usage" , value=cmd.usage , inline=True)
                embed.add_field(name="Category" , value=cmd.category.value , inline=True)

                # Send the embed
                await self.client.send_message(message.channel , embed=embed)
                return

        # No command with that name was found
        await self.client.send_message(message.channel , content="No command found named " + args[0])
