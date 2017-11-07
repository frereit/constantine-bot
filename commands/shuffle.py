from commands.command import Command
from category import Category
from random import shuffle


class Shuffle(Command):
    def __init__(self, queuehelper):
        aliases = ["shuffle" , "randomize"]
        shortdescription = "Shuffles the queue"
        longdescription = "Shuffles the queue"
        usage = "/".join(aliases) + " "
        category = Category.MEDIA
        self.queue = queuehelper
        super().__init__(aliases , shortdescription , longdescription , usage , category)

    async def execute(self , client , message , args , **kwargs):
        if len(args) != 0:
            return False
        shuffle(self.queue.queue)
        await client.send_message(message.channel, content="Shuffled queue!")
        return True
