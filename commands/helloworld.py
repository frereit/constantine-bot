from category import Category
from commands.command import Command


class HelloWorld(Command):
    def __init__(self):
        self.name = "HelloWorld"
        self.shortdescription = "Generic Test Command"
        self.longdescription = "The most cliche test commnand ever."
        self.usage = self.name
        self.category = Category.CORE
        super().__init__(self.name , self.shortdescription , self.longdescription , self.usage , self.category)

    async def execute(self , client , message , args , **kwargs):
	client.send_message(message.channel , content="HelloWorld")