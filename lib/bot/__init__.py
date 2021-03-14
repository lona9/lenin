from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

PREFIX = '&'

OWNER_IDS = [485054727755792410]

class Bot(BotBase):
  def __init__(self):
    self.PREFIX = PREFIX
    self.ready = False
    self.guild = None
    self.scheduler = AsyncIOScheduler()

    super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

  async def run(self, version):
    self.VERSION = version

    with open(".lib/bot/token", "r", encoding="utf-8") as tf:
      self.TOKEN = tf.read()
      print('running bot...')
      super().run(self.TOKEN, reconnect=True)

  async def on_connect(self):
    print('estoy listo, estoy listo, estoy listo')

  async def on_disconnect(self):
    print('bot offline')

  async def on_ready(self):
    if not self.ready:
      self.ready = True
      self.guild = self.get_guild(716064319938494545)
      print("bot ready")

    elif:
      print("bot reconnected")

  async def on_message(self, message):
    pass

bot = Bot()


