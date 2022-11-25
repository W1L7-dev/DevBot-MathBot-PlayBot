import os

def load_cog(bot, cog):
  for filename in os.listdir(cog):
    if filename.endswith(".py"):
      bot.load_extension(f"{cog.replace('/', '.')}.{filename[:-3]}")