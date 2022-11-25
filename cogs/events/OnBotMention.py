from nextcord.ext import commands
import nextcord

class OnBotMention(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if self.bot.user.mentioned_in(message):
      embed = nextcord.Embed(title="Bot Mentioned", description=f"Hello! I'm **__DevBot__**! I use the new **Slash Commands**!", color=nextcord.Color.blurple())
      await message.channel.send(embed=embed)

def setup(bot):
  bot.add_cog(OnBotMention(bot))