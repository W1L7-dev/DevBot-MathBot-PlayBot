from nextcord.ext import commands, application_checks
import nextcord

class Admin(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.log = 1021762338279391262

  @nextcord.slash_command(name="addrole", description="Add a role to a user")
  @application_checks.has_permissions(manage_roles=True)
  async def addrole(self, inter: nextcord.Interaction, role: nextcord.Role,  member: nextcord.Member=nextcord.SlashOption(required=False)):
    if member is None:
      member = inter.user.mention
    embed = nextcord.Embed(title="Role Added", description=f"Added **{role.mention}** to **{member.mention}**", color=nextcord.Color.blurple())
    logembed = nextcord.Embed(title="Role Added", description=f"{inter.user.mention} added **{role.mention}** to **{member.mention}**", color=nextcord.Color.blurple())
    log = self.bot.get_channel(self.log)
    await member.add_roles(role)
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="removerole", description="Remove a role from a user")
  @application_checks.has_permissions(manage_roles=True)
  async def removerole(self, inter: nextcord.Interaction, role: nextcord.Role, member: nextcord.Member=nextcord.SlashOption(required=False)):
    if member is None:
      member = inter.user.mention
    embed = nextcord.Embed(title="Role Removed", description=f"Removed **{role.mention}** from **{member.mention}**", color=nextcord.Color.blurple())
    logembed = nextcord.Embed(title="Role Removed", description=f"{inter.user.mention} removed **{role.mention}** from **{member.mention}**", color=nextcord.Color.blurple())
    log = self.bot.get_channel(self.log)
    await member.remove_roles(role)
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="createrole", description="Create a role")
  @application_checks.has_permissions(manage_roles=True)
  async def createrole(self, inter: nextcord.Interaction, name: str, color=nextcord.SlashOption(required=False)):
    if color is None:
      color = nextcord.Color.blurple()
    elif color not in nextcord.Color():
      color = nextcord.Color.blurple()
    embed = nextcord.Embed(title="Role Created", description=f"Created **{name}**", color=nextcord.Color.blurple())
    logembed = nextcord.Embed(title="Role Created", description=f"{inter.user.mention} created **{name}**", color=nextcord.Color.blurple())
    log = self.bot.get_channel(self.log)
    await inter.guild.create_role(name=name, color=color)
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="delrole", description="Delete a role")
  @application_checks.has_permissions(manage_roles=True)
  async def delrole(self, inter: nextcord.Interaction, role: nextcord.Role):
    embed = nextcord.Embed(title="Role Deleted", description=f"Deleted **{role.mention}**", color=nextcord.Color.blurple())
    logembed = nextcord.Embed(title="Role Deleted", description=f"{inter.user.mention} deleted **{role.mention}**", color=nextcord.Color.blurple())
    log = self.bot.get_channel(self.log)
    await role.delete()
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="createcategory", description="Create a category")
  @application_checks.has_permissions(manage_channels=True)
  async def createcategory(self, inter: nextcord.Interaction, name: str):
    embed = nextcord.Embed(title="Category Created", description=f"Created **{name}**", color=nextcord.Color.blurple())
    logembed = nextcord.Embed(title="Category Created", description=f"{inter.user.mention} created **{name}**", color=nextcord.Color.blurple())
    log = self.bot.get_channel(self.log)
    await inter.guild.create_category(name=name)
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="delcategory", description="Delete a category")
  @application_checks.has_permissions(manage_channels=True)
  async def delcategory(self, inter: nextcord.Interaction, category: nextcord.CategoryChannel):
    for category in inter.guild.categories:
      if category.name == category:
        for channels in category.channels:
          await channels.delete()
        log = self.bot.get_channel(self.log)
        embed = nextcord.Embed(title="Category Deleted", description=f"Deleted **{category.name}**", color=nextcord.Color.blurple())
        logembed = nextcord.Embed(title="Category Deleted", description=f"{inter.user.mention} deleted **{category.name}**", color=nextcord.Color.blurple())
        await category.delete()
        await inter.response.send_message(embed=embed)
        await log.send(embed=logembed)
        break

  @nextcord.slash_command(name="addcategory", description="Add a channel to a category")
  @application_checks.has_permissions(manage_channels=True)
  async def addcategory(self, inter: nextcord.Interaction, category: nextcord.CategoryChannel, channel: nextcord.TextChannel):
    embed = nextcord.Embed(title="Channel Added", description=f"Added **{channel.mention}** to **{category.name}**", color=nextcord.Color.blurple())
    logembed = nextcord.Embed(title="Channel Added", description=f"{inter.user.mention} added **{channel.mention}** to **{category.name}**", color=nextcord.Color.blurple())
    log = self.bot.get_channel(self.log)
    await channel.edit(category=category)
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="removecategory", description="Remove a channel from a category")
  @application_checks.has_permissions(manage_channels=True)
  async def removecategory(self, inter: nextcord.Interaction, channel: nextcord.TextChannel):
    embed = nextcord.Embed(title="Channel Removed", description=f"Removed **{channel.mention}** from **{channel.category.name}**", color=nextcord.Color.blurple())
    logembed = nextcord.Embed(title="Channel Removed", description=f"{inter.user.mention} removed **{channel.mention}** from **{channel.category.name}**", color=nextcord.Color.blurple())
    log = self.bot.get_channel(self.log)
    await channel.edit(category=None)
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="createchannel", description="Create a channel")
  @application_checks.has_permissions(manage_channels=True)
  async def createchannel(self, inter: nextcord.Interaction, name: str, category: nextcord.CategoryChannel=nextcord.SlashOption(required=False)):
    embed = nextcord.Embed(title="Channel Created", description=f"Created **{name}**", color=nextcord.Color.blurple())
    logembed = nextcord.Embed(title="Channel Created", description=f"{inter.user.mention} created **{name}**", color=nextcord.Color.blurple())
    log = self.bot.get_channel(self.log)
    await inter.guild.create_text_channel(name=name, category=category)
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="delchannel", description="Delete a channel")
  @application_checks.has_permissions(manage_channels=True)
  async def delchannel(self, inter: nextcord.Interaction, channel: nextcord.TextChannel):
    embed = nextcord.Embed(title="Channel Deleted", description=f"Deleted **{channel.mention}**", color=nextcord.Color.blurple())
    logembed = nextcord.Embed(title="Channel Deleted", description=f"{inter.user.mention} deleted **{channel.mention}**", color=nextcord.Color.blurple())
    log = self.bot.get_channel(self.log)
    await channel.delete()
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="createvoicechannel", description="Create a voice channel")
  @application_checks.has_permissions(manage_channels=True)
  async def createvoicechannel(self, inter: nextcord.Interaction, name: str, category: nextcord.CategoryChannel=nextcord.SlashOption(required=False)):
    embed = nextcord.Embed(title="Voice Channel Created", description=f"Created **{name}**", color=nextcord.Color.blurple())
    logembed = nextcord.Embed(title="Voice Channel Created", description=f"{inter.user.mention} created **{name}**", color=nextcord.Color.blurple())
    log = self.bot.get_channel(self.log)
    await inter.guild.create_voice_channel(name=name, category=category)
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="delvoicechannel", description="Delete a voice channel")
  @application_checks.has_permissions(manage_channels=True)
  async def delvoicechannel(self, inter: nextcord.Interaction, channel: nextcord.VoiceChannel):
    embed = nextcord.Embed(title="Voice Channel Deleted", description=f"Deleted **{channel.name}**", color=nextcord.Color.blurple())
    logembed = nextcord.Embed(title="Voice Channel Deleted", description=f"{inter.user.mention} deleted **{channel.name}**", color=nextcord.Color.blurple())
    log = self.bot.get_channel(self.log)
    await channel.delete()
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

def setup(bot):
  bot.add_cog(Admin(bot))