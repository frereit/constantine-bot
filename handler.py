# Import all commands
from commands.crypto import Crypto
from commands.decrypt import Decrypt
from commands.encrypt import Encrypt
from commands.hash import Hash
from commands.math import Math
from commands.news import News
from commands.nowplaying import Playing
from commands.ping import Ping
from commands.play import Play
from commands.queue import Queue
from commands.queuehelper import QueueHelper
from commands.say import Say
from commands.shuffle import Shuffle
from commands.translate import Translate
from commands.help import Help
from commands.helloworld import HelloWorld
from commands.wiki import Wiki


class CommandHandler:
    """CommandHandler is used to call the correct command and handle help"""

    # Command Prefix and Client are passed on by constantine.py so that the commands can send messages
    def __init__(self , prefix , client):
        # Used to keep track of all commands available
        queuehelper = QueueHelper()
        self.commandlist = [
            Ping() ,
            Say() ,
            Translate() ,
            HelloWorld(),
            News(),
            Crypto(),
            Math(),
            Play(queuehelper),
            Playing(queuehelper),
            Queue(queuehelper),
            Shuffle(queuehelper),
            Hash(),
            Encrypt(),
            Decrypt(),
            Wiki(),
        ]
        self.prefix = prefix
        self.client = client
        self.commandlist.append(Help(self.commandlist , self.prefix))  # This shall be added last

    # Searches for the correct command and calls it.
    async def handle(self , message):
        # Search for the command with the correct name, ignores case
        for command in self.commandlist:
            if self.is_alias(command, message.content):
                if not await command.execute(self.client , message , self.get_args(message.content)):
                    await self.client.send_message(message.channel , content=command.get_wrong_usage())

    # Arguments are parsed in the handler so that creating a new command is even easier (of courses we could just
    # parse in the __init__ of command.py but it both works.
    @staticmethod
    def get_args(message):
        args = message.split(" ")
        args.pop(0)
        return args

    def is_alias(self, cmd, message):
        for alias in cmd.aliases:
            if message.lower().startswith(self.prefix + alias.lower()):
                return True
        return False
