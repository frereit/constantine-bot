from commands.command import Command
from category import Category
class HelloWorld(Command):

    def __init__(self):
        self.aliases = ["HelloWorld", "Hello"]
        self.shortdescription = "A generic Hello World command"
        self.longdescription = "A command that when used returns 'Hello World'"

        self.usage = "/".join(self.aliases)
        self.category = Category.CORE
        super().__init__(self.aliases, self.shortdescription, self.longdescription, self.usage, self.category)

        async def execute(self, client, message, args, **kwargs):
            await client.send_messages(message.channel.content = "Hello World")
