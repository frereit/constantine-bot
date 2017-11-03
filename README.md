# Constantine

Constantine is an open-source multifunctional [Discord](https://discordapp.com/) Bot written in [Python](https://www.python.org/).

  - Music Player (Planned)
  - ToDo List and Reminders (Planned)
  - Voting (Planned)

# Usage

>Core
>!ping - Sends 'Pong' back
>!say/send_message <Text> - Makes the bot say whatever you want.
>!help [command] - Lists all commands.
>Utilities
>!translate/alias2/alias3 <detect|<lang (e.g. de-en)>|available> [text] - Quickly translate stuff

### Tech

Constantine uses the following libaries and APIs:
  - [pipreqs](https://github.com/bndr/pipreqs) - Quickly creating requirements.txt files for specific projects.
  - [Discord.py](https://github.com/Rapptz/discord.py) - Discord API Wrapper for Python

### Installation

Clone [this repository](https://github.com/frereit/constantine-bot) using 
```
git clone https://github.com/frereit/constantine-bot.git
cd constantine-bot
```
Install required libaries:
```
pip install -r requirements.txt
```
Create a new [Discord App](https://discordapp.com/developers/applications/me/create) and create a Bot User.

Configure your Client ID, Client Secret, Username (NOT your discord username, the username of the bot!) and Token using your favourite text editor in config.json.

Run the bot:
```
python constantine.py
```

### FAQ

>WIP

### Contributing
##### Found a bug in the code? Have a great idea for a feature or just want to refactor our code? GREAT!

Feel free to fork the repository and request a pull request. If you plan on doing greater changes, please contact us BEFORE starting coding your changes, we just want to avoid any wasted time, maybe we are working on the same thing and we can cooperate or we don't approve the feature and wouldn't accept the pull request.

License
----

[GNU General Public License v3.0](https://github.com/frereit/constantine-bot/blob/develop/LICENSE)
