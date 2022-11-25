from nextcord.ext import commands
import nextcord

class OnCommandError(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandNotFound):
      embed = nextcord.Embed(title="Command Not Found", description="The command you entered was not found. Please try again.", color=nextcord.Color.red())
      await ctx.send(embed=embed)
      print(error)
    elif isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(title="Missing Required Argument", description="You are missing a required argument. Please try again.", color=nextcord.Color.red())
      await ctx.send(embed=embed)
      print(error)
    elif isinstance(error, commands.MissingPermissions):
      embed = nextcord.Embed(title="Missing Permissions", description="You are missing the required permissions to use this command.", color=nextcord.Color.red())
      await ctx.send(embed=embed)
      print(error)
    elif isinstance(error, commands.BotMissingPermissions):
      embed = nextcord.Embed(title="Bot Missing Permissions", description="The bot is missing the required permissions to use this command.", color=nextcord.Color.red())
      await ctx.send(embed=embed)
      print(error)
    elif isinstance(error, commands.NotOwner):
      embed = nextcord.Embed(title="Not Bot Owner", description="You are not the owner of this bot.", color=nextcord.Color.red())
      await ctx.send(embed=embed)
      print(error)
    elif isinstance(error, commands.CommandOnCooldown):
      embed = nextcord.Embed(title="Command On Cooldown", description="This command is on cooldown. Please try again later.", color=nextcord.Color.red())
      await ctx.send(embed=embed)
      print(error)
    elif isinstance(error, commands.DisabledCommand):
      embed = nextcord.Embed(title="Command Disabled", description="This command is disabled.", color=nextcord.Color.red())
      await ctx.send(embed=embed)
      print(error)
    elif isinstance(error, commands.CheckFailure):
      embed = nextcord.Embed(title="Check Failure", description="You failed a check.", color=nextcord.Color.red())
      await ctx.send(embed=embed)
      print(error)
    elif isinstance(error, commands.CommandInvokeError):
      embed = nextcord.Embed(title="Command Invoke Error", description="An error occurred while invoking the command.", color=nextcord.Color.red())
      await ctx.send(embed=embed)
      print(error)
    elif isinstance(error, commands.CommandError):
      embed = nextcord.Embed(title="Command Error", description="An error occurred while processing the command.", color=nextcord.Color.red())
      await ctx.send(embed=embed)
      print(error)
    elif isinstance(error, commands.ExtensionError):
      embed = nextcord.Embed(title="Extension Error", description="An error occurred while processing the extension.", color=nextcord.Color.red())
      await ctx.send(embed=embed)
      print(error)
    elif isinstance(error, commands.ExtensionAlreadyLoaded):
      embed = nextcord.Embed(title="Extension Already Loaded", description="The extension is already loaded.", color=nextcord.Color.red())
      await ctx.send(embed=embed)
      print(error)
    elif isinstance(error, commands.ExtensionNotLoaded):
      embed = nextcord.Embed(title="Extension Not Loaded", description="The extension is not loaded.", color=nextcord.Color.red())
      await ctx.send(embed=embed)
      print(error)
    elif isinstance(error, commands.ExtensionNotFound):
      embed = nextcord.Embed(title="Extension Not Found", description="The extension was not found.", color=nextcord.Color.red())
      await ctx.send(embed=embed)
      print(error)
    elif isinstance(error, commands.ExtensionFailed):
      embed = nextcord.Embed(title="Extension Failed", description="The extension failed to load.", color=nextcord.Color.red())
      await ctx.send(embed=embed)
      print(error)
    else:
      embed = nextcord.Embed(title="Unknown Error", description="An unknown error occurred. Please try again.", color=nextcord.Color.red())
      await ctx.send(embed=embed)
      print(error)

def setup(bot):
  bot.add_cog(OnCommandError(bot))