#Most of this code is written by Yung
#Some of this code was pulled from: https://github.com/DarthJahus/MinecraftServerStatus-Discord

#Minecraft Server Pinger and Embed Updator
#Please note that api.mcsrvstat.us only updates every 10 minutes, change the api link and update if you need

import discord, json, requests, time
from datetime import datetime, timezone, timedelta
from asyncio import sleep

with open("config.json", "r") as _f:
    config = json.loads(_f.read())

token= config["discord_bot_token"]
sleep_time = 300
client = discord.Client()

#Enter your servers here
#[<Name>, <IP>, <Show Player Count (True/False)>, <Force Next Line (True/False)]
servers = [
    ["Server Name", "play.yungsn.me", True, False],
    ["My Other Server", "mc.hypixel.net:25565", False, False],
]

#Enter your Embed info here
embedTitle = "My Title"
embedColour = 0xffffff
embedThumbnail = "https://i.imgur.com/U067iC8.jpg"
embedFooterIcon = "https://i.imgur.com/U067iC8.jpg"

async def getAPI(address,i):
    _req = requests.get("https://api.mcsrvstat.us/2/%s" % address)
    if _req.status_code != 200:
        print("Error contacting API : %s" % _req.status_code)
    else:
        _req_json = _req.json()
        print("Contacted API correctly.")

        #server offline
        if not _req_json["online"]:
            print("Server offline")
            servers[i].append(":red_circle: Offline")
        else:
            print("Server online")
            if servers[i][2] == True:
                servers[i].append(":green_circle: Online \n:video_game: Playing: %s" % (_req_json["players"]["online"]))
            else:
                servers[i].append(":green_circle: Online")
            print (servers)
            

@client.event
async def on_ready():
    print('Bot logged in as {0.user}.'.format(client))
    await run()

async def run():
    while True:
        try:
            with open("last_message.id", "r") as _f:
                _embed_message_id = int(_f.read())
                print("Found stored message id %i" % _embed_message_id)
        except:
            _embed_message_id = -1
            print("Nothing stored. Id set to -1.")
        
        for i in range (0,len(servers)):
            await getAPI(servers[i][1],i)

        try:
            _embed=discord.Embed(title=embedTitle, color=embedColour)
            _embed.set_thumbnail(url=embedThumbnail)

            for i in range (0,len(servers)):
                if servers[i][3] == False:
                    _embed.add_field(name=servers[i][0], value=servers[i][4], inline=True)
                    servers[i].pop(4)
                elif servers[i][3] == True:
                    _embed.add_field(name="\u200b", value="\u200b", inline=False)
                    _embed.add_field(name=servers[i][0], value=servers[i][4], inline=True)
                    servers[i].pop(4)


            _embed.set_footer(text="Refreshed @ %s, Powered by YungCZ.com" % datetime.strftime(datetime.now(tz=timezone(timedelta(hours=1))), "%H:%M:%S"), icon_url= embedFooterIcon)

        except Exception as e: print(e)



        if _embed_message_id == -1:
            try:
                print("Creating and sending message.")
                _channel = client.get_channel(config["discord_channel_id"])
                _embed_message = await _channel.send(embed=_embed)
                _embed_message_id = _embed_message.id
                print("Message created correctly.")
            except:
                print("Error: Could not send message to channel.")
        else:
            try:
                print("Getting old message with id %i" % _embed_message_id)
                _channel = client.get_channel(config["discord_channel_id"])
                _embed_message = await _channel.fetch_message(_embed_message_id)
                print("Editing the old message...")
                await _embed_message.edit(embed=_embed)
                print("Edited the old message correctly.")
            except discord.errors.NotFound:
                print("Could not find message to edit.")
                _embed_message_id = -1
            except discord.errors.Forbidden:
                # You do not have the permissions required to get a message.
                print("Error: Please, allow the bot to view ancient messages.")
                _embed_message_id = -1
        try:
            with open("last_message.id", "w") as _f:
                _f.write(str(_embed_message_id))
            print("Message data saved correctly.")
        except:
            print("Could not save data.")
            pass

        await sleep(sleep_time)


client.run(token)



