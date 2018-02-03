import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = ".fg")


@client.event
async def on_ready():
    print("Bot is online and connected to Discord!")
    #else:
    #print("The was a problem somewhere, please try again!")

@client.event
async def on_message(message) :
    if message.content.upper().startswith('.fg play'):
        await client.send_message(message.channel, ".pl https://youtu.be/8QckszO77Pw")
        await client.send_message(message.channel, "ha ha :laughing: dont troll with me!!!")




client.run("NDA4NzA5MjI0NDIwNDc0ODgw.DVYXXA.pDvezrLBWG70WaA8g0PhgnipbcU")
