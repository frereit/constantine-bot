from category import Category
from commands.command import Command
import requests

class Math(Command):
    def __init__(self):
        aliases = ['math' , 'calculate']
        shortdescription = "Evaluates math expressions."
        longdescription = 'This command evaluates a user-specified mathematical expression using the ' \
                          'free MathJS API. http://api.mathjs.org/.'
        usage = "/".join(aliases) + " <expression>"
        category = Category.UTIL
        super().__init__(aliases , shortdescription , longdescription , usage , category)

    async def execute(self , client , message , args , **kwargs):
        if len(args) == 0:
            return False
        expression = "".join(args)
        result = requests.get("http://api.mathjs.org/v1/" + expression, params={'expr': expression})
        await client.send_message(message.channel , content=result.text)
        return True
