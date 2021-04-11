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
    await ctx.channel.send('Recuerden que les compañeres del podcast Voces Andinas extienden la invitación a todo el server para **comentar los resultados electorales de Perú y Ecuador 2021** hoy domingo 11 de abril, a las 19 horas (Perú/Ecuador), 20 horas (Chile).\nLa transmisión se hará en paralelo por YouTube y en el server.\n¡Les esperamos en unas horas!\n<@&801508398662942790>')
    await ctx.channel.send(file=discord.File(os.path.join("/home/runner/leninv2/data/img", 'orbitburovocesandinas.png')))


  #DM NOTIFICACIONES
  @command()
  async def notificaciones(self, ctx):
    with open('/home/runner/leninv2/data/textfiles/notificaciones-id.txt') as f:
      users = f.read().split(', ')
      for i in users:
        user = await self.bot.fetch_user(i)
        print(user.name)
        try:
          await user.send('text')
        except Forbidden:
          pass

  
  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("notifications")

def setup(bot):
  bot.add_cog(Notifications(bot))