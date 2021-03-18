from discord.ext.commands import Cog
from discord.utils import get

class Reactions(Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("reactions")

  @Cog.listener()
  async def on_raw_reaction_add(self, payload):
    user = payload.member

    if user == self.bot:
      return

    menor = get(user.guild.roles, name="menor")
    mayor = get(user.guild.roles, name="mayor")
    el = get(user.guild.roles, name="él")
    ella = get(user.guild.roles, name="ella")
    elle = get(user.guild.roles, name="elle/ele")
    campanita = get(user.guild.roles, name="notificaciones")

    if payload.channel_id == 801276868027482164:
      if payload.emoji.name == '🐛':
        await user.add_roles(menor)
      elif payload.emoji.name == '🦋':
        await user.add_roles(mayor)
      elif payload.emoji.name =='🥝':
        await user.add_roles(el)
      elif payload.emoji.name =='🍓':
        await user.add_roles(ella)
      elif payload.emoji.name =='🍉':
        await user.add_roles(elle)
      elif payload.emoji.name =='1️⃣':
        await user.remove_roles(menor)
      elif payload.emoji.name =='2️⃣':
        await user.remove_roles(mayor)
      elif payload.emoji.name =='3️⃣':
        await user.remove_roles(el)
      elif payload.emoji.name =='4️⃣':
        await user.remove_roles(ella)
      elif payload.emoji.name =='5️⃣':
        await user.remove_roles(elle)
      elif payload.emoji.name =='🛎️':
        await user.add_roles(campanita)

    lona = await self.bot.fetch_user(485054727755792410)

    if payload.channel_id == 801820643300474940:
      if payload.emoji.name == '🗿':
        with open('/home/runner/lenin/ayuda/ayuda2.txt') as f:
          ayuda = f.read()
          await user.send(ayuda)
          await lona.send('{} necesita ayuda con el bot'.format(user))
          
    if payload.channel_id == 801276868027482164:
      if payload.emoji.name =='🛎️':
        await lona.send('{} quiere recibir notificaciones'.format(user))
        f = open('/home/runner/lenin/roles/notificaciones-nombre.txt', 'a')
        f.write(", '<@{}>'".format(user, ', '))
        f.close()
        f = open('/home/runner/lenin/roles/notificaciones-id.txt', 'a')
        newuser = ', ' + str(user.id)
        f.write(newuser)
        f.close()

def setup(bot):
  bot.add_cog(Reactions(bot))