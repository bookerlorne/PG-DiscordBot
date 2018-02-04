import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    print("Bot is online and connected to Discord!")
    #else:
    #print("The was a problem somewhere, please try again!")

@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")

@client.event
async def on_message(message) :
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!SAY'):
        if message.author.id == "350237851331330048":
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You do not have the appropriate permissions. :smile:")

    if message.content.upper().startswith('!AMIADMIN'):
        if "398377706984701953" in [role.id for role in message.author.roles]:
            userID = message.author.id
            await client.send_message(message.channel, "You are a admin!")
        else:
            await client.send_message(message.channel, "You are not a admin, sorry!")

    if message.content.upper().startswith('!JOKE'):
        await client.send_message(message.channel, "Here's one...")
        await client.send_message(message.channel, "I was coded by Lorne, you think I can tell jokes :laughing:")

    if message.content.upper().startswith('!HELP'):
        await client.send_message(message.channel, "Please go to the tech support channel for further help.s")

    if message.content.upper().startswith('!HI'):
        await client.send_message(message.channel, "Hey... :smile:")

    if message.content.upper().startswith('!SPAM'):
            await client.send_message(message.channel, "Please enter !BANPERSON {Spammer's name}, and...{reason for tempoary ban}")

    if message.content.upper().startswith('?HeyPeter'):
            await client.send_message(message.channel, "Why hello there!")

    if message.content.upper().startswith('!TSPINME'):
        await client.send_message(message.channel, "Please use this chat for Discord help only.")
        await client.send_message(message.channel, "This chat must not be used for general chatting go to the general channel for that.")

client.run("NDA4NzA5MjI0NDIwNDc0ODgw.DVeFZw.fovx5CitAgkpdtSrSD4WSYHdNto")
