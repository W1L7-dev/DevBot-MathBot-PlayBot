from nextcord.ext import commands
import nextcord

class Infos(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name="rules", description="Get the rules of the server")
  async def rules(self, inter: nextcord.Interaction):
    embed = nextcord.Embed(title='Rules', description='These are the rules of the server', color=nextcord.Color.blurple())
    embed.add_field(name='1. Be respectful', value='You must respect all users, regardless of your liking towards them. Treat others the way you want to be treated.', inline=False)
    embed.add_field(name='2. No Inappropriate Language', value='The use of profanity should be kept to a minimum. However, any derogatory language towards any user is prohibited.', inline=False)
    embed.add_field(name='3. No Spamming', value='Spamming is not allowed. This includes excessive messages, emojis, and images.', inline=False)
    embed.add_field(name='4. No NSFW Content', value='NSFW content is not allowed. This includes any content that is sexually explicit, violent, or otherwise inappropriate.', inline=False)
    embed.add_field(name='5. No Advertising', value='Advertising is not allowed. This includes any links to other servers, personanal websites, or other platforms.', inline=False)
    embed.add_field(name='6. No Self-Promotion', value='Self-promotion is not allowed. This includes any links to your own social media accounts, YouTube channels, or other platforms.', inline=False)
    embed.add_field(name='7. No offensicve names and profile pictures', value='Your name and profile picture must not be offensive to any user. This includes any racial slurs, derogatory terms, or other inappropriate content.', inline=False)
    embed.add_field(name='8. No direct and inderect threats', value='Threats are not allowed. This includes any threats of violence, doxxing, hacking, raiding or other inappropriate content.', inline=False)
    embed.add_field(name='9. No impersonation', value='Impersonation is not allowed. This includes any attempts to impersonate any user, including staff members.', inline=False)
    embed.add_field(name='10. No trolling', value='Trolling is not allowed. This includes any attempts to disrupt the server, including spamming, raiding, or other inappropriate content.', inline=False)
    embed.add_field(name='11. No asking for staff', value='Asking for staff is not allowed. You can apply for staff in the forum `staff-application` This includes any attempts to ask for staff.', inline=False)
    embed.add_field(name="12. Speak English", value="Please speak English in the server. You won't be punished for it, but English is our main language.", inline=False)
    embed.add_field(name="13. No begging", value="Begging is not allowed. This includes any attempts to beg for money, nitro, or other inappropriate content.", inline=False)
    embed.add_field(name='14. Follow Discord TOS', value='You must follow Discord\'s Terms of Service. This includes any attempts to bypass Discord\'s TOS.', inline=False)
    embed.add_field(name='15. Follow Discord Community Guidelines', value='You must follow Discord\'s Community Guidelines. This includes any attempts to bypass Discord\'s Community Guidelines.', inline=False)
    embed.add_field(name='16. Follow Discord Guidelines', value='You must follow Discord\'s Guidelines. This includes any attempts to bypass Discord\'s Guidelines.', inline=False)
    embed.add_field(name="**The staff will punish you if you break the rules.**", value="**If you break the rules, you will be punished.**", inline=False)
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="userinfo", description="Get the info of a user")
  async def userinfo(self, inter: nextcord.Interaction, member: nextcord.Member=nextcord.SlashOption(required=False)):
    if member is None:
      member = inter.user
    embed = nextcord.Embed(title=f"{member.name}'s info", description=f"Here is the info of {member.name}", color=nextcord.Color.blurple())
    embed.add_field(name="Name", value=member.name, inline=False)
    embed.add_field(name="ID", value=member.id, inline=False)
    embed.add_field(name="Status", value=member.status, inline=False)
    embed.add_field(name="Top Role", value=member.top_role, inline=False)
    embed.add_field(name="Joined At", value=member.joined_at, inline=False)
    embed.add_field(name="Created At", value=member.created_at, inline=False)
    embed.add_field(name="Bot?", value=member.bot, inline=False)
    embed.set_thumbnail(url=member.avatar.url)
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="serverinfo", description="Get the info of the server")
  async def serverinfo(self, inter: nextcord.Interaction):
    embed = nextcord.Embed(title=f"{inter.guild.name}'s info", description=f"Here is the info of {inter.guild.name}", color=nextcord.Color.blurple())
    embed.add_field(name="Name", value=inter.guild.name, inline=False)
    embed.add_field(name="ID", value=inter.guild.id, inline=False)
    embed.add_field(name="Owner", value=inter.guild.owner, inline=False)
    embed.add_field(name="Region", value=inter.guild.region, inline=False)
    embed.add_field(name="Created At", value=inter.guild.created_at, inline=False)
    embed.add_field(name="Members", value=inter.guild.member_count, inline=False)
    embed.add_field(name="Bots", value=len([member for member in inter.guild.members if member.bot]), inline=False)
    embed.add_field(name="Humans", value=len([member for member in inter.guild.members if not member.bot]), inline=False)
    embed.add_field(name="Text Channels", value=len(inter.guild.text_channels), inline=False)
    embed.add_field(name="Voice Channels", value=len(inter.guild.voice_channels), inline=False)
    embed.add_field(name="Categories", value=len(inter.guild.categories), inline=False)
    embed.add_field(name="Roles", value=len(inter.guild.roles), inline=False)
    embed.add_field(name="Emojis", value=len(inter.guild.emojis), inline=False)
    embed.add_field(name="Boosts", value=inter.guild.premium_subscription_count, inline=False)
    embed.add_field(name="Boost Level", value=inter.guild.premium_tier, inline=False)
    embed.set_thumbnail(url=inter.guild.icon.url)
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="botinfo", description="Get the info of the bot")
  async def botinfo(self, inter: nextcord.Interaction):
    embed = nextcord.Embed(title=f"{inter.user.name}'s info", description=f"Here is the info of {self.user.name}", color=nextcord.Color.blurple())
    embed.add_field(name="Name", value=inter.user.name, inline=False)
    embed.add_field(name="ID", value=inter.user.id, inline=False)
    embed.add_field(name="Status", value=inter.user.status, inline=False)
    embed.add_field(name="Top Role", value=inter.user.top_role, inline=False)
    embed.add_field(name="Joined At", value=inter.user.joined_at, inline=False)
    embed.add_field(name="Created At", value=inter.user.created_at, inline=False)
    embed.add_field(name="Bot?", value=self.bot.user, inline=False)
    embed.set_thumbnail(url=inter.user.avatar.url)
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="roleinfo", description="Get the info of a role")
  async def roleinfo(self, ctx: nextcord.Interaction, role: nextcord.Role):
    embed = nextcord.Embed(title=f"{role.name}'s info", description=f"Here is the info of {role.name}", color=nextcord.Color.blurple())
    embed.add_field(name="Name", value=role.name, inline=False)
    embed.add_field(name="ID", value=role.id, inline=False)
    embed.add_field(name="Color", value=role.color, inline=False)
    embed.add_field(name="Position", value=role.position, inline=False)
    embed.add_field(name="Created At", value=role.created_at, inline=False)
    embed.add_field(name="Mentionable", value=role.mentionable, inline=False)
    embed.add_field(name="Hoisted", value=role.hoist, inline=False)
    embed.add_field(name="Managed", value=role.managed, inline=False)
    embed.add_field(name="Members", value=len(role.members), inline=False)
    embed.set_thumbnail(url=role.guild.icon.url)
    await ctx.send(embed=embed)

  @nextcord.slash_command(name="channelinfo", description="Get the info of a channel")
  async def channelinfo(self, ctx: nextcord.Interaction, channel: nextcord.TextChannel):
    embed = nextcord.Embed(title=f"{channel.name}'s info", description=f"Here is the info of {channel.name}", color=nextcord.Color.blurple())
    embed.add_field(name="Name", value=channel.name, inline=False)
    embed.add_field(name="ID", value=channel.id, inline=False)
    embed.add_field(name="Category", value=channel.category, inline=False)
    embed.add_field(name="Created At", value=channel.created_at, inline=False)
    embed.add_field(name="NSFW", value=channel.is_nsfw(), inline=False)
    embed.add_field(name="Members", value=len(channel.members), inline=False)
    embed.set_thumbnail(url=channel.guild.icon.url)
    await ctx.send(embed=embed)

  @nextcord.slash_command(name="emojiinfo", description="Get the info of an emoji")
  async def emojiinfo(self, ctx: nextcord.Interaction, emoji):
    embed = nextcord.Embed(title=f"{emoji.name}'s info", description=f"Here is the info of {emoji.name}", color=nextcord.Color.blurple())
    embed.add_field(name="Name", value=emoji.name, inline=False)
    embed.add_field(name="ID", value=emoji.id, inline=False)
    embed.add_field(name="Created At", value=emoji.created_at, inline=False)
    embed.add_field(name="Animated", value=emoji.animated, inline=False)
    embed.add_field(name="Managed", value=emoji.managed, inline=False)
    embed.add_field(name="URL", value=emoji.url, inline=False)
    embed.set_thumbnail(url=emoji.url)
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Infos(bot))
