# imports of dependencies
import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import os
import asyncio

# Defines the prefix and intents of the bot
client = commands.Bot(command_prefix="!", intents=discord.Intents.all(), case_insensitive=True)

# cycles through an array of bot statuses
bot_status = cycle(["Subscribe to LinkexaHy on YouTube!", "LinkBot | !help", "with LinkexaHy", "Follow LinkexaHy on all socials!"])

# loops around the bot statuses after reaching last status
@tasks.loop(minutes=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

# Outputs "Bot is working" in console when the bot is online, and starts the status loop.
@client.event
async def on_ready():
    print("Bot is working")
    change_status.start()

# Tells the server what to look for when loading cogs.
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
        
# loads the client and starts the bot.
async def main():
    async with client:
        await load()
        await client.start("MTA1NTUwOTM5NTc3NTE2NDQ0Ng.GK3IHd.jJAhiAW3TcYen-p14r7NimdN6XrZkMCyMnvG4M")

# Starts running the variable, main
asyncio.run(main())
