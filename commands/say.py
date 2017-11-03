from category import Category
from commands.command import Command


class Say(Command):
    def __init__(self):
        self.aliases = ["say" , "send_message"]
        self.shortdescription = "Makes the bot say whatever you want."
        self.longdescription = "Makes the bot say whatever you want. Used to check if arguments are working."
        self.usage = "/".join(self.aliases) + " <Text>"
        self.category = Category.CORE
        super().__init__(self.aliases , self.shortdescription , self.longdescription , self.usage , self.category)

    async def execute(self , client , message , args , **kwargs):
        # We need text, thus at least 1 argument
        if len(args) == 0:
            return False  # No arguments, print syntax

        # Send back whatever the user inputs
        await client.send_message(message.channel , content=" ".join(args))
        return True  # Command was run successfully
