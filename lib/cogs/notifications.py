import discord
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
import os

class Notifications(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="actividad", aliases=["act"])
  async def actividad(self, ctx):
    await ctx.message.delete()
    await ctx.channel.send('Compañeres, les recordamos que hoy tendremos una nueva actividad de nuestro ciclo de formación de Latinoamérica, donde leeremos y analizaremos el texto **"Auge y caída de Sendero Luminoso"** el sábado 3 de abril a las 16:00 horas (GMT -3).\n<@&801508398662942790>\n¡Les esperamos en unas horas!\n')
    await ctx.channel.send(file=discord.File(os.path.join("/home/runner/leninv2/data/img", 'afichesendero.png')))


  #DM NOTIFICACIONES
  @command()
  async def notificaciones(self, ctx):
    with open('/home/runner/leninv2/data/textfiles/notificaciones-id.txt') as f:
      users = f.read().split(', ')
      for i in users:
        user = await self.bot.fetch_user(i)
        await user.send('Compañeres, les recordamos que hoy tendremos una nueva actividad, donde leeremos y analizaremos el texto **"Auge y caída de Sendero Luminoso"** el sábado 3 de abril a las 16:00 horas (GMT -3).\n¡Les esperamos en unas horas!\n')
        await user.send(file=discord.File(os.path.join("/home/runner/leninv2/data/img", 'afichesendero.png')))
  
  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("notifications")

def setup(bot):
  bot.add_cog(Notifications(bot))