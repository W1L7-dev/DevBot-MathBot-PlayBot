from dotenv import load_dotenv
from nextcord.ext import commands
import nextcord
import os

class OnMemberLeaving(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    load_dotenv()

  @commands.Cog.listener()
  async def on_member_remove(self, member):
    channel = self.bot.get_channel(1021584271871311933)
    embed = nextcord.Embed(title="Goodbye", description=f"Goodbye, {member.mention}!", color=nextcord.Color.blurple())
    await channel.send(embed=embed)

def setup(bot):
  bot.add_cog(OnMemberLeaving(bot))