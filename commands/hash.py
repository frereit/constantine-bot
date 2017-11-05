from category import Category
from commands.command import Command
import hashlib


class Hash(Command):
    def __init__(self):
        aliases = ["hash"]
        shortdescription = "Hash a string using a variety of hashing algorithms"
        longdescription = "Returns the hashed version of a user-specified string using a user-specified hashing " \
                          "algorithm."
        usage = "/".join(aliases) + " <algorithm|available> [text]"
        category = Category.UTIL
        super().__init__(aliases , shortdescription , longdescription , usage , category)

    async def execute(self , client , message , args , **kwargs):
        if len(args) < 1:
            return False

        if args[0] == 'available':
            if len(args) != 1:
                return False
            text = "Available algorithms: ```" + ", ".join(hashlib.algorithms_available) + "```"
            await client.send_message(message.channel , content=text)
            return True

        if args[0] in hashlib.algorithms_available:
            algorithm = args.pop(0)
            h = hashlib.new(algorithm)
            unhashed = " ".join(args).encode('utf-8')
            h.update(unhashed)
            text = "Hashed with " + algorithm + "! Result: " + str(h.hexdigest())
            await client.send_message(message.channel , content=text)
            return True
        else:
            text = "Algorithm not recognized!\nAvailable algorithms: ```" + ", ".join(
                hashlib.algorithms_available) + "```"
            await client.send_message(message.channel , content=text)
            return True
