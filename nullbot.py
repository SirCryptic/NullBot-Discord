import discord
from discord.ext import commands
import subprocess
import os
import re

data = {
    "prefix": "!" # or whatever prefix you want to use
}

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix=data['prefix'], intents=intents)
def sanitize(input_str):
    return re.sub('[^A-Za-z0-9\.\-]', '', input_str)
@client.event
async def on_ready():
    print('Bot is ready!')

@client.event
async def on_message(message):
    args = message.content.split(" ")
    if args[0] == data['prefix'] + 'console':
        if args[1] == 'help':
            await message.channel.send("List of available commands: \n"
				"-----------------------------------------------------------------------\n"
                + data['prefix'] + "console nmap - Detect OS & Find Open Ports On A Host\n"
                "-----------------------------------------------------------------------\n"
                "NullBot Beta v1.0.0 Developed By: [ SirCryptic ] - [ NullSecurityTeam ]\n")
            # add any other commands here
        elif args[1] == 'nmap':
            sanitizedInput1 = sanitize(args[2])
            output = subprocess.check_output(["nmap", sanitizedInput1]).decode()
            await message.channel.send(output)
        elif args[1] == 'nikto -h':
            sanitizedInput2 = sanitize(args[2])
            output = subprocess.check_output(["nikto", sanitizedInput2]).decode()
            await message.channel.send(output)
        # add any other commands here

client.run('place_your_bot_token_here')
