import discord
import pogoda
from discord.ext import commands

from config import *

intents = discord.Intents.default()  # Подключаем разрешения
intents.message_content = True
# Задание префикса и интентов
bot = commands.Bot(command_prefix='', intents=intents)

@bot.command()
async def погода(ctx, message):
    await ctx.send(pogoda.weather_city(message))

@bot.command()
async def пинг(ctx):
    await ctx.send('понг')


bot.run(token_bot)