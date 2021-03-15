from discord.ext.commands import Cog
from discord.ext.commands import command

class Fun(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command()
  async def somecommand(self, ctx):
    pass
  
  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("fun")

def setup(bot):
  bot.add_cog(Fun(bot))