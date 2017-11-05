import wikipedia
from category import Category
from commands.command import Command

class Wiki(Command):

    def __init__(self):
        aliases = ["wikipedia", "wiki"]
        shortdescription = "A command that shows the most relevant Wikipedia article"
        longdescription = "A command that shows the most relevant Wikipedia article"

        usage = "/".join(aliases)
        category = Category.UTIL
        super().__init__(aliases, shortdescription, longdescription, usage, category)

    async def execute(self, client, message, args, **kwargs):
        if len(args) == 0:
            return False

        userInput = args
        search = wikipedia.page(userInput)
        pagetitle = search.title
        pageURL = search.url
        pageSummary =  wikipedia.summary(userInput, sentences=1)