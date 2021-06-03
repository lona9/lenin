import discord
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Forbidden
from discord import Embed
import os

class Notifications(Cog):
  def __init__(self, bot):
    self.bot = bot

  ## INFOGRAFIA ANIVERSARIO
  @command(name="anni", aliases=["aniversario"])
  async def anni(self, ctx):
    await ctx.message.delete()
    await ctx.channel.send("Camaradas, hemos recopilado distintas estadísticas de nuestro server a lo largo de este año que queremos compartir con todes, estamos felices de estar a días de cumplir un año desde la primera vez que nos juntamos a discutir de política! Les compartimos una infografía de los números más relevantes del server, así como un word cloud construido con todos los mensajes del canal <#716081744390127717>.\nNo olvidar que este sábado 5 de junio nos juntamos a las 14:00 (GMT -4, hora chilena) para hablar sobre **Kpop y marxismo** y celebrar nuestro primer aniversario!\n<@&716089943130243092>")
    await ctx.channel.send(file=discord.File(os.path.join("/root/lenin/data/img/", "estadisticas.png")))
    await ctx.channel.send(file=discord.File(os.path.join("/root/lenin/data/img/", "orbitburo.png")))

  ## MENSAJE SERVER
  @command(name="actividad", aliases=["act"])
  async def actividad(self, ctx):
    await ctx.message.delete()
    await ctx.channel.send("Les recordamos este sábado 5 de junio a las 14:00 horas (GMT -4, hora chilena) tendremos nuestra actividad de aniversario, donde discutiremos sobre **Kpop y marxismo**, en conmemoración a los dos grandes temas que engloban a OrbitBuró en Español.\n¡Les esperamos este sábado para la celebración!\n<@&801508398662942790>")
    await ctx.channel.send(file=discord.File(os.path.join("/root/lenin/data/img/", "aniversario_orbitburo.png")))

  #DM NOTIFICACIONES
  @command()
  async def notificaciones(self, ctx):
    guild = ctx.message.guild
    for role in guild.roles:
      if role.name == "notificaciones":
        role_id = role
        break

    for member in guild.members:
      if role_id in member.roles:
          try:
              await member.send("Les recordamos este sábado 5 de junio a las 14:00 horas (GMT -4, hora chilena) tendremos nuestra actividad de aniversario, donde discutiremos sobre **Kpop y marxismo**, en conmemoración a los dos grandes temas que engloban a OrbitBuró en Español.\n¡Les esperamos este sábado para la celebración!")
              await member.send(file=discord.File(os.path.join("/root/lenin/data/img/", "aniversario_orbitburo.png")))
          except Forbidden:
              pass

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("notifications")

def setup(bot):
  bot.add_cog(Notifications(bot))
