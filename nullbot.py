import discord
from discord.ext import commands
import subprocess
import os
import re
import ipaddress
import socket

data = {
    "prefix": "!" # or whatever prefix you want to use
}

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix=data['prefix'], intents=intents)

def sanitize(input_str):
    return re.sub('[^A-Za-z0-9\.\-]', '', input_str)

def is_authorized(user):
    authorized_roles = ["Root", "Moderator","NullBot User"] # Replace with your own authorized roles
    for role in user.roles:
        if role.name in authorized_roles:
            return True
    return False

@client.event
async def on_ready():
    print('Bot is ready!')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    args = message.content.split(" ")
    if args[0] == data['prefix'] + 'console':
        if args[1] == 'help':
            await message.channel.send("List of available commands: \n"
                "-----------------------------------------------------------------------\n"
                + data['prefix'] + "console nmap - Detect OS & Find Open Ports On A Host\n"
                + data['prefix'] + "console nikto - Scan a web server for vulnerabilities\n"
                "-----------------------------------------------------------------------\n"
                "NullBot Beta v1.0.0 Developed By: [ SirCryptic ] - [ NullSecurityTeam ]\n")
        elif args[1] == 'nmap':
            if not is_authorized(message.author):
                await message.channel.send("You are not authorized to run this command.")
                return
            sanitizedInput = sanitize(args[2])
            try:
                ip = ipaddress.ip_address(sanitizedInput)
                if ip.is_loopback or ip.is_link_local:
                    await message.channel.send("Scanning localhost and link-local addresses is not allowed.")
                    return
                host = ipaddress.ip_network('10.0.0.0/8')
                if ip in host:
                    await message.channel.send("Scanning addresses within the host machine's network is not allowed.")
                    return
            except ValueError:
                await message.channel.send("Invalid IP address.")
                return
            command = f"sudo nmap -O {sanitizedInput}"
            output = subprocess.check_output(command, shell=True).decode()
            await message.channel.send(output)
        elif args[1] == 'nikto':
            if not is_authorized(message.author):
                await message.channel.send("You are not authorized to run this command.")
                return
            sanitizedInput = sanitize(args[2])
            try:
                ip = ipaddress.ip_address(sanitizedInput)
                if ip.is_loopback or ip.is_link_local:
                    await message.channel.send("Scanning localhost and link-local addresses is not allowed.")
                    return
                host = ipaddress.ip_network('10.0.0.0/8')
                if ip in host:
                    await message.channel.send("Scanning addresses within the host machine's network is not allowed.")
                    return
            except ValueError:
                await message.channel.send("Invalid IP address.")
                return
            command = ["nikto", "-h", sanitizedInput]
            output = subprocess.check_output(command).decode()
            await message.channel.send(output)

client.run('your_bot_token')
