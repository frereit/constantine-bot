class Command:
    """All commands extend from this class, but the class should never be used as object"""

    def __init__(self, name, shortdescription, longdescription, usage, category):
        self.name = name
        self.shortdescription = shortdescription
        self.longdescription = longdescription
        self.usage = usage
        self.category = category

    def getshortinfo(self):
        return self.name + " - " + self.shortdescription

    def getfullinfo(self):
        return self.longdescription + "\n" + "Usage: " + self.usage + "\n" + "Category: " + self.category

    def getcategory(self):
        return self.category

    def execute(self, client, channel, args):
        pass
