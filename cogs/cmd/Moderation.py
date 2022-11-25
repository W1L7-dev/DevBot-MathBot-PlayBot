from nextcord.ext import commands, application_checks
import datetime
import nextcord
import asyncio
import re
import json

class Moderation(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name="lock", description="Lock a channel")
  @application_checks.has_guild_permissions(manage_channels=True)
  async def lock(self, inter: nextcord.Interaction, channel: nextcord.TextChannel=nextcord.SlashOption(required=False)):
    if channel is None:
      channel = inter.channel
    log = self.bot.get_channel(1021762338279391262)
    logembed = nextcord.Embed(title="Channel Locked", description=f"{inter.user.mention} locked {channel.mention}", color=nextcord.Color.blurple())
    embed = nextcord.Embed(title="Channel Locked", description=f"Locked **{channel.mention}**", color=nextcord.Color.blurple())
    await channel.set_permissions(inter.guild.default_role, send_messages=False)
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="unlock", description="Unlock a channel")
  @application_checks.has_guild_permissions(manage_channels=True)
  async def unlock(self, inter: nextcord.Interaction, channel: nextcord.TextChannel=nextcord.SlashOption(required=False)):
    if channel is None:
      channel = inter.channel
    log = self.bot.get_channel(1021762338279391262)
    logembed = nextcord.Embed(title="Channel Unlocked", description=f"Unlocked **{channel.mention}**", color=nextcord.Color.blurple())
    embed = nextcord.Embed(title="Channel Unlocked", description=f"Unlocked **{channel.mention}**", color=nextcord.Color.blurple())
    await channel.set_permissions(inter.guild.default_role, send_messages=True)
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="slowmode", description="Set the slowmode of a channel")
  @application_checks.has_guild_permissions(manage_channels=True)
  async def slowmode(self, inter: nextcord.Interaction, seconds: int, channel: nextcord.TextChannel=nextcord.SlashOption(required=False)):
    if channel is None:
      channel = inter.channel
    log = self.bot.get_channel(1021762338279391262)
    logembed = nextcord.Embed(title="Slowmode Set", description=f"Set the slowmode of **{channel.mention}** to **{seconds}** seconds", color=nextcord.Color.blurple())
    embed = nextcord.Embed(title="Slowmode Set", description=f"Set the slowmode of **{channel.mention}** to **{seconds}** seconds", color=nextcord.Color.blurple())
    await channel.edit(slowmode_delay=seconds)
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="templock", description="Temporarily lock a channel")
  @application_checks.has_guild_permissions(manage_channels=True)
  async def templock(self, inter: nextcord.Interaction, time: int, channel: nextcord.TextChannel=nextcord.SlashOption(required=False)):
    if channel is None:
      channel = inter.channel
    input = re.split("(\d+)", time)
    del input[0]
    seconds = 0
    for i in range(1, len(input), 2):
      timeModifier = input[i]
      timeValue = int(input[i-1])
      if timeModifier == "d":
        seconds += 86400 * timeValue
      elif timeModifier == "h":
        seconds += 3600 * timeValue
      elif timeModifier == "m":
        seconds += 60 * timeValue
      elif timeModifier == "s":
        seconds += timeValue
    log = self.bot.get_channel(1021762338279391262)
    embed = nextcord.Embed(title="Channel Temporarily Locked", description=f"Temporarily locked **{channel.mention}** for **{seconds}** seconds", color=nextcord.Color.blurple())
    logembed = nextcord.Embed(title="Channel Temporarily Locked", description=f"Temporarily locked **{channel.mention}** for **{seconds}** seconds", color=nextcord.Color.blurple())
    await channel.set_permissions(inter.guild.default_role, send_messages=False)
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)
    await asyncio.sleep(seconds)
    await channel.set_permissions(inter.guild.default_role, send_messages=True)

  @nextcord.slash_command(name="clear", description="Clear messages")
  @application_checks.has_guild_permissions(manage_messages=True)
  async def clear(self, inter: nextcord.Interaction, amount: int, channel: nextcord.TextChannel=nextcord.SlashOption(required=False)):
    if channel is None:
      channel = inter.channel
    log = self.bot.get_channel(1021762338279391262)
    logembed = nextcord.Embed(title="Messages Cleared", description=f"Cleared **{amount}** messages in **{channel.mention}**", color=nextcord.Color.blurple())
    embed = nextcord.Embed(title="Messages Cleared", description=f"Cleared **{amount}** messages in **{channel.mention}**", color=nextcord.Color.blurple())
    await channel.purge(limit=amount)
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="ban", description="Ban a user")
  @application_checks.has_guild_permissions(ban_members=True)
  async def ban(self, inter: nextcord.Interaction, user: nextcord.User, reason: str=nextcord.SlashOption(required=False)):
    if reason is None:
      reason = "No reason provided"
    log = self.bot.get_channel(1021762338279391262)
    logembed = nextcord.Embed(title="User Banned", description=f"Banned **{user.mention}** because of {reason}", color=nextcord.Color.blurple())
    embed = nextcord.Embed(title="User Banned", description=f"Banned **{user.mention}** because of {reason}", color=nextcord.Color.blurple())
    await inter.guild.ban(user, reason=reason)
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="unban", description="Unban a user")
  @application_checks.has_guild_permissions(ban_members=True)
  async def unban(self, inter: nextcord.Interaction, user: nextcord.User, reason: str=nextcord.SlashOption(required=False)):
    banned_users = await inter.guild.bans()
    member_name, member_discriminator = user.split('#')
    for ban_entry in banned_users:
      user = ban_entry.user
      if (user.name, user.discriminator) == (member_name, member_discriminator):
        log = self.bot.get_channel(1021762338279391262)
        logembed = nextcord.Embed(title="User Unbanned", description=f"Unbanned **{user.mention}**", color=nextcord.Color.blurple())
        embed = nextcord.Embed(title="User Unbanned", description=f"Unbanned **{user.mention}**", color=nextcord.Color.blurple())
        await inter.guild.unban(user)
        await inter.response.send_message(embed=embed)
        await log.send(embed=logembed)
        return
      else:
        embed = nextcord.Embed(title="User Not Found", description=f"Couldn't find **{user}** in the ban list", color=nextcord.Color.blurple())
        await inter.response.send_message(embed=embed)
        return

  @nextcord.slash_command(name="tempban", description="Temporarily ban a user")
  @application_checks.has_guild_permissions(ban_members=True)
  async def tempban(self, inter: nextcord.Interaction, user: nextcord.User, time: int, reason: str=nextcord.SlashOption(required=False)):
    if reason is None:
      reason = "No reason provided"
    input = re.split("(\d+)", time)
    del input[0]
    seconds = 0
    for i in range(1, len(input), 2):
      timeModifier = input[i]
      timeValue = int(input[i-1])
      if timeModifier == "d":
        seconds += 86400 * timeValue
      elif timeModifier == "h":
        seconds += 3600 * timeValue
      elif timeModifier == "m":
        seconds += 60 * timeValue
      elif timeModifier == "s":
        seconds += timeValue
    log = self.bot.get_channel(1021762338279391262)
    logembed = nextcord.Embed(title="User Temporarily Banned", description=f"Temporarily banned **{user.mention}** for **{seconds}** seconds because of {reason}", color=nextcord.Color.blurple())
    embed = nextcord.Embed(title="User Temporarily Banned", description=f"Temporarily banned **{user.mention}** for **{seconds}** seconds because of {reason}", color=nextcord.Color.blurple())
    await inter.guild.ban(user, reason=reason)
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)
    await asyncio.sleep(seconds)
    await inter.guild.unban(user)

  @nextcord.slash_command(name="kick", description="Kick a user")
  @application_checks.has_guild_permissions(kick_members=True)
  async def kick(self, inter: nextcord.Interaction, user: nextcord.User, reason: str=nextcord.SlashOption(required=False)):
    if reason is None:
      reason = "No reason provided"
    log = self.bot.get_channel(1021762338279391262)
    logembed = nextcord.Embed(title="User Kicked", description=f"Kicked **{user.mention}** because of {reason}", color=nextcord.Color.blurple())
    embed = nextcord.Embed(title="User Kicked", description=f"Kicked **{user.mention}** because of {reason}", color=nextcord.Color.blurple())
    await inter.guild.kick(user, reason=reason)
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="timeout", description="Temporarily mute a user")
  @application_checks.has_guild_permissions(manage_roles=True)
  async def timeout(self, inter: nextcord.Interaction, user: nextcord.User, time: int, reason: str=nextcord.SlashOption(required=False)):
    if reason is None:
      reason = "No reason provided"
    input = re.split("(\d+)", time)
    del input[0]
    seconds = 0
    for i in range(1, len(input), 2):
      timeModifier = input[i]
      timeValue = int(input[i-1])
      if timeModifier == "d":
        seconds += 86400 * timeValue
      elif timeModifier == "h":
        seconds += 3600 * timeValue
      elif timeModifier == "m":
        seconds += 60 * timeValue
      elif timeModifier == "s":
        seconds += timeValue
    log = self.bot.get_channel(1021762338279391262)
    logembed = nextcord.Embed(title="User Timed Out", description=f"Temporarily muted **{user.mention}** for **{seconds}** seconds because of {reason}", color=nextcord.Color.blurple())
    embed = nextcord.Embed(title="User Timed Out", description=f"Temporarily muted **{user.mention}** for **{seconds}** seconds because of {reason}", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)
    await asyncio.sleep(seconds)
    await user.timeout(datetime.timedelta(seconds=seconds, reason=reason))

  @nextcord.slash_command(name="warn", description="Warn a user")
  @application_checks.has_guild_permissions(manage_messages=True)
  async def warn(self, inter: nextcord.Interaction, member: nextcord.Member, *, reason=nextcord.SlashOption(required=False)):
    with open("/json/warns.json", "r") as f:
      warns = json.load(f)
    with open("/json/warns.json", "w") as f:
      if str(member.id) in warns:
        warns[str(member.id)]["warns"] += 1
        warns[str(member.id)]["reasons"].append(reason)
      else:
        warns[str(member.id)] = {}
        warns[str(member.id)]["warns"] = 1
        warns[str(member.id)]["reasons"] = [reason]
      json.dump(warns, f, indent=4)
    log = self.bot.get_channel(1021762338279391262)
    logembed = nextcord.Embed(title="User Warned", description=f"Warned **{member.mention}** because of {reason}", color=nextcord.Color.blurple())
    embed = nextcord.Embed(title="User Warned", description=f"Warned **{member.mention}** because of {reason}", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)
    await log.send(embed=logembed)

  @nextcord.slash_command(name="warnings", description="Check a user's warnings")
  @application_checks.has_guild_permissions(manage_messages=True)
  async def warnings(self, inter: nextcord.Interaction, member: nextcord.Member):
    with open("/json/warns.json", "r") as f:
      warns = json.load(f)
    if str(member.id) in warns:
      embed = nextcord.Embed(title=f"Warnings for {member}", description=f"**{warns[str(member.id)]['warns']}** warnings", color=nextcord.Color.blurple())
      for reason in warns[str(member.id)]["reasons"]:
        embed.add_field(name="Reason", value=reason, inline=False)
    else:
      embed = nextcord.Embed(title=f"Warnings for {member}", description="**0** warnings", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="clearwarns", description="Clear a user's warnings")
  @application_checks.has_guild_permissions(manage_messages=True)
  async def clearwarns(self, inter: nextcord.Interaction, member: nextcord.Member):
    with open("/json/warns.json", "r") as f:
      warns = json.load(f)
    with open("/json/warns.json", "w") as f:
      if str(member.id) in warns:
        del warns[str(member.id)]
      json.dump(warns, f, indent=4)
    embed = nextcord.Embed(title="Warnings Cleared", description=f"Warnings for **{member.mention}** have been cleared", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="removewarn", description="Remove a warning from a user")
  @application_checks.has_guild_permissions(manage_messages=True)
  async def removewarn(self, inter: nextcord.Interaction, member: nextcord.Member, number: int):
    with open("/json/warns.json", "r") as f:
      warns = json.load(f)
    with open("/json/warns.json", "w") as f:
      if str(member.id) in warns:
        warns[str(member.id)]["warns"] -= 1
        del warns[str(member.id)]["reasons"][number]
      json.dump(warns, f, indent=4)
    embed = nextcord.Embed(title="Warning Removed", description=f"{number} warning(s) for **{member.mention}** has been removed", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

def setup(bot):
  bot.add_cog(Moderation(bot))