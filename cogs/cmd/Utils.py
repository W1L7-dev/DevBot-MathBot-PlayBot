from nextcord.ext import commands
import nextcord

class Utils(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name="ping", description="Get the bot's latency")
  async def ping(self, inter: nextcord.Interaction):
    embed = nextcord.Embed(title=f'Pong! **{round(self.bot.latency * 1000)}**ms', color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="say", description="Make the bot say something")
  async def say(self, inter: nextcord.Interaction, message: str):
    await inter.response.send_message(message)

  @nextcord.slash_command(name="embed", description="Make the bot send an embed")
  async def embed(self, inter: nextcord.Interaction, title: str, message: str):
    embed = nextcord.Embed(title=title, description=message, color=nextcord.Color.random())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="nick", description="Change your nickname")
  async def nick(self, inter: nextcord.Interaction, nickname: str):
    await inter.user.edit(nick=nickname)
    embed = nextcord.Embed(f'Nickname changed to **{nickname}**', color=nextcord.Color.green())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="resetnick", description="Reset your nickname")
  async def resetnick(self, inter: nextcord.Interaction):
    await inter.user.edit(nick=None)
    embed = nextcord.Embed(description='Nickname reset', color=nextcord.Color.green())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="avatar", description="Get a user's avatar")
  async def avatar(self, inter: nextcord.Interaction, member: nextcord.Member=nextcord.SlashOption(required=False)):
    if member is None:
      member = inter.user
    embed = nextcord.Embed(title=f'**{member.name}**\'s avatar', color=nextcord.Color.blurple())
    embed.set_image(url=member.avatar.url)
    await inter.response.send_message(embed=embed)

def setup(bot):
  bot.add_cog(Utils(bot))