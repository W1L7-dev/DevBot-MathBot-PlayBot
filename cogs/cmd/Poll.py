from nextcord.ext import commands
import nextcord

class Poll(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name="yesno", description="Create a yes-no poll")
  async def yesno(self, inter: nextcord.Interaction, *, question):
    embed = nextcord.Embed(title="Poll", description=question, color=nextcord.Color.blurple())
    embed.set_author(name=inter.author.display_name, icon_url=inter.user.avatar.url)
    embed.set_footer(text=f"Poll ID: {inter.message.id}")
    message = await inter.response.send_message(embed=embed)
    await message.add_reaction("✅")
    await message.add_reaction("❌")

  @nextcord.slash_command(name="poll", description="Create a poll with custom options")
  async def poll(self, inter: nextcord.Interaction, question, *, options: str):
    options = options.split(",")
    if len(options) > 10:
      return await inter.response.send_message(embed=nextcord.Embed(title="You can only have up to 10 options.", color=nextcord.Color.blurple()), ephemeral=True)
    if len(options) < 2:
      return await inter.response.send_message(embed=nextcord.Embed(title="You need at least two options.", color=nextcord.Color.blurple()), ephemeral=True)
    embed = nextcord.Embed(title="Poll", description=question, color=nextcord.Color.green())
    embed.set_author(name=inter.user.name, icon_url=inter.user.avatar.url)
    reactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    for x, option in enumerate(options):
      embed.add_field(name=reactions[x], value=option, inline=False)
    await inter.response.send_message(embed=embed)
    for reaction in reactions[:len(options)]:
      message: nextcord.Message
      async for message in inter.channel.history():
        if not message.embeds:
          continue
        if message.embeds[0].title == embed.title and message.embeds[0].colour == embed.colour:
          vote = message
          break
        else:
          return
      await vote.add_reaction(reaction)

  @nextcord.slash_command(name="pollresult", description="Get the results of a poll")
  async def pollresult(self, inter: nextcord.Interaction, message_id):
    message = await inter.channel.fetch_message(message_id)
    reactions = message.reactions
    embed = nextcord.Embed(title='Poll Results', description=f'**{message.embeds[0].description}**', color=nextcord.Color.blurple())
    embed.set_footer(text=message.embeds[0].footer.text)
    for reaction in reactions:
      percentage = round((reaction.count - 1) / (len(message.reactions) - 1) * 100)
      embed.add_field(name=f'{reaction.emoji}', value=f'{reaction.count - 1}, {percentage}%', inline=True)
    await inter.response.send_message(embed=embed)

def setup(bot):
  bot.add_cog(Poll(bot))