from discord import Embed

from category import Category
from commands.command import Command


class Help(Command):
    def __init__(self , commandlist, prefix):
        self.aliases = ["help"]
        self.shortdescription = "Lists all commands."
        self.longdescription = "Get info about every command currently available with syntax and a description."
        self.usage = "help [command]"
        self.category = Category.CORE
        self.commandlist = commandlist
        self.prefix = prefix
        super().__init__(self.aliases , self.shortdescription , self.longdescription , self.usage , self.category)

    async def execute(self , client , message , args , **kwargs):
        # Maximum amount of arguments is 1
        if len(args) > 1:
            await client.send_message(message.channel , content="Wrong usage! Usage: !help [command]")
            return False

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
            await client.send_message(message.channel , embed=helpembed)
            return True

        # One argument was given => Give exact info about that command
        for cmd in self.commandlist:
            # If we found the command user is looking for (Ignores case)
            for alias in cmd.aliases:
                if alias.lower() == args[0].lower():
                    # Create embed Frame
                    embed = Embed(title=self.prefix + "/".join(cmd.aliases) , color=0xff8000)
                    embed.set_author(name="Constantine Help")

                    # Create 3 embed fields
                    embed.add_field(name="Description" , value=cmd.longdescription , inline=True)
                    embed.add_field(name="Usage" , value=cmd.usage , inline=True)
                    embed.add_field(name="Category" , value=cmd.category.value , inline=True)

                    # Send the embed
                    await client.send_message(message.channel , embed=embed)
                    return True

        # No command with that name was found
        await client.send_message(message.channel , content="No command found named " + args[0])
        return True


