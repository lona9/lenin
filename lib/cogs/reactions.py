from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.utils import get
from discord import Embed

class Reactions(Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("reactions")

  @command(name="pais")
  async def pais(self, ctx):
    paises = await ctx.channel.send("Para agregarte un rol de acuerdo a tu nacionalidad/país de residencia, haz click en la bandera del país que corresponda.")
    banderas = ["🇦🇷", "🇧🇴", "🇧🇷", "🇨🇱", "🇨🇴", "🇪🇨", "🇺🇸", "🇲🇽", "🇵🇾", "🇵🇪", "🇻🇪"]
    for i in banderas:
      await paises.add_reaction(i)

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
    argentina = get(user.guild.roles, name="argentina")
    bolivia = get(user.guild.roles, name="bolivia")
    brasil = get(user.guild.roles, name="brasil")
    chile = get(user.guild.roles, name="chile")
    colombia = get(user.guild.roles, name="colombia")
    ecuador = get(user.guild.roles, name="ecuador")
    estados_unidos = get(user.guild.roles, name="estados unidos")
    mexico = get(user.guild.roles, name="méxico")
    paraguay = get(user.guild.roles, name="paraguay")
    peru = get(user.guild.roles, name="perú")
    venezuela = get(user.guild.roles, name="venezuela")
    spain = get(user.guild.roles, name="españa")

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
      elif payload.emoji.name == '🇦🇷':
        await user.add_roles(argentina)
      elif payload.emoji.name == '🇧🇴':
        await user.add_roles(bolivia)
      elif payload.emoji.name == '🇧🇷':
        await user.add_roles(brasil)
      elif payload.emoji.name == '🇨🇱':
        await user.add_roles(chile)
      elif payload.emoji.name == '🇨🇴':
        await user.add_roles(colombia)
      elif payload.emoji.name == '🇪🇨':
        await user.add_roles(ecuador)
      elif payload.emoji.name == '🇺🇸':
        await user.add_roles(estados_unidos)
      elif payload.emoji.name == '🇲🇽':
        await user.add_roles(mexico)
      elif payload.emoji.name == '🇵🇾':
        await user.add_roles(paraguay)
      elif payload.emoji.name == '🇵🇪':
        await user.add_roles(peru)
      elif payload.emoji.name == '🇻🇪':
        await user.add_roles(venezuela)
      elif payload.emoji.name == '🇪🇸':
        await user.add_roles(spain)

    self.leninlog = self.bot.get_channel(829158432925024287)
    channel = self.leninlog

    if payload.channel_id == 801820643300474940:
      if payload.emoji.name == '🗿':
        embed = Embed(colour=0xFF0000)

        fields = [("¡Hola!", "Soy el bot de **Orbitburó en Español** y ¡estoy aquí para guiarte! <:chuu:716783609763069962>", False), ("Vi que tenías dudas sobre cómo usarme, aquí te dejo algunos comandos que te podrían servir. Para utilizar cualquier comando, solo debes escribir la palabra (con & adelante siempre).\nIntenta con los siguientes comandos para ver más información:","\u200B\n**&ayuda**: ¡estás aquí!\n**&comandos**: lista de comandos disponibles para interactuar conmigo\n**&canales**: lista de todos los canales y sus descripciones\n\u200B", False), ("¿Dónde usarme?", "Puedes usarme en todos los canales abiertos, excepto en los canales específicos para otros bots, o en esta misma conversación.", False)]

        for name, value, inline in fields:
          embed.add_field(name=name, value=value, inline=inline)
        
        embed.set_author(name='lenin', icon_url="https://cdn.discordapp.com/attachments/716135897476628521/822171692494618624/logodegradooo.png")

        embed.set_footer(text="Si presento problemas o necesitas más ayuda, menciona o envía un mensaje a @lona")

        await user.send(embed=embed)

        await self.leninlog.send('{} necesita ayuda con el bot'.format(user))
          
    if payload.channel_id == 801276868027482164:
      if payload.emoji.name =='🛎️':
        await self.leninlog.send('{} quiere recibir notificaciones'.format(user))
        f = open('/home/runner/leninv2/data/textfiles/notificaciones-nombre.txt', 'a')
        f.write(", '<@{}>'".format(user, ', '))
        f.close()
        f = open('/home/runner/leninv2/data/textfiles/notificaciones-id.txt', 'a')
        newuser = ', ' + str(user.id)
        f.write(newuser)
        f.close()

def setup(bot):
  bot.add_cog(Reactions(bot))