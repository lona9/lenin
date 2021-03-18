from discord.ext.commands import Cog
from discord.ext.commands import command
from random import choice, randint

class Fun(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="hello", aliases=["hi", "hola"])
  async def somecommand(self, ctx):
    await ctx.channel.send(f'holi {ctx.author.mention}!')

  @command(name="dice")
  async def roll_dice(self, ctx, die_string: str):
    dice, value = (int(term) for term in die_string.split("d"))
    rolls = [randint(1, value) for i in range(dice)]

    await ctx.send(" + ".join([str(r) for r in rolls]) + f" = {sum(rolls)}")
  
  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("fun")

def setup(bot):
  bot.add_cog(Fun(bot))