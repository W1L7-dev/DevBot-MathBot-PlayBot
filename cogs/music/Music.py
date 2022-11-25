from nextcord.ext import commands
from dotenv import load_dotenv
from lyricsgenius import Genius
import youtube_dl
import asyncio
import nextcord
import random
import os
import json

youtube_dl.utils.bug_reports_message = lambda: ''

YTDL_OPTIONS = {
  'format': 'bestaudio/best',
  'restrictfilenames': True,
  'noplaylist': True,
  'nocheckcertificate': True,
  'ignoreerrors': False,
  'logtostderr': False,
  'quiet': True,
  'no_warnings': True,
  'default_search': 'auto',
  'source_address': '0.0.0.0'
}

FFMPEG_OPTIONS = {
  'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)

class YTDLSource(nextcord.PCMVolumeTransformer):
  def __init__(self, source, *, data, volume=0.5):
    super().__init__(source, volume)
    self.data = data
    self.title = self.data.get('title')
    self.url = ''

  @classmethod
  async def from_url(cls, url, *, loop=None, stream=False):
    loop = loop or asyncio.get_event_loop()
    data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

    if 'entries' in data:
      data = data['entries'][0]

    filename = data['url'] if stream else ytdl.prepare_filename(data)
    return cls(nextcord.FFmpegPCMAudio(filename, **FFMPEG_OPTIONS), data=data)

class Music(commands.Cog):
  def __init__(self, bot):
    load_dotenv()
    self.bot = bot
    self.genius = Genius(os.getenv("GENIUS"))

  @nextcord.slash_command(name="join", description="Join a voice channel")
  async def join(self, inter: nextcord.Interaction):
    if inter.user.voice is None:
      embed = nextcord.Embed(description='You are not in a voice channel', color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed, ephemeral=True)
    voice_channel = inter.user.voice.channel
    if inter.guild.voice_client is None:
      await voice_channel.connect()
    else:
      await inter.guild.voice_client.move_to(voice_channel)
    embed = nextcord.Embed(description=f'Joined **{voice_channel}**', color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="leave", description="Leave a voice channel")
  async def leave(self, inter: nextcord.Interaction):
    await inter.guild.voice_client.disconnect()
    embed = nextcord.Embed(description='Left voice channel', color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="play", description="Play a song")
  async def play(self, inter: nextcord.Interaction, url: str):
    try:
      server = inter.guild
      voice_channel = server.voice_client

      async with inter.channel.typing():
        filename = await YTDLSource.from_url(url, loop=self.bot.loop)
        voice_channel.play(nextcord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
      embed = nextcord.Embed(description=f'Now playing: **{filename.title}**', color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)
    except Exception as e:
      embed = nextcord.Embed(description=f'Error: {e}', color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed, ephemeral=True)

  @nextcord.slash_command(name="pause", description="Pause a song")
  async def pause(self, inter: nextcord.Interaction):
    voice_client = inter.guild.voice_client
    if voice_client.is_playing():
      voice_client.pause()
      embed = nextcord.Embed(description='Song paused', color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)
    else:
      embed = nextcord.Embed(description='Song is not playing', color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed, ephemeral=True)

  @nextcord.slash_command(name="resume", description="Resume a song")
  async def resume(self, inter: nextcord.Interaction):
    voice_client = inter.guild.voice_client
    if voice_client.is_paused():
      voice_client.resume()
      embed = nextcord.Embed(description='Song resumed', color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)
    else:
      embed = nextcord.Embed(description='Song is not paused', color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed, ephemeral=True)

  @nextcord.slash_command(name="stop", description="Stop a song")
  async def stop(self, inter: nextcord.Interaction):
    voice_client = inter.guild.voice_client
    if voice_client.is_playing():
      voice_client.stop()
      embed = nextcord.Embed(description='Song stopped', color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)
    else:
      embed = nextcord.Embed(description='Song is not playing', color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed, ephemeral=True)

  @nextcord.slash_command(name="nowplaying", description="Get the song that is currently playing")
  async def nowplaying(self, inter: nextcord.Interaction):
    voice_client = inter.guild.voice_client
    if voice_client.is_playing():
      embed = nextcord.Embed(description=f'Now playing: **{voice_client.source.title}**', color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed)
    else:
      embed = nextcord.Embed(description='Song is not playing', color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed, ephemeral=True)

  @nextcord.slash_command(name="lyrics", description="Get lyrics of a song")
  async def lyrics(self, inter: nextcord.Interaction, *, query: str):
    try:
      async with inter.channel.typing():
        song = self.genius.search_song(query)
        embed = nextcord.Embed(title=f'Lyrics for {song.title}', description=song.lyrics, color=nextcord.Color.blurple())
        await inter.response.send_message(embed=embed)
    except Exception as e:
      embed = nextcord.Embed(description=f'Error: {e}', color=nextcord.Color.blurple())
      await inter.response.send_message(embed=embed, ephemeral=True)

  @nextcord.slash_command(name="queue", description="Get the queue")
  async def queue(self, inter: nextcord.Interaction):
    with open('queue.json', 'r') as f:
      queue = json.load(f)
    embed = nextcord.Embed(title='Queue', description=queue['queue'], color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="add", description="Add a song to the queue")
  async def add(self, inter: nextcord.Interaction, url: str):
    with open('queue.json', 'r') as f:
      queue = json.load(f)
    queue['queue'].append(url)
    with open('queue.json', 'w') as f:
      json.dump(queue, f)
    embed = nextcord.Embed(description=f'Added **{url}** to the queue', color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="remove", description="Remove a song from the queue")
  async def remove(self, inter: nextcord.Interaction, index: int):
    with open('queue.json', 'r') as f:
      queue = json.load(f)
    queue['queue'].pop(index)
    with open('queue.json', 'w') as f:
      json.dump(queue, f)
    embed = nextcord.Embed(description=f'Removed **{index}** from the queue', color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="clear", description="Clear the queue")
  async def clear(self, inter: nextcord.Interaction):
    with open('queue.json', 'r') as f:
      queue = json.load(f)
    queue['queue'].clear()
    with open('queue.json', 'w') as f:
      json.dump(queue, f)
    embed = nextcord.Embed(description='Cleared the queue', color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="shuffle", description="Shuffle the queue")
  async def shuffle(self, inter: nextcord.Interaction):
    with open('queue.json', 'r') as f:
      queue = json.load(f)
    random.shuffle(queue['queue'])
    with open('queue.json', 'w') as f:
      json.dump(queue, f)
    embed = nextcord.Embed(description='Shuffled the queue', color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="loop", description="Loop the queue")
  async def loop(self, inter: nextcord.Interaction):
    with open('queue.json', 'r') as f:
      queue = json.load(f)
    queue['loop'] = not queue['loop']
    with open('queue.json', 'w') as f:
      json.dump(queue, f)
    embed = nextcord.Embed(description=f'Loop is now **{queue["loop"]}**', color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="skip", description="Skip a song")
  async def skip(self, inter: nextcord.Interaction):
    voice_client = inter.guild.voice_client
    voice_client.stop()
    embed = nextcord.Embed(description='Song skipped', color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

  @nextcord.slash_command(name="volume", description="Change the volume")
  async def volume(self, inter: nextcord.Interaction, volume: int):
    voice_client = inter.guild.voice_client
    voice_client.source.volume = volume / 100
    embed = nextcord.Embed(description=f'Volume changed to **{volume}**', color=nextcord.Color.blurple())
    await inter.response.send_message(embed=embed)

def setup(bot):
  bot.add_cog(Music(bot))