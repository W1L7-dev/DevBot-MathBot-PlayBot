from nextcord.ext import commands, application_checks
from tasks.asyncs.Clear import cls
from tasks.Restart import restart
import nextcord
import datetime
import time
import os

class Dev(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    global uptime
    uptime = time.time()

  @nextcord.slash_command(name="uptime", description="Shows the uptime of the bot")
  @application_checks.has_guild_permissions(administrator=True)
  async def uptime(self, inter: nextcord.Interaction):
    now = str(datetime.timedelta(seconds=int(round(time.time() - uptime))))
    embed = nextcord.Embed(title="Uptime", description=f"Uptime: **{now}**", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="clearoutput", description="Clears the console")
  @application_checks.has_guild_permissions(administrator=True)
  async def clearoutput(self, inter: nextcord.Interaction):
    embed = nextcord.Embed(title="Clear", description="Cleared the console", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)
    await cls()

  @nextcord.slash_command(name="print", description="Prints something in the terminal")
  @application_checks.has_permissions(administrator=True)
  async def echo(self, inter: nextcord.Interaction, *, text: str):
    embed = nextcord.Embed(title="Print", description=f"Printed `{text}` in the terminal", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)
    print(text)

  @nextcord.slash_command(name="restart", description="Restarts the bot")
  @application_checks.has_guild_permissions(administrator=True)
  async def restart(self, inter: nextcord.Interaction):
    embed = nextcord.Embed(title="Restart", description="Restarting the bot...", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)
    restart()

  @nextcord.slash_command(name="shutdown", description="Shuts down the bot")
  @application_checks.has_guild_permissions(administrator=True)
  async def shutdown(self, inter: nextcord.Interaction):
    embed = nextcord.Embed(title="Shutdown", description="Shutting down the bot...", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)
    await self.bot.close()

  @nextcord.slash_command(name="loadcog", description="Loads a cog")
  @application_checks.has_guild_permissions(administrator=True)
  async def loadcog(self, inter: nextcord.Interaction, cog: str, type):
    try:
      self.bot.load_extension(f"cogs.{type}.{cog}")
      embed = nextcord.Embed(title="LoadCog", description=f"Loaded **{cog}**", color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)
    except Exception as e:
      embed = nextcord.Embed(title="LoadCog", description=f"Failed to load **{cog}** due to \n```{e}```", color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="unloadcog", description="Unloads a cog")
  @application_checks.has_guild_permissions(administrator=True)
  async def unloadcog(self, inter: nextcord.Interaction, cog: str, type):
    try:
      self.bot.unload_extension(f"cogs.{type}.{cog}")
      embed = nextcord.Embed(title="UnloadCog", description=f"Unloaded **{cog}**", color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)
    except Exception as e:
      embed = nextcord.Embed(title="UnloadCog", description=f"Failed to unload **{cog}** due to \n```{e}```", color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="reloadcog", description="Reloads a cog")
  @application_checks.has_guild_permissions(administrator=True)
  async def reloadcog(self, inter: nextcord.Interaction, cog: str, type):
    try:
      self.bot.reload_extension(f"cogs.{type}.{cog}")
      embed = nextcord.Embed(title="ReloadCog", description=f"Reloaded **{cog}**", color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)
    except Exception as e:
      embed = nextcord.Embed(title="ReloadCog", description=f"Failed to reload **{cog}** due to \n```{e}```", color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="activityplay", description="Sets the bot's activity to playing")
  @application_checks.has_guild_permissions(administrator=True)
  async def activityplay(self, inter: nextcord.Interaction, activity: str):
    await self.bot.change_presence(activity=nextcord.Game(name=activity))
    embed = nextcord.Embed(title="ActivityPlay", description=f"Set the activity to **{activity}**", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="activitywatch", description="Sets the bot's activity to watching")
  @application_checks.has_guild_permissions(administrator=True)
  async def activitywatch(self, inter: nextcord.Interaction, activity: str):
    await self.bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=activity))
    embed = nextcord.Embed(title="ActivityWatch", description=f"Set the activity to **{activity}**", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="activitylisten", description="Sets the bot's activity to listening")
  @application_checks.has_guild_permissions(administrator=True)
  async def activitylisten(self, inter: nextcord.Interaction, activity: str):
    await self.bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=activity))
    embed = nextcord.Embed(title="ActivityListen", description=f"Set the activity to **{activity}**", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="activitystream", description="Sets the bot's activity to streaming")
  @application_checks.has_guild_permissions(administrator=True)
  async def activitystream(self, inter: nextcord.Interaction, activity: str, url: str):
    await self.bot.change_presence(activity=nextcord.Streaming(name=activity, url=url))
    embed = nextcord.Embed(title="ActivityStream", description=f"Set the activity to **{activity}**", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="activityclear", description="Clears the bot's activity")
  @application_checks.has_guild_permissions(administrator=True)
  async def activityclear(self, inter: nextcord.Interaction):
    await self.bot.change_presence(activity=None)
    embed = nextcord.Embed(title="ActivityClear", description="Cleared the activity", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="activitydefault", description="Sets the bot's activity to the default")
  @application_checks.has_guild_permissions(administrator=True)
  async def activitydefault(self, inter: nextcord.Interaction):
    await self.bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"The Dev Community"))
    embed = nextcord.Embed(title="ActivityDefault", description="Set the activity to the default", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="statusonline", description="Sets the bot's status to online")
  @application_checks.has_guild_permissions(administrator=True)
  async def statusonline(self, inter: nextcord.Interaction):
    await self.bot.change_presence(status=nextcord.Status.online)
    embed = nextcord.Embed(title="StatusOnline", description="Set the status to online", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="statusidle", description="Sets the bot's status to idle")
  @application_checks.has_guild_permissions(administrator=True)
  async def statusidle(self, inter: nextcord.Interaction):
    await self.bot.change_presence(status=nextcord.Status.idle)
    embed = nextcord.Embed(title="StatusIdle", description="Set the status to idle", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="statusdnd", description="Sets the bot's status to dnd")
  @application_checks.has_guild_permissions(administrator=True)
  async def statusdnd(self, inter: nextcord.Interaction):
    await self.bot.change_presence(status=nextcord.Status.dnd)
    embed = nextcord.Embed(title="StatusDND", description="Set the status to dnd", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="statusoffline", description="Sets the bot's status to offline")
  @application_checks.has_guild_permissions(administrator=True)
  async def statusoffline(self, inter: nextcord.Interaction):
    await self.bot.change_presence(status=nextcord.Status.offline)
    embed = nextcord.Embed(title="StatusOffline", description="Set the status to offline", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="createfile", description="Creates a file")
  @application_checks.has_guild_permissions(administrator=True)
  async def createfile(self, inter: nextcord.Interaction, filename: str, content: str=nextcord.SlashOption(required=False)):
    if content is None:
      content = ""
    with open(filename, "w") as f:
      f.write(content)
    embed = nextcord.Embed(title="CreateFile", description=f"Created file **{filename}**", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="delfile", description="Deletes a file")
  @application_checks.has_guild_permissions(administrator=True)
  async def delfile(self, inter: nextcord.Interaction, filename: str):
    try:
      os.remove(filename)
      embed = nextcord.Embed(title="DelFile", description=f"Deleted file **{filename}**", color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)
    except FileNotFoundError:
      embed = nextcord.Embed(title="DelFile", description=f"File **{filename}** not found", color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="readfile", description="Reads a file")
  @application_checks.has_guild_permissions(administrator=True)
  async def readfile(self, inter: nextcord.Interaction, filename: str):
    with open(filename, "r") as f:
      content = f.read()
    embed = nextcord.Embed(title="ReadFile", description=f"**{filename}**\n{content}", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="writefile", description="Writes to a file")
  @application_checks.has_guild_permissions(administrator=True)
  async def writefile(self, inter: nextcord.Interaction, filename: str, content: str):
    with open(filename, "a") as f:
      f.write(content)
    embed = nextcord.Embed(title="WriteFile", description=f"Wrote to file **{filename}**", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="clearfile", description="Clears a file")
  @application_checks.has_guild_permissions(administrator=True)
  async def clearfile(self, inter: nextcord.Interaction, filename: str):
    with open(filename, "w") as f:
      f.write("")
    embed = nextcord.Embed(title="ClearFile", description=f"Cleared file **{filename}**", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="createfolder", description="Creates a folder")
  @application_checks.has_guild_permissions(administrator=True)
  async def createfolder(self, inter: nextcord.Interaction, foldername: str):
    os.mkdir(foldername)
    embed = nextcord.Embed(title="CreateFolder", description=f"Created folder **{foldername}**", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="delfolder", description="Deletes a folder")
  @application_checks.has_guild_permissions(administrator=True)
  async def delfolder(self, inter: nextcord.Interaction, foldername: str):
    try:
      os.rmdir(foldername)
      embed = nextcord.Embed(title="DelFolder", description=f"Deleted folder **{foldername}**", color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)
    except FileNotFoundError:
      embed = nextcord.Embed(title="DelFolder", description=f"Folder **{foldername}** not found", color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="listfolder", description="Lists a folder")
  @application_checks.has_guild_permissions(administrator=True)
  async def listfolder(self, inter: nextcord.Interaction, foldername: str):
    files = os.listdir(foldername)
    embed = nextcord.Embed(title="ListFolder", description=f"**{foldername}**\n{files}", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="clearfolder", description="Clears a folder")
  @application_checks.has_guild_permissions(administrator=True)
  async def clearfolder(self, inter: nextcord.Interaction, foldername: str):
    files = os.listdir(foldername)
    for file in files:
      os.remove(file)
    embed = nextcord.Embed(title="ClearFolder", description=f"Cleared folder **{foldername}**", color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="eval", description="Evaluates code")
  @application_checks.has_guild_permissions(administrator=True)
  async def eval(self, inter: nextcord.Interaction, code: str):
    try:
      exec(code)
      embed = nextcord.Embed(title="Eval", description=f"Executed code", color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)
    except Exception as e:
      embed = nextcord.Embed(title="Eval", description=f"Error: {e}", color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="exec", description="Executes code")
  @application_checks.has_guild_permissions(administrator=True)
  async def exec(self, inter: nextcord.Interaction, code: str):
    try:
      i = exec(code)
      embed = nextcord.Embed(title="Exec", description=f"Executed code:\n{i}", color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)
    except Exception as e:
      embed = nextcord.Embed(title="Exec", description=f"Error: {e}", color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)

def setup(bot):
  bot.add_cog(Dev(bot))