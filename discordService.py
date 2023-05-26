import discord
from discord.ext import commands
 

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
   
@bot.command(name='ping')
async def ping(self, ctx:commands.Context):
    await ctx.send('Pong!')

bot.run('MTExMTY5MTAyMTQyODk5MDA3NA.Gte2i4.YueOSwWpSBAHsBJDwWgsjBdzIgzoya1R1ZJoY8')
