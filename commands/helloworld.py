from commands.command import Command
from category import Category
class HelloWorld(Command):

    def __init__(self):
        aliases = ["HelloWorld", "Hello"]
        shortdescription = "A generic Hello World command"
        longdescription = "A command that when used returns 'Hello World'"

        usage = "/".join(aliases)
        category = Category.CORE
        super().__init__(aliases, shortdescription, longdescription, usage, category)

    async def execute(self, client, message, args, **kwargs):
        await client.send_message(message.channel, content = "Hello World")
        return True