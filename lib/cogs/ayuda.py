from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed

class Ayuda(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="ayuda", aliases=["info"])
  async def ayuda(self, ctx):

    # self.guild = self.get_guild(716064319938494545)
    embed = Embed(colour=0xFF0000)

    fields = [("¡Hola!", "Soy el bot de **Orbitburó en Español** y ¡estoy aquí para guiarte! <:chuu:716783609763069962>", False),
      ("Información", "Escribe los siguientes comandos para pedir más información:", False),
      ("&ayuda", "¡estás aquí!", False),
      ("&comandos", "lista de comandos disponibles para interactuar conmigo", False),
      ("&canales", "lista de todos los canales y sus descripciones", False),
      ("¿Dónde usarme?", "Puedes usarme en todos los canales abiertos, incluso por DM, excepto en los canales específicos para otros bots: <#774806561465565194>, <#774730648774246431>, <#716081709296255077> y <#731919940533223514>.", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)
    embed.set_author(name='lenin', icon_url="https://cdn.discordapp.com/attachments/716135897476628521/822171692494618624/logodegradooo.png")
    embed.set_footer(text="Si presento problemas o necesitas más ayuda, menciona o envía un mensaje a @lona")

    await ctx.channel.send(embed=embed)
  
  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("ayuda")

def setup(bot):
  bot.add_cog(Ayuda(bot))