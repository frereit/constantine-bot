from enum import Enum

from commands.ping import Ping


class Category(Enum):
    CORE = 0


class CommandHandler:
    """CommandHandler is used to call the correct command and handle help"""
    commandlist = [
        Ping("ping" , "Simple command to test the bot." , "This command can not only be used to check if the "
                                                          "bot is listening but also to check the response "
                                                          "time of it." , "No arguments." , Category.CORE)
    ]

    def __init__(self , prefix, client):
        self.prefix = prefix
        self.client = client

    async def handle(self , message):
        if message.content.startswith(self.prefix + "help"):
            self.help(message)
            return
        for command in self.commandlist:
            if message.content.startswith(self.prefix + command.name):
                await command.execute(self.client, message, self.get_args(message.content) , )

    @staticmethod
    def get_args(message):
        lencommand = len(message.split(" ")[0])
        args = message[lencommand:].split(" ")
        return args

    def help(self , message):
        """ Not implemented """
        raise NotImplementedError
