class Command:
    """All commands extend from this class, but the class should never be used as object"""

    def __init__(self, name, shortdescription, longdescription, usage, category):
        self.name = name
        self.shortdescription = shortdescription
        self.longdescription = longdescription
        self.usage = usage
        self.category = category

    def getshortinfo(self):
        return self.usage + " - " + self.shortdescription

    def get_wrong_usage(self):
        return "Wrong usage! Usage: " + self.usage

    async def execute(self , client , message , args , **kwargs):
        pass
