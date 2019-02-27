from category import Category
from commands.command import Command
from crypthelper import AESCipher


class Decrypt(Command):
    def __init__(self):
        aliases = ["decrypt"]
        shortdescription = "Decrypt text using AES"
        longdescription = "Decrypts a string using AES Encryption with a user-specified password"
        usage = "/".join(aliases) + "<password> <text>"
        category = Category.UTIL
        super().__init__(aliases , shortdescription , longdescription , usage , category)

    async def execute(self , client , message , args , **kwargs):
        if len(args) == 0:
            return False
        password = args.pop(0)
        text = " ".join(args)
        decrypted = AESCipher(password).decrypt(text)
        await client.send_message(message.channel , content=decrypted)
        return True
