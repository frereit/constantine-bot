from commands.command import  Command


class Ping(Command):

    @staticmethod
    async def execute(client, message , args , **kwargs):
        print(message.author + " executed the ping command.")
        await client.send_message(message.channel, content="Pong!")
