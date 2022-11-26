from nextcord.ext import commands
import nextcord
import asyncio
import json

class Levelling(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author.bot:
      return

    with open('cogs/cmd/json/levels.json', 'r') as f:
      users = json.load(f)

    await self.update_data(users, message.author)
    await self.add_experience(users, message.author, 5)
    await self.level_up(users, message.author, message)

    with open('cogs/cmd/json/levels.json', 'w') as f:
      json.dump(users, f)

  async def update_data(self, users, user):
    if not str(user.id) in users:
      users[str(user.id)] = {}
      users[str(user.id)]['experience'] = 0
      users[str(user.id)]['level'] = 1

  async def add_experience(self, users, user, exp):
    users[str(user.id)]['experience'] += exp

  async def level_up(self, users, user, message):
    experience = users[str(user.id)]['experience']
    lvl_start = users[str(user.id)]['level']
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
      await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
      users[str(user.id)]['level'] = lvl_end

  @nextcord.slash_command(name='rank', description='Shows your rank')
  async def rank(self, inter: nextcord.Interaction):
    with open('cogs/cmd/json/levels.json', 'r') as f:
      users = json.load(f)

    await self.update_data(users, inter.user)

    user_id = str(inter.user.id)
    username = inter.user.name
    level = users[user_id]['level']
    experience = users[user_id]['experience']

    embed = nextcord.Embed(title=f"{username}'s Rank", description=f"{username} is level {level}", color=nextcord.Color.blue())
    embed.set_thumbnail(url=inter.user.avatar.url)
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name='leaderboard', description='Shows the leaderboard')
  async def leaderboard(self, inter: nextcord.Interaction):
    with open('cogs/cmd/json/levels.json', 'r') as f:
      users = json.load(f)
    leaderboard = []
    for user in users:
      name = int(user)
      level = users[user]['level']
      leaderboard.append([name, level])
    embed = nextcord.Embed(title="Leaderboard", description="The leaderboard", color=nextcord.Color.blue())
    i = 1
    for x in range(len(leaderboard)):
      name, level = leaderboard[x]
      embed.add_field(name=f"{i}. {self.bot.get_user(name)}", value=f"Level: {level}", inline=False)
      i += 1
    await inter.response.send_message(embed=embed)

def setup(bot):
  bot.add_cog(Levelling(bot))