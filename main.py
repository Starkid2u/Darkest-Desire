#!/usr/bin/env/str python3

from time import sleep
import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import random

with open("tokenfile", "r") as tokenfile:
    token=tokenfile.read()


async def attachments_to_files(attached,spoiler=False):
    filelist = []
    for i in attached:
        file = await i.to_file()
        filelist.insert(len(filelist),file)
    return filelist
    
my_id = 347198887309869078


client = discord.Client()

@client.event
async def on_ready():
    print('hello world')

curser = 0
cursevictim = 0 
cursed = 0
@client.event
async def on_message(message):

    curse = discord.utils.get(message.guild.roles, id = 750130819099656284)
    dead = discord.utils.get(message.guild.roles, id = 714535509279637525)

    #this reality code
    global cursed
    global cursevictim
    global curser
    if message.content.startswith("this reality"):
        if cursed == 1:
            return
        await message.mentions[0].add_roles(curse,reason="cursed")
        cursed = 1
        cursevictim = message.mentions[0]
        curser = message.author
        await message.channel.send("my mentality")
    if cursed == 1:
        if dead in cursevictim.roles or dead in curser.roles:
            await message.channel.send(f"{message.mentions[0].mention} you are no longer cursed")
            await cursevictim.remove_roles(curse,reason="not cursed")
            cursed = 0
            cursevictim = 0
            curser = 0
            return


client.run(token)