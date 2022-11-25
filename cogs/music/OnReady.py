from nextcord.ext import commands
import nextcord

class OnReady(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print(f"Logged in as {self.bot.user} (ID: {self.bot.user.id})")
    print("------")
    await self.bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name="Your music"))

def setup(bot):
  bot.add_cog(OnReady(bot))