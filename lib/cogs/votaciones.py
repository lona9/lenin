from discord.ext.commands import Cog
from discord.ext.commands import command

class Votaciones(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command()
  async def vote(self, ctx):
    await ctx.message.delete()
    msg = await ctx.channel.send("Compañeres, queremos iniciar canales en el server para poder aprender idiomas entre todes, y queremos saber en qué idiomas estarían interesades en partipar, ya sea aprendiendo desde cero o ayudando con lo que ya saben.\n\nLas opciones son las siguientes:\n:one: Chino mandarín\n:two: Portugués\n:three: Inglés\n:four: Coreano\n\nLas opciones que muestren interés de parte de la comunidad tendrán su propio canal para interactuar y aprender!")
    reacciones = ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]

    for reaction in reacciones:
      await msg.add_reaction(reaction)


  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("votaciones")

def setup(bot):
  bot.add_cog(Votaciones(bot))