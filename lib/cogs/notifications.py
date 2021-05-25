import discord
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Forbidden
from discord import Embed
import os

class Notifications(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="actividad", aliases=["act"])
  async def actividad(self, ctx):
    await ctx.message.delete()
    await ctx.channel.send("Compañeres, les invitamos a la última actividad de nuestro ciclo de Latinoamérica, el cual finalizaremos con una discusión sobre el paro nacional en Colombia, este sábado 29 de mayo a las 18:00 (GMT -4, hora chilena).\n¡Les esperamos este sábado para culminar el ciclo!\n<@&801508398662942790>")
    await ctx.channel.send(file=discord.File(os.path.join("/root/lenin/data/img/", "colombiatwt.png")))

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
              await member.send("Compañeres, les invitamos a la última actividad de nuestro ciclo de Latinoamérica, el cual finalizaremos con una discusión sobre el paro nacional en Colombia, este sábado 29 de mayo a las 18:00 (GMT -4, hora chilena).\n¡Les esperamos este sábado para culminar el ciclo!")
              await member.send(file=discord.File(os.path.join("/root/lenin/data/img/", "colombiatwt.png")))
          except Forbidden:
              pass

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("notifications")

def setup(bot):
  bot.add_cog(Notifications(bot))
