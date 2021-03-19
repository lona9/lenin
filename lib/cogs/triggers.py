from discord.ext.commands import Cog
from discord.utils import get
import random

class Triggers(Cog):
  def __init__(self, bot):
    self.bot = bot

  @Cog.listener()
  async def on_message(self, message):
    if not message.author.bot:

      msg = message.content

      if 'leamos' in msg.lower() or 'leido' in msg.lower() or 'lee' in msg.lower() or 'leiste' in msg.lower() or 'leyó' in msg.lower() or 'lei' in msg.lower() or 'leyendo' in msg.lower():
        await message.channel.send('¿Alguien dijo leer? ¡Recuerda leer el texto de la próxima actividad!')

      if 'trotsk' in msg.lower() or 'trosk' in msg.lower():
        await message.channel.send(':pick:')

      if 'lenin' in msg.lower():
        autolenin = ['¿Están hablando de mí?', '¿Me buscaban?', '¿Alguien dijo mi nombre?', '¡Sí, aquí estoy!', 'No es lindo hablar de alguien a sus espaldas.', '¿Yo qué?', '¿Qué pasa conmigo?', 'Ese es mi nombre, no lo gastes.']
        await message.channel.send(random.choice(autolenin))

      if ' pena' in msg.lower() or 'pena ' in msg.lower() or ' sad ' in msg.lower() or msg.endswith('sad') or 'sad' == msg.lower() or 'sad ' in msg.lower() or 'sadd' in msg.lower() or 'triste' in msg.lower() or 'llorar' in msg.lower() or 'tot' == msg.lower() or msg.endswith('tot'):
          await message.channel.send('tkm no estés triste')

      if ' feliz' in msg.lower():
          await message.channel.send('yo también bestie!')

      if 'cumpleaños' in msg.lower():
          await message.channel.send('¿Quién está de cumpleaños? ¡Feliz cumpleaños, camarada! :partying_face:')

      if 'anticomunismo' in msg.lower() or 'anticomunista' in msg.lower():
        await message.channel.send('<:yeojin2:716798849464795260>')

      if 'blackpink' in msg.lower():
        await message.channel.send('RS1 IS COMING')

      self.reprmusica = self.bot.get_channel(731919940533223514)
      self.secgen = self.bot.get_channel(716135897476628521)
      self.pruebot = self.bot.get_channel(800131110989463592)

      if msg.startswith('!p'):
        if message.channel == self.secgen:
          return
        elif message.channel == self.pruebot:
          return
        elif message.channel != self.reprmusica:
          await message.channel.send('Los comandos del bot de música deben ser enviados en el canal de <#731919940533223514>.')

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("triggers")

def setup(bot):
  bot.add_cog(Triggers(bot))