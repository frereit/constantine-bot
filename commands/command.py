class Command:
    """All commands extend from this class, but the class should never be used as object"""

    def __init__(self, aliases, shortdescription, longdescription, usage, category):
        self.aliases = aliases
        self.shortdescription = shortdescription
        self.longdescription = longdescription
        self.usage = usage
        self.category = category

    # Used for quick formatting for !help without arguments
    def getshortinfo(self):
        return self.usage + " - " + self.shortdescription

    # This is sent to discord when the usage is wrong.
    def get_wrong_usage(self):
        return "Wrong usage! Usage: " + self.usage

    # Execute method template
    async def execute(self , client , message , args , **kwargs):
        pass
