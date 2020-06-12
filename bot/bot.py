# bot.py

DEBUG = False

#os access
import os

# discord bot api
import discord
# enviromental variables importer
from dotenv import load_dotenv
# make api requests to minecraft-api
import requests

#thing to identify commands on server
PREFIX = '!'

load_dotenv(verbose=True)
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# register an event handler
@client.event
async def on_message(message):

    # ignore myself
    if (message.author == client.user):
        return

    if (message.content.startswith(PREFIX)):

        if DEBUG:
            print(" -- RECEIVED COMMAND -- ")
            print("Channel Catagory:")
            print(message.channel.category)

        # minecraft
        if (message.channel.category.name == "minecraft"):

            if DEBUG:
                print("MINECRAFT COMMAND")

            # minecraft whitelist command
            if message.content.startswith(PREFIX + 'whitelist'):
                # add to list
                if message.content.startswith(PREFIX + 'whitelist add'):

                    #get the list of users to add
                    uname = message.content.split('add ', 1)[1]

                    # make the request to minecraft api
                    r = requests.get("http://" + message.channel.name + ".root.cturtle98.com:8080/whitelist/add/?u=" + uname)

                    if r.ok:
                        await message.channel.send(message.author.mention + " those user(s) should now be on the whitelist")
                    else:
                        await message.channel.send(message.author.mention + " ERROR! Please contact Ciaran!")
                
                else:
                    await message.channel.send(message.author.mention + " Usage: !whitelist add <username. ~~ OR whitelist remove <username> ~~")

    else:
        return

client.run(TOKEN)