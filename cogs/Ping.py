# imports dependencies
import discord 
from discord.ext import commands 

# Defines the class as a cog command and defines variables
class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client 
        
  # tells the server to print "Ping.py is ready!" when the cog is working
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping.py is ready!")
        
  # Defines what !ping would do. In this case, it will return with "Pong! <latency>ms"
    @commands.command()
    async def Ping(self, ctx):
        bot_latency = round(self.client.latency * 1000)
        embed = discord.Embed(description=f"The bot latency is **{bot_latency}** ms", color=ctx.author.color)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        
        await ctx.send(embed=embed)

# Adds the cog to the client
async def setup(client):
    await client.add_cog(Ping(client))