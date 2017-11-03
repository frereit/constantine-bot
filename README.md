# Constantine

Constantine is an open-source multifunctional [Discord](https://discordapp.com/) Bot written in [Python](https://www.python.org/).

  - Music Player (Planned)
  - ToDo List and Reminders (Planned)
  - Voting (Planned)

# Usage

  - !help [command] - Everyone knows what this does.
  - !ping - Responds with "Pong!"
  - !say <Text> - Responds with user-specified text
  - !translate <detect|<lang>|available> [text]- Available returns all available languages. Detect tries to detect what language a user-specified text is written in. <lang> is the language the user would like to translate into. Example command: "!translate de-en Hallo, wie geht es dir?" will return "Hello, how are you?". If no input language is specified it tries to detect the language. From my experience one word translations work best. This command uses the free [Yandex Translator API](https://translate.yandex.com/)
  - !news <[source (default: google-news)]|info|available> [source] - Available returns all available news sources. info [source] returns details about the specified source. !news [source] will return the top ten articles, a short description and a link on the specified news site. If no news site is specified, Google News will be used because it puts together news from different sites.

### Tech

Constantine uses the following libaries and APIs:
  - [pipreqs](https://github.com/bndr/pipreqs) - Quickly creating requirements.txt files for specific projects.
  - [Discord.py](https://github.com/Rapptz/discord.py) - Discord API Wrapper for Python

### Installation

##### Part 1: Download
Clone [this repository](https://github.com/frereit/constantine-bot) using 
```
git clone https://github.com/frereit/constantine-bot.git
cd constantine-bot
```
Download required libaries:
```
pip install -r requirements.txt
```

##### Part 2: Creating the Bot
Create a new [Discord App](https://discordapp.com/developers/applications/me/create) and create a Bot User. You can add the bot to your server by modifing this url: 
`https://discordapp.com/oauth2/authorize?&client_id=[BOT ID]`
You can find your bot id in the Bot User Settings.

Open config.json and configure all properties. Get the YandexKey [here](https://tech.yandex.com/translate/) and the NewsKey [here](https://newsapi.org). The Discord Token can be found in the settings of the bot user [here](https://tech.yandex.com/translate/).

##### Part 3: Starting the bot

If nothing went wrong start the bot:
```
python constantine.py
```
and after a little time you should see 
```
Logged in as
[USERNAME]
[ID]
```
pop up in your console. Your bot is now online! If you encouter any erorrs feel free to open an issue!

### FAQ

>WIP

### Contributing
##### Found a bug in the code? Have a great idea for a feature or just want to refactor our code? GREAT!

Feel free to fork the repository and request a pull request. If you plan on doing greater changes, please contact us BEFORE starting coding your changes, we just want to avoid any wasted time, maybe we are working on the same thing and we can cooperate or we don't approve the feature and wouldn't accept the pull request.

License
----

[GNU General Public License v3.0](https://github.com/frereit/constantine-bot/blob/develop/LICENSE)
