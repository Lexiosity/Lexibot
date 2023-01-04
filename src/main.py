# imports of dependencies
import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import os
import asyncio 
import json

# Defines the prefix and intents of the bot 

def get_server_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)
        
    return prefix[str(message.guild.id)]

client = commands.Bot(command_prefix=get_server_prefix, intents=discord.Intents.all(), case_insensitive=True)

# cycles through an array of bot statuses
bot_status = cycle(["Subscribe to LinkexaHy on YouTube!", "LinkBot | !help", "with LinkexaHy", "Follow LinkexaHy on all socials!"])

# loops around the bot statuses after reaching last status
@tasks.loop(minutes=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

# Outputs "Bot is working" in console when the bot is online, and starts the status loop.
@client.event
async def on_ready():
    await client.tree.sync()
    print("Bot is working")
    change_status.start()
    
@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)
        
    prefix[str(guild.id)] = "lk!"
    
    with open("prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)
        
@client.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)

    prefix.pop(str(guild.id))
    
    with open("prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)
        
@client.command()
async def setprefix(ctx, *, newprefix: str):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)
    
    prefix[str(ctx.guild.id)] = newprefix
    
    with open("prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)
    
# Tells the server what to look for when loading cogs.
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
        
# loads the client and starts the bot.
async def main():
    async with client:
        await load()
        await client.start("MTA1NTUwOTM5NTc3NTE2NDQ0Ng.GyLYQg.oewqWUPa--Wwde3ZSlBP203CbB0oW3_zFw0lRs")

# Starts running the variable, main
asyncio.run(main())
