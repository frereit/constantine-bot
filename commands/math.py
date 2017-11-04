from category import Category
from commands.command import Command
import numexpr


class Math(Command):
    def __init__(self):
        aliases = ['math' , 'calculate']
        shortdescription = "Evaluates math expressions."
        longdescription = 'This command evaluates a user-specified mathematical expression using the free MathJS API. ' \
                          'http://api.mathjs.org/. Supported constants (10 digits): pi, e '
        usage = "/".join(aliases) + " <expression>"
        category = Category.UTIL
        super().__init__(aliases , shortdescription , longdescription , usage , category)

    @staticmethod
    def replace_constant_variables(expression):
        expression = expression.replace("pi" , "3.1415926536")
        expression = expression.replace("e" , "2.7182818285")
        return expression

    @staticmethod
    def replace_constant_numbers(expression):
        expression = expression.replace("3.1415926536", "π")
        expression = expression.replace("2.7182818285", "e")
        return expression

    async def execute(self , client , message , args , **kwargs):
        if len(args) == 0:
            return False
        expression = "".join(args)
        expression = self.replace_constant_variables(expression)
        try:
            result = numexpr.evaluate(expression)
            await client.send_message(message.channel , content=self.replace_constant_numbers(expression) + " = " + str(result))
        except Exception:
            await client.send_message(message.channel , content=expression + " isn't a valid expression")
        return True
