from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
from random import choice, randint
import pendulum
import datetime
from datetime import datetime

class Utility(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="dice", aliases=["dado", "roll"])
  async def roll_dice(self, ctx, die_string: str):
    dice, value = (int(term) for term in die_string.split("d"))
    rolls = [randint(1, value) for i in range(dice)]

    await ctx.send(" + ".join([str(r) for r in rolls]) + f" = {sum(rolls)}")

  @command(name="eco", aliases=["echo"])
  async def eco(self, ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)

  @command(name="hora", aliases=["reloj", "clock"])
  async def hora(self, ctx):

  # TIMEZONES
    tz_CL = pendulum.timezone('America/Santiago')
    datetime_CL = datetime.now(tz_CL)

    tz_PE = pendulum.timezone('America/Lima')
    datetime_PE = datetime.now(tz_PE)

    tz_BO = pendulum.timezone('America/La_Paz')
    datetime_BO = datetime.now(tz_BO)

    tz_JP = pendulum.timezone('Asia/Tokyo')
    datetime_JP = datetime.now(tz_JP)

    tz_MX = pendulum.timezone('America/Mexico_City')
    datetime_MX = datetime.now(tz_MX)

    hora = (":flag_mx: (CDMX) **(GMT -6): **", datetime_MX.strftime("%H:%M:%S"), "\n", ":flag_pe: :flag_ec: :flag_co: **(GMT -5): **", datetime_PE.strftime("%H:%M:%S"), "\n", ":flag_bo: :flag_ve: **(GMT -4): **", datetime_BO.strftime("%H:%M:%S"), "\n", ":flag_ar: :flag_cl: :flag_br: :flag_uy: :flag_py: **(GMT -3) : **", datetime_CL.strftime("%H:%M:%S"), "\n", ":flag_kr: :flag_jp: **(GMT +9): **", datetime_JP.strftime("%H:%M:%S"))

    hora = "".join(hora)

    embed = Embed(title="Reloj", colour=0xFF0000)
    fields =[("La hora actual es:", hora, False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    embed.set_author(name='lenin', icon_url="https://cdn.discordapp.com/attachments/716135897476628521/822171692494618624/logodegradooo.png")

    await ctx.channel.send(embed=embed)
  
  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("utility")

def setup(bot):
  bot.add_cog(Utility(bot))