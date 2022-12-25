# imports dependencies
import discord 
from discord.ext import commands 
import asyncio

# Defines the class as a cog command and defines variables
class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client 
        
  # tells the server to print "Template.py is ready!" when the cog is working
    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation.py is ready!")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,count: int):
        await ctx.channel.purge(limit=count)
        clear_message = await ctx.send(f"{count} message(s) have been sent to the Sacred Realm! {ctx.guild.name} is safe again!")
        channel = self.client.get_channel(1040181540811972729)
        await channel.send(f"**{count}** message(s) have been cleared in {ctx.channel.mention}.")
        await asyncio.sleep(5)
        await clear_message.delete()
        
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member, *, modreason):
        await ctx.guild.kick(member)
        
        conf_embed=discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Kicked", value=f"{member.mention} has been kicked from {ctx.guild.name} by {ctx.author.mention}.", inline=False)
        conf_embed.add_field(name="Reason", value=modreason, inline=False)
        
        channel=self.client.get_channel(1040181540811972729)
        conf_message=await ctx.send(embed=conf_embed)
        await channel.send(f"**{member.name}** has been kicked from the server")
        await asyncio.sleep(5)
        await conf_message.delete()
        

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, modreason):
        await ctx.guild.ban(member)
        
        ban_conf_embed=discord.Embed(title="Success!", color=discord.Color.green())
        ban_conf_embed.add_field(name="Banned", value=f"{member.mention} has been banished to the Sacred Realm by {ctx.author.mention}. Now {ctx.guild.name} is safe once again!", inline=False)
        ban_conf_embed.add_field(name="Reason", value=modreason, inline=False)
        
        channel=self.client.get_channel(1040181540811972729)
        ban_conf_message=await ctx.send(embed=ban_conf_embed)
        await channel.send(f"**{member.name}** has been banned from the server")
        await asyncio.sleep(5)
        await ban_conf_message.delete()
        
    @commands.command(name="unban")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userId):
        user = discord.Object(id=userId)
        await ctx.guild.unban(user)
        
        unban_conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        unban_conf_embed.add_field(name="Unbanned", value=f"<@{userId}> has been unbanned by {ctx.author.mention}.", inline=False)
        
        channel=self.client.get_channel(1040181540811972729)
        unban_conf_msg=await ctx.send(embed=unban_conf_embed)
        await channel.send(f"**{userId}** has been unbanned on the server.")
        await asyncio.sleep(5)
        await unban_conf_msg.delete()

# Adds the cog to the client
async def setup(client):
    await client.add_cog(Moderation(client))
