from category import Category
from commands.command import Command
from crypthelper import AESCipher


class Encrypt(Command):
    def __init__(self):
        aliases = ["encrypt"]
        shortdescription = "Encrypt text using AES"
        longdescription = "Encrypt a string using AES Encryption with a user-specified password"
        usage = "/".join(aliases) + "<password> <text>"
        category = Category.UTIL
        super().__init__(aliases , shortdescription , longdescription , usage , category)

    async def execute(self , client , message , args , **kwargs):
        if len(args) == 0:
            return False
        password = args.pop(0)
        text = " ".join(args)
        encrypted = AESCipher(password).encrypt(text)
        await client.send_message(message.channel , content=encrypted.decode('utf-8'))
        return True
