from discord.ext.commands import Cog
from discord import Embed
from discord.ext.commands import command

class Buscar(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="buscar")
  async def buscar(self, ctx, *args):

    self.ctx = ctx

    if args == ():
      await ctx.channel.send('Debes escribir una palabra clave para que pueda buscar')

    else:
      message = str(' '.join(args).lower())

      fields1 = [("Sesión", "1", True),
                  ("Ciclo", "Primer ciclo", True),
                  ("Fecha", "6 de junio de 2020", True),
                  ("Texto", "Capítulos 1-3 - ¿Qué es el Marxismo Leninismo Maoísmo? de *Marxismo-leninismo-maoísmo: Curso básico*", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/folders/1PSdO_boRaNHdLMjEBRwXHq7OzRL7rXuS", False)]

      fields2 = [("Sesión", "2", True),
                  ("Ciclo", "Primer ciclo", True),
                  ("Fecha", "20 de junio de 2020", True),
                  ("Texto", "Capítulos 5-7 - Tres fuentes del marxismo de *Marxismo-leninismo-maoísmo: Curso básico*", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/folders/1Uf2fTz752QiRv3HQoRVVEkGvETGNVGEf", False)]

      fields3 = [("Sesión", "3", True),
                  ("Ciclo", "Primer ciclo", True),
                  ("Fecha", "11 de julio de 2020", True),
                  ("Texto", "Parte 1: Burgueses y proletarios del *Manifiesto Comunista*", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/folders/1hms3YbrbYRhy0wS6ckcFcwxWvBh7CDWi", False)]

      fields4 = [("Sesión", "4", True),
                  ("Ciclo", "Primer ciclo", True),
                  ("Fecha", "25 de julio de 2020", True),
                  ("Documental", "Chicago Boys", False),
                  ("Recursos adicionales", "No disponibles", False)]

      fields5 = [("Sesión", "5", True),
                  ("Ciclo", "Primer ciclo", True),
                  ("Fecha", "1 de agosto de 2020", True),
                  ("Documental", "Mini-serie 'Desmitificando China'", False),
                  ("Link de YouTube", "https://www.youtube.com/playlist?list=PLT3D1aiytzdlRayJOj9ibTKAyqOeYqVQ9", False)]

      fields6 = [("Sesión", "6", True),
                  ("Ciclo", "Primer ciclo", True),
                  ("Fecha", "15 de agosto de 2020", True),
                  ("Texto", "Capítulo 1: Contraatacando desde la cocina de *El patriarcado del salario*", False),
                  ("Autora", "Silvia Federici", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/folders/1H7io2vjRjCgmZYJOQ4pPldO1xBegtpBP", False)]

      fields7 = [("Sesión", "7", True),
                  ("Ciclo", "Primer ciclo", True),
                  ("Fecha", "29 de agosto de 2020", True),
                  ("Texto", "Más allá de la sociedad disciplinaria de *La Sociedad del Cansancio*", False),
                  ("Autor", "Byungchul Han", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/folders/1iCXKbQ1hl2HV6WkD1y-8tuzGt-T3hQ89", False)]

      fields8 = [("Sesión", "8", True),
                  ("Ciclo", "Primer ciclo", True),
                  ("Fecha", "5 de Septiembre de 2020", True),
                  ("Documental", "La Batalla de Chile: El poder popular", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/folders/1IXj_DiVo9_n96zzXZAsaj_38U0A5OLyX", False)]

      fields9 = [("Sesión", "9", True),
                  ("Ciclo", "Primer ciclo", True),
                  ("Fecha", "12 de Septiembre de 2020", True),
                  ("Documental", "La Batalla de Chile: El golpe de Estado", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/folders/1YyqhoJFMdjqVZlV0k4ktyJ6tEIBxUu6W", False)]

      fields10 = [("Sesión", "1", True),
                  ("Ciclo", "Segundo ciclo", True),
                  ("Fecha", "26 de Septiembre de 2020", True),
                  ("Texto", "Sobre el materialismo dialéctico y el materialismo histórico", False),
                  ("Autor", "Iosef Stalin", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/u/2/folders/1xLHJhI08TvDZpxzr8GFAVJasmj1qw0Yv", False)]

      fields11 = [("Sesión", "2", True),
                  ("Ciclo", "Segundo ciclo", True),
                  ("Fecha", "10 de octubre de 2020", True),
                  ("Texto", "Explotación capitalista", False),
                  ("Autora", "Marta Harnecker", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/u/2/folders/1ISNsLouPoGb0VgrpngIR7OHB-_Q1uagU", False)]

      fields12 = [("Sesión", "3", True),
                  ("Ciclo", "Segundo ciclo", True),
                  ("Fecha", "24 de octubre de 2020", True),
                  ("Documental", "Revolución rusa: Ellos se atrevieron", False),
                  ("Link documental", "https://www.youtube.com/watch?v=M51ZZ9ApCtw", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/folders/1039uf5TmOKeBn1hQg3dhGRUKRL_RpFGO?usp=sharing", False)]

      fields13 = [("Sesión", "4", True),
                  ("Ciclo", "Segundo ciclo", True),
                  ("Fecha", "7 de noviembre de 2020", True),
                  ("Texto", "La enfermedad infantil del izquierdismo en el comunismo", False),
                  ("Autor", "Vladimir Ilich Lenin", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/u/2/folders/1IK2Bz4uYlKOVMiucUJNPOi_yQbnz2HNA", False)]

      fields14 = [("Sesión", "5", True),
                  ("Ciclo", "Segundo ciclo", True),
                  ("Fecha", "21 de noviembre de 2020", True),
                  ("Texto", "Tendencias filosóficas en el movimiento feminista", False),
                  ("Autora", "Anuradha Ghandy", False),
                  ("Link del texto", " https://www.marxists.org/espanol/ghandy/2006/tendencias-filosoficas-movfem.htm", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/folders/1eRH_6fCKItYrx-d7QWvOSEtOyMZhU8x3?usp=sharing", False)]

      fields15 = [("Sesión", "6", True),
                  ("Ciclo", "Segundo ciclo", True),
                  ("Fecha", "19 de diciembre de 2020", True),
                  ("Texto", "Revolución China, Capítulos 25 al 31 de *Marxismo-leninismo-maoísmo: Curso básico*", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/folders/1fRMV5aggpwD1Xty2QeeT0fIh8B9_AW1T?usp=sharing", False)]

      fields16 = [("Sesión", "7", True),
                  ("Ciclo", "Segundo ciclo", True),
                  ("Fecha", "16 de enero de 2021", True),
                  ("Documental", "Ciudadanes leales de Pyongyang en Seúl", False),
                  ("Link del documental", "https://www.youtube.com/watch?v=ktE_3PrJZO0", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/folders/1xGyB0VckETnJOUU7t5lS6ubToXFU9wlC?usp=sharing", False)]

      fields17 = [("Sesión", "1", True),
                  ("Ciclo", "Tercer ciclo", True),
                  ("Fecha", "30 de enero de 2021", True),
                  ("Documental", "4 Lonkos: Vida, muerte y profanación", False),
                  ("Link del documental", "https://vimeo.com/323817586", False)]

      fields18 = [("Sesión", "2", True),
                  ("Ciclo", "Tercer ciclo", True),
                  ("Fecha", "13 de febrero de 2021", True),
                  ("Texto", "El problema del indio y El problema de la tierra de *7 ensayos de interpretación de la realidad peruana*", False),
                  ("Autor", "José Carlos Mariátegui", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/folders/1wRBrThyKV47wxTZw9kn1IHl0XgpcrkPR?usp=sharing", False)]

      fields19 = [("Sesión", "3", True),
                  ("Ciclo", "Tercer ciclo", True),
                  ("Fecha", "27 de febrero de 2021", True),
                  ("Documental", "Cubanas: Mujeres en Revolución", False),
                  ("Link del documental", "https://youtu.be/IXdgfuK8j_8", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/folders/1L9349HsOCO4nHSE9rgpANjA7MJhPPf8R?usp=sharing", False)]

      fields20 = [("Sesión", "4", True),
                  ("Ciclo", "Tercer ciclo", True),
                  ("Fecha", "13 de marzo de 2021", True),
                  ("Texto", "Comunismo y anticomunismo en Colombia en los inicios de la guerra fría", False),
                  ("Autor", "Luis Trejos Rosero", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/folders/1z7i5z0MvfpJbRQMiY15LmqGshC3zQwDy?usp=sharing", False)]

      fields21 = [("Sesión", "5", True),
                ("Ciclo", "Tercer ciclo", True),
                ("Fecha", "3 de abril de 2021", True),
                ("Texto", "Auge y caída de Sendero Luminoso", False),
                ("Autor", "Fabiola Escárgaza", False),
                ("Carpeta de Drive", "https://drive.google.com/drive/folders/1kG5ZSjSfPj5NUxEPsJ0MzwtLpIoanXmv?usp=sharing", False)]

      fields22 = [("Sesión", "6", True),
                  ("Ciclo", "Tercer ciclo", True),
                  ("Fecha", "15 de mayo de 2021", True),
                  ("Texto", "Historia del MIR: 'Si quieren guerra, guerra tendrán...'", False),
                  ("Autor", "Cristián Pérez", False),
                  ("Carpeta de Drive", "https://drive.google.com/drive/folders/118Y_LF0QNvnFdlSRxhtEaGo83y7jaiBm?usp=sharing", False)]

      fields23 = [("Sesión", "7", True),
                  ("Ciclo", "Tercer ciclo", True),
                  ("Fecha", "29 de mayo de 2021", True),
                  ("Una mirada al paro nacional colombiano", "Discusión de la situación actual colombiana", True),
                  ("Drive", "https://drive.google.com/drive/folders/1OqF9uXHjCITLrK7hqqn9A-_9kjYzToIb?usp=sharing", False)]

      def make_embed(x):
        embed = Embed(colour=0xFF0000)
        for name, value, inline in x:
          embed.add_field(name=name, value=value, inline=inline)
        embed.set_author(name='lenin', icon_url="https://cdn.discordapp.com/attachments/716135897476628521/822171692494618624/logodegradooo.png")
        return embed

      embed1 = make_embed(fields1)
      embed2 = make_embed(fields2)
      embed3 = make_embed(fields3)
      embed4 = make_embed(fields4)
      embed5 = make_embed(fields5)
      embed6 = make_embed(fields6)
      embed7 = make_embed(fields7)
      embed8 = make_embed(fields8)
      embed9 = make_embed(fields9)
      embed10 = make_embed(fields10)
      embed11 = make_embed(fields11)
      embed12 = make_embed(fields12)
      embed13 = make_embed(fields13)
      embed14 = make_embed(fields14)
      embed15 = make_embed(fields15)
      embed16 = make_embed(fields16)
      embed17 = make_embed(fields17)
      embed18 = make_embed(fields18)
      embed19 = make_embed(fields19)
      embed20 = make_embed(fields20)
      embed21 = make_embed(fields21)
      embed22 = make_embed(fields22)
      embed23 = make_embed(fields23)


      actividades = {embed1: ["marxismo", "básico", "curso básico", "marxismo leninismo", "marxismo leninismo maoísmo", "marx", "materialismo", "introduccion", "introducción"],
      embed2: ["marxismo", "básico", "curso básico", "marxismo leninismo", "marx", "materialismo", "lenin", "introduccion", "introducción"],
      embed3: ["manifiesto comunista", "marx", "engels", "manifiesto", "burgueses", "proletarios", "marxismo", "comunismo"],
      embed4: ["chicago", "chicago boys", "documental", "chile", "dictadura", "dictadura militar", "golpe", "golpe de estado", "latinoamerica", "latinoamérica", "latam", "pinochet"],
      embed5: ["china", "maoismo", "mao", "maoísmo"],
      embed6: ["federici", "silvia federici", "feminismo"],
      embed7: ["la sociedad del cansancio", "sociedad del cansancio", "byungchul han", "byungchul", "byung-chul", "byung-chul han"],
      embed8: ["batalla de chile", "poder popular", "la batalla de chile", "chile", "documental", "latinoamerica", "latinoamérica", "latam", "dictadura"],
      embed9: ["batalla de chile", "golpe de estado", "el golpe de estado", "golpe", "dictadura", "la batalla de chile", "chile", "documental", "latinoamerica", "latinoamérica", "latam", "pinochet"],
      embed10: ["filosofía", "filosofia", "filosofia politica", "filosofía política", "stalin", "materialismo", "marxismo", "marx", "materialismo dialéctico", "materialismo histórico"],
      embed11: ["economía", "economia", "economia politica", "economía política", "harnecker", "marta harnecker"],
      embed12: ["revolución", "rusia", "revolución rusa", "revolucion", "revolucion rusa", "lenin", "stalin", "trosky", "trostky"],
      embed13: ["lenin", "leninismo", "enfermedad infantil", "izquierdismo"],
      embed14: ["anuradha", "anuradha ghandy", "ghandy", "feminismo", "feminismo liberal", "radfem", "feminismo radical", "feminismo cultural", "feminismo anar"],
      embed15: ["curso básico", "maoísmo", "maoismo", "mao", "china", "revolución", "revolucion", "revolucion china", "revolución china"],
      embed16: ["corea", "corea del sur", "corea del norte", "norcorea", "surcorea", "kim jongun", "guerra de corea", "guerra fría", "documental", "pyongyang"],
      embed17: ["mapuche", "argentina", "4 lonkos", "lonkos", "latinoamerica", "latinoamérica", "latam", "documental", "lonko"],
      embed18: ["mariategui", "mariátegui", "problema del indio", "problema de la tierra", "el problema del indio", "el problema de la tierra", "perú", "peru", "peruano", "latinoamerica", "latinoamérica", "latam"],
      embed19: ["cuba", "mujeres", "feminismo", "revolucion cubana", "revolución cubana", "mujeres en revolución", "mujeres en revolucion", "documental", "latinoamerica", "latinoamérica", "latam"],
      embed20: ["colombia", "latinoamerica", "latinoamérica", "latam", "anticomunismo", "comunismo", "guerrilla", "guerra fría"],
      embed21: ["perú", "peru", "sendero luminoso", "sendero", "latam", "latinoamérica", "latinoamerica", "guzmán"],
      embed22: ["chile", "dictadura", "mir", "latinoamérica", "latinoamerica"],
      embed23: ["colombia", "paro", "protesta", "latam", "latinoamerica", "latinoamérica", "esmad", "violencia policial"]}

      counter = 0

      for key, value in actividades.items():
        if message in value:
          await ctx.send(embed=key)
          counter += 1
        else:
          pass
      await ctx.send(f"Búsqueda finalizada, resultados encontrados: {counter}")

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("buscar")

def setup(bot):
  bot.add_cog(Buscar(bot))
