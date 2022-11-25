from nextcord.ext import commands

class OnBotMention(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if self.bot.user.mentioned_in(message):
      await message.channel.send(f"Hello! I'm PlayBot, a music bot. I use the slash commands")

def setup(bot):
  bot.add_cog(OnBotMention(bot))