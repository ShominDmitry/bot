import os
import random
import discord
from discord.ext import commands

# from config import settings
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='', intents=intents)


@bot.event
async def on_ready():
    print('Я вошёл в систему как {0.user}'.format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    code_for_save = "Save_me"
    if code_for_save in message.content:
        message_content = message.content.replace(code_for_save, "")
        with open("saved.txt", "a") as f:
            f.write((message.content + "\n"))

    await bot.process_commands(message)


@bot.command()
async def хай(ctx):
    embed = discord.Embed(color=0000, title='Хай', description="Привет")
    await ctx.send(embed=embed)


@bot.command()
async def BENG(ctx):
    embed = discord.Embed(color=0000, title='BENG', description="BENGERFOP#1415")
    await ctx.send(embed=embed)


@bot.command()
async def привет(ctx):
    embed = discord.Embed(color=0000, title='привет', description="ну привет")
    await ctx.send(embed=embed)


@bot.command()
async def ОТДАЙ_КАРТИНКУ(ctx):
    img_list = os.listdir(r'pictures')
    img_path = 'pictures/' + random.choice(img_list)
    await ctx.send(file=discord.File(img_path))


@bot.command()
async def команды(ctx):
    embed = discord.Embed(color=0000, title='команды', description="вот список"
                                                                   "\n 🐱‍💻ОТДАЙ_КАРТИНКУ = рандом картинка"
                                                                   "\n ✨BENG = мой ак"
                                                                   "\n 🙌привет = ну привет"
                                                                   "\n ✔хай = привет"
                          )

    await ctx.send(embed=embed)


bot.run('MTA5MzQzMTE1NzkyNTg4Mzk0NA.GUYbGr.eUIRr8qRl5VRbGHcOFpauvuuCA-TjbejCfirhk')
