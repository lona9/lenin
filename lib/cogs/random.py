from discord.ext.commands import Cog
from discord.ext.commands import command
import random

class Random(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="dato", aliases=["fact", "facts", "datos"])
  async def dato(self, ctx):
    with open('/home/runner/leninv2/data/textfiles/random/datos.txt') as f:
      datos = f.read().splitlines()
      await ctx.channel.send(random.choice(datos))

  @command(name="bob", aliases=["bobesponja"])
  async def bob(self, ctx):
    with open('/home/runner/leninv2/data/textfiles/random/bob.txt') as f:
      bob = f.read().splitlines()
      await ctx.channel.send(random.choice(bob))

  @command(name="cita", aliases=["citas", "quote", "quotes"])
  async def cita(self, ctx):
    with open('/home/runner/leninv2/data/textfiles/random/citas.txt') as f:
      citas = f.read().splitlines()
      await ctx.channel.send(random.choice(citas))

  @command(name="cancion")
  async def cancion(self, ctx):
    with open('/home/runner/leninv2/data/textfiles/random/spotify.txt') as f:
      cancion = f.read().splitlines()
      await ctx.channel.send(random.choice(cancion))

  @command(name="kpop")
  async def kpop(self, ctx):
    with open('/home/runner/leninv2/data/textfiles/random/kpop.txt') as f:
      kpop = f.read().splitlines()
      await ctx.channel.send(random.choice(kpop))

  @command(name="recomendacion", aliases=["texto"])
  async def recomendacion(self, ctx):
    with open('/home/runner/leninv2/data/textfiles/random/recomendacion.txt') as f:
      recomendacion = f.read().splitlines()
      await ctx.channel.send("Si tienes tiempo libre, podrías leer **{}**.\nBúscalo en la biblioteca de Drive: https://drive.google.com/drive/folders/18uO60i2t8zkg3hlu-Mb_9D3RQD2HA_M5?usp=sharing".format(random.choice(recomendacion)))

  @command(name="suerte")
  async def suerte(self, ctx, *args):
    with open('/home/runner/leninv2/data/textfiles/random/suerte.txt') as f:
      suerte = f.read().splitlines()
      if args == ():
        await ctx.channel.send('¡Debes hacerme una pregunta para ver tu suerte!')
      else:
        await ctx.channel.send('Mi bola de cristal dice: "{}".'.format(random.choice(suerte)))

  @command(name="opinion")
  async def opinion(self, ctx, *args):
    with open('/home/runner/leninv2/data/textfiles/random/opinion.txt') as f:
      opinion = f.read().splitlines()
      if args == ():
        await ctx.channel.send('¡Debes agregar algo para poder darte mi opinión!')
      else:
          await ctx.channel.send(random.choice(opinion))

  @command(name="nezuko")
  async def nezuko(self, ctx):
    personas = ["fullsun", "dani", "flop"]
    test = ["opción 1", "opción 2", "opción 3"]

    await ctx.send("Nezuko Kamado va para...")
    await ctx.send("...")
    await ctx.send("....")
    await ctx.send(".....")
    await ctx.send("......")
    await ctx.send(".......")
    await ctx.send(f"{random.choice(personas)}!!!")


  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("random")

def setup(bot):
  bot.add_cog(Random(bot))