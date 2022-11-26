from nextcord.ext import commands, application_checks
import nextcord

class Tickets(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name="ticket", description="Create a ticket")
  @application_checks.has_guild_permissions(manage_channels=True)
  async def ticket(self, inter: nextcord.Interaction):
    embed = nextcord.Embed(title='Ticket', description='React to this message to create a ticket', color=nextcord.Color.blurple())
    msg = await inter.response.send_message(embed=embed)
    f = await msg.fetch()
    await f.add_reaction('🎟️')

  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    if payload.member.bot:
      return
    if payload.emoji.name == '🎟️':
      guild = self.bot.get_guild(payload.guild_id)
      channel = await guild.create_text_channel(f'ticket-{payload.member.name}', category=nextcord.utils.get(guild.categories, name='🎟・Tickets'))
      await channel.set_permissions(payload.member, read_messages=True, send_messages=True)
      embed = nextcord.Embed(title='Ticket', description=f'{payload.member.mention}\'s ticket\nClick on ❌ to close the ticket', color=nextcord.Color.blurple())
      msg = await channel.send(embed=embed)
      await msg.add_reaction('❌')
    elif payload.emoji.name == '❌':
      # check if the channel is a ticket
      channel = self.bot.get_channel(payload.channel_id)
      if channel.name.startswith('ticket-'):
        await channel.delete()

def setup(bot):
  bot.add_cog(Tickets(bot))