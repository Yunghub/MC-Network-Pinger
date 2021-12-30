# Minecraft Network Pinger, Discord Embed

Sends a Discord embed to the channel of your choice for network monitoring

## Installation

Install all of the required packages on requirements.txt

```bash
# Windows
pip install -r requirements.txt
```

Then configure your bot in both your config.js and main.py
```python
# Main.py
token= config["discord_bot_token"]
client = discord.Client()

#Enter your servers here
#[<Name>, <IP>, <Show Player Count (True/False)>, <Force Next Line (True/False)]
servers = [
    ["Server Name", "play.yungsn.me", True, False],
    ["My Other Server", "mc.hypixel.net:25565", False, False],
]

#Enter your Embed info here
sleep_time = 5 # API caches every 10 minutes anyways...
embedTitle = "My Title"
embedColour = 0xffffff
embedThumbnail = "https://i.imgur.com/U067iC8.jpg"
embedFooterIcon = "https://i.imgur.com/U067iC8.jpg"
activityServerIndex = 0 #Which index of server for your bots activity
activityTwitchURL = "https://www.twitch.tv/yung_streams" #Has to be a valid URL otherwise Discord will silent ignore
```
```json
// config.json
{
  "discord_bot_token": "YourTokenHere",
  "discord_channel_id": 694206942069420
}
```


## Usage
Run the main.py when you have configured both of the files.

![image](https://user-images.githubusercontent.com/59136907/147694608-20414ce6-671c-41be-af07-35a78d756c45.png)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

