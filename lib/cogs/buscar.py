from discord.ext.commands import Cog
from discord import Embed
from discord.ext.commands import command

class Buscar(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command(name="buscar")
  async def buscar(self, ctx, *args):
    
    if args == ():
      await ctx.channel.send('Debes escribir una palabra clave para que pueda buscar')

    else:
      message = str(' '.join(args).lower())

      actividades = {"¿Qué es el Marxismo Leninismo Maoísmo?": ["marxismo", "básico", "curso básico", "marxismo leninismo", "marxismo leninismo maoísmo", ], 
      "Tres fuentes del marxismo": ["marxismo", "básico", "curso básico", "marxismo leninismo"], 
      "Documental Chicago Boys": ["chicago", "chicago boys", "documental", "chile", "dictadura", "dictadura militar", "golpe", "golpe de estado"], 
      "Desmitificando China": ["china", "maoismo"],
      "El patriarcado del salario": ["federici", "silvia federici", "feminismo"],
      "La sociedad del cansancio": ["la sociedad del cansancio", "sociedad del cansancio"], 
      "Documental La Batalla de Chile: El poder popular": ["batalla de chile", "poder popular", "la batalla de chile", "chile"],
      "Documental La Batalla de Chile: El golpe de Estado": ["batalla de chile", "golpe de estado", "el golpe de estado", "golpe", "dictadura", "la batalla de chile", "chile"],
      "Sobre el materialismo dialéctico y el materialismo histórico": ["filosofía", "filosofia", "filosofia politica", "filosofía política", "stalin", "materialismo", "marxismo"], 
      "Explotación capitalista": ["economía", "economia", "economia politica", "economía política", "harnecker", "marta harnecker"],
      "Revolución rusa": ["revolución", "rusia", "revolución rusa", "revolucion", "revolucion rusa", "lenin", "stalin", "trosky", "trostky"],
      }
      
      counter = 0

      for key, value in actividades.items():
        if message in value:
            await ctx.send(key)
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