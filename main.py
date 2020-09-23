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
    await client.change_presence(status=discord.Status.offline)
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
        await message.channel.send("my mentality")
    if ("you are no longer cursed" in message.content) and (message.mentions != []) and (message.author == client.user):
        cursed = 0

@client.event
async def on_member_update(before, after):
    
    dead = discord.utils.get(after.guild.roles, id = 714535509279637525)
    curse = discord.utils.get(after.guild.roles, id = 750130819099656284)
    general = discord.utils.get(after.guild.channels, id = 712716066618605591)
    
    if after.id == my_id:
        #linking status
        try:
            if after.activity.name == "Spotify":
                await client.change_presence(status=after.status, activity=discord.Activity(name=after.activity.name, type=discord.ActivityType.listening))
            elif after.activity.type == discord.ActivityType.streaming:
                await client.change_presence(status=after.status, activity=discord.Activity(name=after.activity.name, url=after.activity.url, type=discord.ActivityType.streaming))
            else:
                await client.change_presence(status=after.status, activity=after.activity)
        except AttributeError or IndexError:
            await client.change_presence(status=after.status, activity=after.activity)
        #this reality
        try:
            if dead in after.roles:
                await general.send(f"{curse.members[0].mention} you are no longer cursed")
                await curse.members[0].remove_roles(curse,reason="not cursed")
        except IndexError:
            return
            

client.run(token)
