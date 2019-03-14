# Work with Python 3.6
# This bot is based on sample code provided by devdungeon.
# https://www.devdungeon.com/content/make-discord-bot-python
import discord
from requests import get

import subprocess

client = discord.Client()

USERID = '<@504121415360839680>'

Quitstate = False
Prog = []

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    if message.content.startswith(USERID):
        msg = message.content[len(USERID):].lstrip()
        print(msg)

        global Quitstate
        global Prog
        if Quitstate:
            if msg.startswith('Yes'):
                print(Quitstate)
                await client.logout()
            else:
                Quitstate = False
        if msg.startswith('ip'):
                msg = get('https://api.ipify.org/').text
                await client.send_message(message.channel, msg)
        if msg.startswith('testrun'):
                Prog = subprocess.Popen(['C:\\Windows\\System32\\calc.exe'])
                msg = "calculator started"
                await client.send_message(message.channel, msg)
        if msg.startswith('testkill'):
                Prog.terminate()
                msg = "calculator stopped"
                await client.send_message(message.channel, msg)
        if msg.startswith('teststatus'):
                if None == Prog.poll():
                    msg = "calculator running"
                else:
                    msg = "calculator stopped"
                await client.send_message(message.channel, msg)
        
        if msg.startswith('quit'):
                await client.send_message(message.channel, "Are you sure? \'Yes\' to confirm")
                Quitstate = True

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

file = open("Seantoken.txt", "r")
client.run(file.read())
file.close()
