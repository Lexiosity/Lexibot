# imports dependencies
import discord 
from discord.ext import commands 
import random

# Defines the class as a cog command and defines variables
class Eightball(commands.Cog):
    def __init__(self, client):
        self.client = client 
    
    # Tells the server to print "eightball.py is ready!
    @commands.Cog.listener()
    async def on_ready(self):
        print("eightball.py is ready!")
        
    # Defines what !eightball/!8ball/!magic_eightball will do. In this case, it will take a random line from the responses.txt file and send it in response to !eightball/!8ball/!magic_eightball
    @commands.command(aliases=["8ball", "eightball"])
    async def magic_eightball(self, ctx, *, question):
        with open("./cogs/eightball/responses.txt", "r") as f:
            random_responses = f.readlines()
            response = random.choice(random_responses)
            await ctx.send(response)

# Adds the cog to the client
async def setup(client):
    await client.add_cog(Eightball(client))
