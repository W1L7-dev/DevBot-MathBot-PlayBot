from dotenv import load_dotenv
from nextcord.ext import commands
from tasks.LoadCog import load_cog
import nextcord
import os

def playbot():
  load_dotenv()
  intents = nextcord.Intents.all()
  bot = commands.Bot(command_prefix="!", intents=intents, default_guild_ids=[1021582244407685200])
  bot.remove_command("help")
  load_cog(bot=bot, cog="cogs/music")
  bot.run(os.getenv("PLAYBOT"))

if __name__ == "__main__":
  playbot()