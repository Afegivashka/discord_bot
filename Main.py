import time

import discord
import pogoda, Questions_my_game
from discord.ext import commands

from config import *

intents = discord.Intents.default()  # Подключаем разрешения
intents.message_content = True
# Задание префикса и интентов
bot = commands.Bot(command_prefix='!', intents=intents)


class Buttons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)

    @discord.ui.button(label="Запись на игру", style=discord.ButtonStyle.green)
    async def game_green_button(self, interaction: discord.Interaction, button: discord.ui.Button):

        user_id = interaction.user.id
        print(time.thread_time(), "Получен айди юзера...")

        if user_id in Questions_my_game.list_player:
            await interaction.message.reply("Вы уже записались")
        else:
            Questions_my_game.list_player.append(user_id)
            print(time.thread_time(), "Айди юзера добавлен в список игроков...")
            user_name = await bot.fetch_user(user_id) #тут очень долго выполняется операция поиска по айди, нужно исправить.
            user_name = user_name.name
            print(time.thread_time(), "Найдено и сохранено имя игрока")
            print(Questions_my_game.list_player)
            await interaction.message.reply(f"{user_name} записался на игру!")


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def clear_all_message(ctx, amount: int):
    count_message = await ctx.channel.purge(limit=amount)
    await ctx.channel.send(f'Deleted {len(count_message)} message(s)')


@bot.command()
async def запись(ctx):
    if ctx.channel.id == id_channel_game_question:
        print(time.thread_time(), " Проверка канала...")
        Questions_my_game.list_player.clear()
        print(time.thread_time(), "Очистка списка игроков успешна...")
        Questions_my_game.spisok_slov.clear()
        print(time.thread_time(), "Очистка списка вопросов успешна...")
        await ctx.channel.send("Игра начинается, у вас 60 секунд чтобы записаться", view=Buttons())
        print(time.thread_time(), "Сообщение с кнопкой отправлено...")
        time_start_game = 60
        while time_start_game != 0:
            time.sleep(15)
            time_start_game -= 15
            await ctx.channel.send(f"Осталось {time_start_game} секунд")
    else:
        await ctx.channel.send(f'{ctx.author} вы не в игровом канале!')


@bot.command()
async def добавить(ctx):
    if ctx.channel.id == id_channel_game_question: #and ctx.author.id in Questions_my_game.list_player:
        Questions_my_game.add_lst(ctx.author.id, ctx.message.content)
        print(Questions_my_game.spisok_slov)
        await ctx.message.delete()
    else:
        await ctx.send('Неккоректный канал или вы не записались на игру!')


@bot.command()
async def вопрос(ctx):
    if ctx.channel.id == id_channel_game_question: #and ctx.author.id in Questions_my_game.list_player:
        pass
    else:
        await ctx.send('Вы уже ответили на вопрос или не участвуете в игре.')


@bot.command()
async def погода(ctx, message):
    await ctx.send(pogoda.weather_city(message))


@bot.command()
async def пинг(ctx):
    await ctx.send("понг")


bot.run(token_bot)