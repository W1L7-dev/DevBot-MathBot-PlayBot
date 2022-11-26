from nextcord.ext import commands, application_checks
import nextcord

class RoleReact(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name="rolereact", description="Create a role reaction message")
  @application_checks.has_guild_permissions(manage_channels=True)
  async def rolereact(self, inter: nextcord.Interaction):
    embed = nextcord.Embed(title='Role Reaction', description='React to this message to get a role', color=nextcord.Color.blurple())
    embed.add_field(name='🎮', value='Game Dev', inline=True)
    embed.add_field(name='🌎', value='Web', inline=True)
    embed.add_field(name='📱', value='Mobile', inline=True)
    embed.add_field(name='🐍', value='Scripting', inline=True)
    embed.add_field(name='🖥️', value='OS', inline=True)
    embed.add_field(name='📚', value='JVM', inline=True)
    embed.add_field(name='📊', value='Shell', inline=True)
    msg = await inter.response.send_message(embed=embed)
    f = await msg.fetch()
    await f.add_reaction('🎮')
    await f.add_reaction('🌎')
    await f.add_reaction('📱')
    await f.add_reaction('🐍')
    await f.add_reaction('🖥️')
    await f.add_reaction('📚')
    await f.add_reaction('📊')

  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    if payload.emoji.name == '🎮':
      guild = self.bot.get_guild(payload.guild_id)
      role = nextcord.utils.get(guild.roles, name='gamedev')
      await payload.member.add_roles(role)
    elif payload.emoji.name == '🌎':
      guild = self.bot.get_guild(payload.guild_id)
      role = nextcord.utils.get(guild.roles, name='web')
      await payload.member.add_roles(role)
    elif payload.emoji.name == '📱':
      guild = self.bot.get_guild(payload.guild_id)
      role = nextcord.utils.get(guild.roles, name='mobile')
      await payload.member.add_roles(role)
    elif payload.emoji.name == '🐍':
      guild = self.bot.get_guild(payload.guild_id)
      role = nextcord.utils.get(guild.roles, name='scripting')
      await payload.member.add_roles(role)
    elif payload.emoji.name == '🖥️':
      guild = self.bot.get_guild(payload.guild_id)
      role = nextcord.utils.get(guild.roles, name='os')
      await payload.member.add_roles(role)
    elif payload.emoji.name == '📚':
      guild = self.bot.get_guild(payload.guild_id)
      role = nextcord.utils.get(guild.roles, name='jvm')
      await payload.member.add_roles(role)
    elif payload.emoji.name == '📊':
      guild = self.bot.get_guild(payload.guild_id)
      role = nextcord.utils.get(guild.roles, name='shell')
      await payload.member.add_roles(role)

  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, payload):
    if payload.emoji.name == '🎮':
      guild = self.bot.get_guild(payload.guild_id)
      role = nextcord.utils.get(guild.roles, name='gamedev')
      member = guild.get_member(payload.user_id)
      await member.remove_roles(role)
    elif payload.emoji.name == '🌎':
      guild = self.bot.get_guild(payload.guild_id)
      role = nextcord.utils.get(guild.roles, name='web')
      member = guild.get_member(payload.user_id)
      await member.remove_roles(role)
    elif payload.emoji.name == '📱':
      guild = self.bot.get_guild(payload.guild_id)
      role = nextcord.utils.get(guild.roles, name='mobile')
      member = guild.get_member(payload.user_id)
      await member.remove_roles(role)
    elif payload.emoji.name == '🐍':
      guild = self.bot.get_guild(payload.guild_id)
      role = nextcord.utils.get(guild.roles, name='scripting')
      member = guild.get_member(payload.user_id)
      await member.remove_roles(role)
    elif payload.emoji.name == '🖥️':
      guild = self.bot.get_guild(payload.guild_id)
      role = nextcord.utils.get(guild.roles, name='os')
      member = guild.get_member(payload.user_id)
      await member.remove_roles(role)
    elif payload.emoji.name == '📚':
      guild = self.bot.get_guild(payload.guild_id)
      role = nextcord.utils.get(guild.roles, name='jvm')
      member = guild.get_member(payload.user_id)
      await member.remove_roles(role)


def setup(bot):
  bot.add_cog(RoleReact(bot))