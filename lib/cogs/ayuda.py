from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed

class Ayuda(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="ayuda", aliases=["info"])
  async def ayuda(self, ctx):
    
    embed = Embed(colour=0xFF0000)

    fields = [("¡Hola!", "Soy el bot de **Orbitburó en Español** y ¡estoy aquí para guiarte! <:chuu:716783609763069962>", False),
      ("Escribe los siguientes comandos para pedir más información:","\u200B\n**&ayuda**: ¡estás aquí!\n**&comandos**: lista de comandos disponibles para interactuar conmigo\n**&canales**: lista de todos los canales y sus descripciones\n\u200B", False),
      ("¿Dónde usarme?", "Puedes usarme en todos los canales abiertos, excepto en los canales específicos para otros bots: <#774806561465565194>, <#774730648774246431>, <#716081709296255077> y <#731919940533223514>", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)
    embed.set_author(name='lenin', icon_url="https://cdn.discordapp.com/attachments/716135897476628521/822171692494618624/logodegradooo.png")
    embed.set_footer(text="Si presento problemas o necesitas más ayuda, menciona o envía un mensaje a @lona")

    await ctx.channel.send(embed=embed)

  @command(name="comandos", aliases=["comando"])
  async def comandos(self, ctx):

    embed = Embed(title="Lista de comandos", colour=0xFF0000)
    
    fields = [("\u200B", "Estos son los comandos que puedes utilizar y sus funciones:", False),
      ("**__Servidor__**","**&canales:** Resumen de los canales del servidor.\n**&buscar**: Busca actividades usando una palabra clave relacionada (ejemplo: &buscar marxismo)\n**&siguiente**: Detalles de la próxima actividad a realizar.\n**&ultima**: Detalles de la última actividad realizada.\n**&drive**: Link para la carpeta de Drive del servidor.\n**&playlist**: Link para la playlist en Spotify de Orbitburó en español.\n**&invitacion**: Envía un DM con un link de invitación al server que caduca en 24 horas.\n**&redes**: Links de las redes sociales del servidor.", False),
      ("**__Al azar__**", "**&cita**: Citas de autores famosos al azar.\n**&dato**: Datos curiosos de izquierda al azar.\n**&bobesponja**: Citas de Bob Esponja al azar.\n**&kpop**: Canción de kpop al azar.\n**&cancion**: Canción en Spotify de la playlist de OrbitBuró en español al azar.\n**&recomendacion**: Texto de nuestra biblioteca en Drive al azar", False), 
      ("**__Misceláneos__**", "**&hora**: Hora actual en distintas zonas horarias.\n**&suerte**: Mira tu futuro haciendo una pregunta luego del comando (ejemplo: &suerte llegaremos al socialismo este año?)\n**&opinion**: Pregúntame tu opinión de alguien (ejemplo: &opinion vivi from loona)", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)
    embed.set_author(name='lenin', icon_url="https://cdn.discordapp.com/attachments/716135897476628521/822171692494618624/logodegradooo.png")
    embed.set_footer(text="Si presento problemas o necesitas más ayuda, menciona o envía un mensaje a @lona")

    await ctx.channel.send(embed=embed)
  
  @command(name="canales", aliases=["canal"])
  async def canales(self, ctx):

    embed = Embed(title="Lista de canales", colour=0xFF0000)
    fields = [("<:haseul2:716798819739762728>", "¿No sabes dónde ir? Te recordamos para qué sirve cada canal en caso de que necesites ayuda:", False),
      ("**__Sección Importantes__**", "<#716068304162258954>: Canal con las reglas del servidor\n<#716076222517608499>: Canal para anuncios importantes. NO SILENCIAR\n<#765349189692817408>: Canal con el resumen de las actividades ya realizadas y por realizar\n<#801276868027482164>: Canal para modificar tus roles\n<#801820643300474940>: Canal para votaciones del servidor", False),
      ("**__Sección Política__**", "<#716081691684241493>: Canal para discusión política en general\n<#716081838908506172>: Canal para subir recursos audiovisuales\n<#723974654548770898>: Canal donde se eligen futuras actividades mediante votación o discusión\n<#716081744390127717>: Canal para llevar a cabo discusiones durante las actividades)", False),
      ("**__Sección Off-topic__**", "<#775731002890518588>: Canal para hablar de cualquier tema\n<#775731090375311400>: Canal para hablar sobre juegos\n<#816493090449653760>: Canal para hablar sobre música\n<#716081709296255077>: Canal para utilizar el bot Chuu\n<#774806561465565194>: Canal para jugar EPIC RPG\n<#774730648774246431>: Canal para jugar Mudae\n<#731919940533223514>: Canal para comandos del reproductor de música", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)
    embed.set_author(name='lenin', icon_url="https://cdn.discordapp.com/attachments/716135897476628521/822171692494618624/logodegradooo.png")
    embed.set_footer(text="Si presento problemas o necesitas más ayuda, menciona o envía un mensaje a @lona")

    await ctx.channel.send(embed=embed)

  @command(name="siguiente", aliases=["proxima"])
  async def siguiente(self, ctx):
    
    embed = Embed(title="Siguiente actividad", colour=0xFF0000)

    fields = [("Sesión", "5", True), ("Ciclo", "Tercer ciclo", True), ("Fecha", "Por definir", True), 
    ("Texto", "Por definir", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    embed.set_author(name='lenin', icon_url="https://cdn.discordapp.com/attachments/716135897476628521/822171692494618624/logodegradooo.png")

    await ctx.channel.send(embed=embed)

  @command(name="ultima", aliases=["anterior"])
  async def ultima(self, ctx):
    
    embed = Embed(title="Última actividad", colour=0xFF0000)

    fields = [("Sesión", "4", True), ("Ciclo", "Tercer ciclo", True), ("Fecha", "13 de marzo", True), 
    ("Texto", "'Comunismo y anticomunismo en Colombia en los inicios de la guerra fría'", False),
    ("Autor", "Luis Trejos Rosero", False),
    ("Carpeta Drive", "https://drive.google.com/drive/folders/1z7i5z0MvfpJbRQMiY15LmqGshC3zQwDy?usp=sharing", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    embed.set_author(name='lenin', icon_url="https://cdn.discordapp.com/attachments/716135897476628521/822171692494618624/logodegradooo.png")

    await ctx.channel.send(embed=embed)

  @command(name="drive")
  async def drive(self, ctx):
    embed = Embed(title="Link del Drive", colour=0xFF0000)
    fields =[("¿Buscas el link para la carpeta de Drive? ¡Acá está!", "https://drive.google.com/drive/folders/1o_xuNEuH_xNnO6LWFWXJ8XqlS2TNQ6Jy?usp=sharing", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    embed.set_footer(text="Si no estás segure de dónde está lo que buscas, revisa #calendario para ver el detalle de las actividades realizadas.")
    embed.set_author(name='lenin', icon_url="https://cdn.discordapp.com/attachments/716135897476628521/822171692494618624/logodegradooo.png")

    await ctx.channel.send(embed=embed)

  @command(name="playlist", aliases=["spotify"])
  async def playlist(self, ctx):
    embed = Embed(title="Playlist oficial de Orbitburó", colour=0xFF0000)
    fields =[("¿Buscas el link de la playlist de Spotify? ¡Acá está!", "https://open.spotify.com/playlist/3ZcCDnPcEucCnZWNe1Yjcq?si=0tIICg21QlGf-AwWlNrr4w", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    embed.set_author(name='lenin', icon_url="https://cdn.discordapp.com/attachments/716135897476628521/822171692494618624/logodegradooo.png")

    await ctx.channel.send(embed=embed)


  @command(name='invitacion', aliases=["invite"])
  async def invitacion(self, ctx, *argument):
    invitelink = await ctx.channel.create_invite(max_age=86400,unique=True)

    await ctx.author.send('¡Aquí está el link de invitación al servidor que pediste! Debes usarlo en las siguientes 24 horas antes de que expire. ')
    await ctx.author.send(invitelink)

  @command(name="redes", aliases=["rrss"])
  async def redes(self, ctx):

    embed = Embed(title="Redes sociales de Orbitburó", colour=0xFF0000)
    fields =[("Síguenos en nuestras redes sociales", "**Twitter**: https://www.twitter.com/OrbitburoES\n**Instagram:** https://www.instagram.com/OrbitburoES", False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    embed.set_author(name='lenin', icon_url="https://cdn.discordapp.com/attachments/716135897476628521/822171692494618624/logodegradooo.png")

    await ctx.channel.send(embed=embed)

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("ayuda")

def setup(bot):
  bot.add_cog(Ayuda(bot))