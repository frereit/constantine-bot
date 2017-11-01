from category import Category
from commands.command import Command


class Ping(Command):

    def __init__(self):
        self.name = "ping"
        self.shortdesc = "Sends 'Pong' back"
        self.longdesc = "This command not only allows you to check if the bot is active, it also allows you to check " \
                        "response time. "
        self.usage = "No arguments."
        self.category = Category.CORE
        super().__init__(self.name , self.shortdesc , self.longdesc , self.usage , self.category)

    async def execute(self , client , message , args , **kwargs):
        print(message.author.name + " executed " + str(self.name))
        print(str(len(args)))
        if len(args) != 0:
            await client.send_message(message.channel, content=self.getfullinfo())
            return False  # Too many arguments, print syntax
        await client.send_message(message.channel, content="Pong!")
        return True  # Command was run successfully
