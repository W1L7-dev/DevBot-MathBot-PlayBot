from nextcord.ext import commands
import nextcord
import random

class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name="8ball", description="Ask the magic 8ball a question")
  async def _8ball(self, inter: nextcord.Interaction, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.'
    ]
    embed = nextcord.Embed(title="Magic 8ball", description=f"Question: {question} \nAnswer: {random.choice(responses)}", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="coinflip", description="Flip a coin")
  async def coinflip(self, inter: nextcord.Interaction):
    responses = ["Heads", "Tails"]
    embed = nextcord.Embed(title="Coinflip", description=f"Result: {random.choice(responses)}", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="dice", description="Roll a dice")
  async def dice(self, inter: nextcord.Interaction):
    embed = nextcord.Embed(title="Dice", description=f"Result: {random.randint(1, 6)}", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="rps", description="Play rock paper scissors")
  async def rps(self, inter: nextcord.Interaction, choice: str):
    choices = ["rock", "paper", "scissors"]
    if choice.lower() not in choices:
      await inter.response.send_message("Please choose either rock, paper, or scissors")
    else:
      bot_choice = random.choice(choices)
      if choice.lower() == bot_choice:
        embed = nextcord.Embed(title="Rock Paper Scissors", description=f"You chose {choice.lower()} \nI chose {bot_choice} \nResult: Tie", color=nextcord.Color.blurple())
        await inter.response.send_message(embed=embed)
      elif choice.lower() == "rock" and bot_choice == "scissors":
        embed = nextcord.Embed(title="Rock Paper Scissors", description=f"You chose {choice.lower()} \nI chose {bot_choice} \nResult: You win", color=nextcord.Color.blurple())
        await inter.response.send_message(embed=embed)
      elif choice.lower() == "rock" and bot_choice == "paper":
        embed = nextcord.Embed(title="Rock Paper Scissors", description=f"You chose {choice.lower()} \nI chose {bot_choice} \nResult: I win", color=nextcord.Color.blurple())
        await inter.response.send_message(embed=embed)
      elif choice.lower() == "paper" and bot_choice == "rock":
        embed = nextcord.Embed(title="Rock Paper Scissors", description=f"You chose {choice.lower()} \nI chose {bot_choice} \nResult: You win", color=nextcord.Color.blurple())
        await inter.response.send_message(embed=embed)
      elif choice.lower() == "paper" and bot_choice == "scissors":
        embed = nextcord.Embed(title="Rock Paper Scissors", description=f"You chose {choice.lower()} \nI chose {bot_choice} \nResult: I win", color=nextcord.Color.blurple())
        await inter.response.send_message(embed=embed)
      elif choice.lower() == "scissors" and bot_choice == "paper":
        embed = nextcord.Embed(title="Rock Paper Scissors", description=f"You chose {choice.lower()} \nI chose {bot_choice} \nResult: You win", color=nextcord.Color.blurple())
        await inter.response.send_message(embed=embed)
      elif choice.lower() == "scissors" and bot_choice == "rock":
        embed = nextcord.Embed(title="Rock Paper Scissors", description=f"You chose {choice.lower()} \nI chose {bot_choice} \nResult: I win", color=nextcord.Color.blurple())
        await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="choose", description="Choose between multiple options")
  async def choose(self, inter: nextcord.Interaction, *choices: str):
    if len(choices) < 2:
      await inter.response.send_message("Please provide at least 2 choices")
    else:
      embed = nextcord.Embed(title="Choose", description=f"Result: {random.choice(choices)}", color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="russianroulette", description="Play russian roulette")
  async def russianroulette(self, inter: nextcord.Interaction):
    responses = ["You died", "You lived"]
    embed = nextcord.Embed(title="Russian Roulette", description=f"Result: {random.choice(responses)}", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="slots", description="Play slots")
  async def slots(self, inter: nextcord.Interaction):
    responses = ["🍎", "🍊", "🍇", "🍒", "🍋", "🍉"]
    embed = nextcord.Embed(title="Slots", description=f"{random.choice(responses)} {random.choice(responses)} {random.choice(responses)}", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="ruin", description="Ruin text")
  async def ruin(self, inter: nextcord.Interaction, text: str):
    embed = nextcord.Embed(title="Ruin", description=f"Result: {text.upper()}", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="reverse", description="Reverse text")
  async def reverse(self, inter: nextcord.Interaction, text: str):
    embed = nextcord.Embed(title="Reverse", description=f"Result: {text[::-1]}", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

def setup(bot):
  bot.add_cog(Fun(bot))