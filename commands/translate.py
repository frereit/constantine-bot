import json
from yandex_translate import YandexTranslate
from category import Category
from commands.command import Command


class Translate(Command):
    def __init__(self):
        self.name = "translate"
        self.shortdescription = "Quickly translate stuff"
        self.longdescription = "Translate a string into another language. The command uses the free Yandex Translate " \
                               "API: https://translate.yandex.com/. Works best with single words. "
        self.usage = "!translate <detect|<lang (e.g. de-en)>|available> [text]"
        self.category = Category.UTIL
        with open('config.json') as data_file:
            config = json.load(data_file)
        self.yandexkey = config['yandexkey']
        self.translate = YandexTranslate(self.yandexkey)
        super().__init__(self.name , self.shortdescription , self.longdescription , self.usage , self.category)

    async def execute(self , client , message , args , **kwargs):
        if len(args) < 1:
            await client.send_message(message.channel, content=self.get_wrong_usage())
            return False

        if args[0] == 'available':
            if not len(args) == 1:
                await client.send_message(message.channel, content=self.get_wrong_usage())
                return False
            else:
                await client.send_message(message.channel , content="Available translate directions: \n```"
                                                                    + ",".join(self.translate.directions) + "```")
                return True

        if args[0] == 'detect':
            args.pop(0)
            await client.send_message(message.channel, content="'" + " ".join(args) + "' seems to be " + self.translate.detect(" ".join(args)))
            return True

        lang = args.pop(0)
        text = " ".join(args)
        translated = self.translate.translate(text=text, lang=lang)
        translation = translated['text'][0]
        await client.send_message(message.channel, content=translation)
        return True

