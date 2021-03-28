import discord
from keep_alive import keep_alive
from asyncio import sleep
from discord import Intents
from datetime import datetime
from glob import glob
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord import Embed, File
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import Context
from discord.ext.commands import CommandNotFound
from ..db import db

PREFIX = '&'

OWNER_IDS = [485054727755792410]

COGS = ["utility", "reactions", "ayuda", "meta", "random", "triggers", "log", "buscar", "cal", "notifications", "info"]

class Ready(object):
  def __init__(self):
    for cog in COGS:
      setattr(self, cog, False)

  def ready_up(self, cog):
    setattr(self, cog, True)
    print(f" {cog} cog ready")

  def all_ready(self):
    return all([getattr(self, cog) for cog in COGS])


class Bot(BotBase):
  def __init__(self):
    self.PREFIX = PREFIX
    self.ready = False
    self.cogs_ready = Ready()
    self.guild = None
    self.scheduler = AsyncIOScheduler()

    intents = Intents.default()
    intents.members = True

    db.autosave(self.scheduler)

    super().__init__(
      command_prefix=PREFIX, 
      owner_ids=OWNER_IDS,
      intents=Intents.all()
      )

  def setup(self):
    for cog in COGS:
      self.load_extension(f"lib.cogs.{cog}")
      print(f" {cog} cog loaded")

    print("setup complete") 

  def run(self, version):
      self.VERSION = version

      print("running setup...")
      self.setup()

      with open("./lib/bot/.env", "r", encoding="utf-8") as tf:
        self.TOKEN = tf.read()

      print('running bot...')
      super().run(self.TOKEN, reconnect=True)

  async def process_commands(self, message):
    ctx = await self.get_context(message, cls=Context)

    if ctx.command is not None:
      if self.ready:
        await self.invoke(ctx)
    
      else:
        await ctx.send("Aún no estoy listo para recibir comandos, por favor espera unos segundos.")

  async def on_connect(self):
    print('bot connected')

  async def on_disconnect(self):
    print('bot offline')

  async def on_error(self, err, *args, **kwargs):
    if err == "on_command_error":
      pass

    await self.pruebot.send("Ocurrió un error.")

    raise

  async def on_command_error(self, ctx, exc):
    if isinstance(exc, CommandNotFound):
      pass

    elif hasattr(exc, "original"):
      raise exc

    else:
      raise exc

  async def on_ready(self):
    if not self.ready:
      
      # self.guild = self.get_guild(716064319938494545)
      self.pruebot = self.get_channel(800131110989463592)
      channel = self.pruebot

      await self.pruebot.send("Estoy listo, estoy listo, estoy listo, estoy listo!")
      self.ready = True
      print("bot ready")

      meta = self.get_cog("Meta")
      await meta.set()

    else:
      print("bot reconnected")

  async def on_message(self, message):
      
    if not message.author.bot:
      await self.process_commands(message)

keep_alive()

bot = Bot()



