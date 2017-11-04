import json  # JSON De/Encoder

import yandex_translate
from yandex_translate import YandexTranslate  # API used for translation
from category import Category  # Category enum with all the categories
from commands.command import Command  # Base class


class Translate(Command):
    def __init__(self):

        # Information about the command
        self.aliases = ["translate"]
        self.shortdescription = "Quickly translate stuff"
        self.longdescription = "Translate a string into another language. The command uses the free Yandex Translate " \
                               "API: https://translate.yandex.com/. Works best with single words. "
        self.usage = "/".join(self.aliases) + " <detect|<lang (e.g. de-en)>|available> [text]"
        self.category = Category.UTIL

        # Get the key from config.json
        with open('config.json') as data_file:
            config = json.load(data_file)
        self.yandexkey = config['yandexkey']

        # Create new Translate instance
        self.translate = YandexTranslate(self.yandexkey)
        super().__init__(self.aliases , self.shortdescription , self.longdescription , self.usage , self.category)

    # Called by CommandHandler when the command is executed
    async def execute(self , client , message , args , **kwargs):
        # We need at least one argument
        if len(args) < 1:
            return False  # Command failed. Handler will print usage.

        # If user wants to see available directions
        if args[0] == 'available':
            # We only need one argument here
            if not len(args) == 1:
                return False  # Too many arguments
            else:
                await client.send_message(message.channel , content="Available translate directions: \n```"
                                                                    + ",".join(self.translate.directions) + "```")
                return True

        if args[0] == 'detect':
            # We only need two arguments here
            if not len(args) >= 2:
                return False  # Not enough arguments. REMEMBER: Each space counts as argument, thus we cant just say
                # exactly two arguments
            args.pop(0)  # Pop 'detect' from argument list to only get the arguments for this sub command
            # Join arguments to text
            text = " ".join(args)
            # Detect language and send it
            await client.send_message(message.channel ,
                                      content="'" + text + "' seems to be " + self.translate.detect(text))
            return True

        # Non of the above => translate using language code
        # Get language code and leave only text behind in args
        lang = args.pop(0)

        if len(args) == 0:
            return False

        # Join the arguments to text
        text = " ".join(args)

        # Translate it and get the text
        try:
            translated = self.translate.translate(text=text , lang=lang)
        except yandex_translate.YandexTranslateException:
            # Notify the user that his lang-code is invalid.
            text = "Whoops! Seems like the language code you supplied is invalid! You can list all available language " \
                   "codes with !translate available "
            await client.send_message(message.channel, content=text)
            return True  # We don't want it to print the syntax

        translation = translated['text'][0]

        # Send the translation
        await client.send_message(message.channel , content=translation)
        return True
