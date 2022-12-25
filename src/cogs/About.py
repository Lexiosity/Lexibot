# imports dependencies
import discord 
from discord.ext import commands 

# Defines the class as a cog command and defines variables
class About(commands.Cog):
    def __init__(self, client):
        self.client = client 
        
  # tells the server to print "About.py is ready!" when the cog is working
    @commands.Cog.listener()
    async def on_ready(self):
        print("About.py is ready!")
        
  # Defines what !about would do.
    @commands.command()
    async def about(self, ctx):
        embed1=discord.Embed(title="About LinkBot", color=discord.Color.dark_green())
        embed1.set_thumbnail(url=self.client.user.avatar)
        embed1.add_field(name="What is LinkBot", value=f"I am a bot specifically designed for {ctx.guild.name}. I can do fun things, like be a magic 8ball with !8ball. I can also tell you my latency! I am also able to help with moderation!", inline=False)
        embed1.add_field(name="How is LinkBot made?", value="I was made with python, using Discord.py! I was also created by LinkexaHy. My source code will be found at <no-url-specified>.")
        embed1.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        
        await ctx.send(embed=embed1)

# Adds the cog to the client
async def setup(client):
    await client.add_cog(About(client))
