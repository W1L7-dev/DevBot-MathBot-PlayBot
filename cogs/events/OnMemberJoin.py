from dotenv import load_dotenv
from nextcord.ext import commands
import nextcord
import os

class OnMemberJoin(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    load_dotenv()

  @commands.Cog.listener()
  async def on_member_join(self, member):
    channel = self.bot.get_channel(1021583945143423117)
    embed = nextcord.Embed(title="Welcome", description=f"Welcome to the server, {member.mention}!", color=nextcord.Color.blurple())
    role = nextcord.utils.get(member.guild.roles, name="✅・members")
    await channel.send(embed=embed)
    await member.add_roles(role)

def setup(bot):
  bot.add_cog(OnMemberJoin(bot))