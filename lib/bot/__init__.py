from discord import Intents
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed
from discord.ext.commands import Bot as BotBase

PREFIX = '&'

OWNER_IDS = [485054727755792410]

class Bot(BotBase):
  def __init__(self):
    self.PREFIX = PREFIX
    self.ready = False
    self.guild = None
    self.scheduler = AsyncIOScheduler()

    intents = Intents.default()
    intents.members = True


    super().__init__(
      command_prefix=PREFIX, 
      owner_ids=OWNER_IDS,
      intents=Intents.all()
      )

  def run(self, version):
      self.VERSION = version

      with open("./lib/bot/.env", "r", encoding="utf-8") as tf:
        self.TOKEN = tf.read()

      print('running bot...')
      super().run(self.TOKEN, reconnect=True)

  async def on_connect(self):
    print('bot connected')

  async def on_disconnect(self):
    print('bot offline')

  async def on_ready(self):
    if not self.ready:
      self.ready = True
      self.guild = self.get_guild(716064319938494545)
      print("bot ready")

      channel = self.get_channel(800131110989463592)
      await channel.send("Now online!")

      embed = Embed(title="Comunismo y anticomunismo en Colombia", colour=0xFF0000, timestamp=datetime.utcnow())

      fields = [("Sesión", "4", True),
      ("Ciclo", "Tercer ciclo", True),
      ("Fecha", "13 de marzo", True),
      ("Texto", "'Comunismo y anticomunismo en Colombia en los inicios de la guerra fría'", False),
      ("Autor", "Luis Trejos Rosero", False)]

      for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
      embed.set_author(name="lona", icon_url=self.guild.icon_url)
      embed.set_footer(text="Drive: https://drive.google.com/drive/folders/1z7i5z0MvfpJbRQMiY15LmqGshC3zQwDy?usp=sharing")

      await channel.send(embed=embed)

      

    else:
      print("bot reconnected")

  async def on_message(self, message):
    pass

bot = Bot()


