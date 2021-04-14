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
    await ctx.channel.send('Concluida la votación, la película que veremos este viernes a las 20:00 horas (GMT -4, hora chilena) es **Ralph el Demoledor**. Les invitamos a todes a participar de esta actividad, donde tendremos un anuncio muy especial para todo el servidor!\n¡Les esperamos el viernes!\n<@&801508398662942790>')
    await ctx.channel.send(file=discord.File(os.path.join("/home/runner/leninv2/data/img", 'ralph.png')))


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
          await member.send("Concluida la votación, la película que veremos este viernes a las 20:00 horas (GMT -4, hora chilena) es **Ralph el Demoledor**. Les invitamos a todes a participar de esta actividad, donde tendremos un anuncio muy especial para todo el servidor!\n¡Les esperamos el viernes!")
          await member.send(file=discord.File(os.path.join("/home/runner/leninv2/data/img", 'ralph.png')))
        except Forbidden:
          pass
  
  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("notifications")

def setup(bot):
  bot.add_cog(Notifications(bot))