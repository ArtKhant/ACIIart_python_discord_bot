import discord
import requests
import io
from discord.ext import commands
from discord import app_commands
from PIL import Image
from io import BytesIO

import ASCII_photo_comverter as ASCII
import ACII_text as ASCII_txt
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), )


@bot.event
async def on_ready():
    print("bot is on line")
    try:
        synced = await bot.tree.sync()
        print(f"bot was synced {len(synced)} commmands")
    except Exception as e:
        print(e)


@bot.tree.command(name="help")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message("If you have problems with bot, just message me. \nAnd yes bot can have problems with high contrast annd resolution photos")


@bot.tree.command(name="info")
async def info(interaction: discord.Interaction):
    await interaction.response.send_message("This bot converts photo into ASCII graphics")


@bot.tree.command(name="plans")
async def splans(interaction: discord.Interaction):
    await interaction.response.send_message(" :construction: Future plans :construction:\n GiF convertation:arrows_clockwise:\nunusual simbouls: 𓁼 𓁽 𓁾 𓁿 𓂀 \nmake ai version\nadd unusual image format support ")



@bot.tree.command(name="convert", description="colour convert")
@app_commands.describe(lib="1 - circles, 2 - binar cod, 3 - pixels, 4 - ASCII preset or just write some simbolus (unstable)",
                       size="simboul size", file="picture")
async def convert(interaction: discord.Interaction, lib: str, size: int, file: discord.Attachment):
    try:
        url = file.url
        data = requests.get(url)
        file_content = Image.open(BytesIO(data.content))
        if file_content is None:
            print("No image")
        try:
            if size > 100:
                size = 100
            elif size <= 1:
                size = 2

            if len(lib) > 18:
                await interaction.response.send_message("too much simbouls")

            if lib == '1':
                print('1')
            elif lib == '2':
                print('2')
            elif lib == '3':
                print('3')
            elif lib == '4':
                print('4')
            else:
                lib = lib * (18 // len(lib))
                print(lib)

            size = int(size)
            lib = str(lib)

            width, height = file_content.size

            width2 = 750
            height2 = width2 * height // width

            file_content = file_content.resize((width2, height2))
            file_content = file_content.convert('RGB')

            output_buffer = BytesIO()

            file_content.save(output_buffer, 'JPEG')

            output_buffer.seek(0)
            file_content = output_buffer.getvalue()

            try:
                data = ASCII.run(lib, size, file_content)

                try:
                    if data is None:
                        print("No image")
                    else:
                        print("image ok")
                    await interaction.response.send_message(file=discord.File(io.BytesIO(data), filename='image.jpg'))


                except:
                    print("message send error:  ")
                    await interaction.response.send_message("WRONG FILE FORMAT \n please use jpg, png, e.t.c \n dont use unusual format\n i try fix it as soon as possible")


            except:
                print("conv error:  ")
                await interaction.response.send_message("sometrhing went wrong... try to change some inputs")


        except:
            print("file formatation error")
            await interaction.response.send_message("wrong file format!")

    except:
        print("bot error:  ")
        await interaction.response.send_message("sometrhing went wrong... ")


@bot.tree.command(name="wb_convert", description="WiteBlack- convert (experimental)")
@app_commands.describe(lib="1 - circles, 2 - binar cod, 3 - pixels, 4 - ASCII preset or just write some simbolus (unstable)",
                       size="simboul size", file="picture")
async def wb_convert(interaction: discord.Interaction, lib: str, size: int, file: discord.Attachment):
    try:
        url = file.url
        data = requests.get(url)
        file_content = Image.open(BytesIO(data.content))
        if file_content is None:
            print("No image")
        try:
            if size > 100:
                size = 100
            elif size <= 1:
                size = 2

            if len(lib) > 18:
                await interaction.response.send_message("too much simbouls")

            if lib == '1':
                print('1')
            elif lib == '2':
                print('2')
            elif lib == '3':
                print('3')
            elif lib == '4':
                print('4')
            else:
                lib = lib * (18 // len(lib))
                print(lib)

            size = int(size)
            lib = str(lib)

            width, height = file_content.size

            width2 = 750
            height2 = width2 * height // width

            file_content = file_content.resize((width2, height2))
            file_content = file_content.convert('RGB')

            output_buffer = BytesIO()

            file_content.save(output_buffer, 'JPEG')

            output_buffer.seek(0)
            file_content = output_buffer.getvalue()

            try:
                data = ASCII.run_WB(lib, size, file_content)

                try:
                    if data is None:
                        print("No image")
                    else:
                        print("image ok")
                    await interaction.response.send_message(file=discord.File(io.BytesIO(data), filename='image.jpg'))


                except:
                    print("message send error:  ")
                    await interaction.response.send_message("WRONG FILE FORMAT \n please use jpg, png, e.t.c \n dont use unusual format\n i try fix it as soon as possible")


            except:
                print("conv error:  ")
                await interaction.response.send_message("sometrhing went wrong... try to change some inputs")


        except:
            print("file formatation error")
            await interaction.response.send_message("wrong file format!")

    except:
        print("bot error:  ")
        await interaction.response.send_message("sometrhing went wrong... ")


@bot.tree.command(name="experimental_convert", description="experimental function, problems possible")
@app_commands.describe(lib="1 - circles, 2 - binar cod, 3 - pixels, 4 - ASCII preset or just write some simbolus (unstable)",
                       size="simboul size",color="color_lvl (bigger -> better (but all that is bigger than 32 will be render as 32, low walues can cause strange results                                                                                                                ))" ,file="picture")
async def experimental_convert(interaction: discord.Interaction, lib: str, size: int, color: int, file: discord.Attachment):
    try:
        url = file.url
        data = requests.get(url)
        file_content = Image.open(BytesIO(data.content))
        if file_content is None:
            print("No image")
        try:
            if size > 100:
                size = 100
            elif size <= 1:
                size = 2

            if color >= 32:
                color = 32
            elif color <= 1:
                color = 3

            if len(lib) > 18:
                await interaction.response.send_message("too much simbouls")

            if lib == '1':
                print('1')
            elif lib == '2':
                print('2')
            elif lib == '3':
                print('3')
            elif lib == '4':
                print('4')
            else:
                lib = lib * (18 // len(lib))
                print(lib)

            size = int(size)
            lib = str(lib)

            width, height = file_content.size

            width2 = 750
            height2 = width2 * height // width

            file_content = file_content.resize((width2, height2))
            file_content = file_content.convert('RGB')

            output_buffer = BytesIO()

            file_content.save(output_buffer, 'JPEG')

            output_buffer.seek(0)
            file_content = output_buffer.getvalue()

            try:
                data = ASCII.exp_run(lib, size, color, file_content)

                try:
                    if data is None:
                        print("No image")
                    else:
                        print("image ok")
                    await interaction.response.send_message(file=discord.File(io.BytesIO(data), filename='image.jpg'))


                except:
                    print("message send error:  ")
                    await interaction.response.send_message("WRONG FILE FORMAT \n please use jpg, png, e.t.c \n dont use unusual format\n i try fix it as soon as possible")


            except:
                print("conv error:  ")
                await interaction.response.send_message("sometrhing went wrong... try to change some inputs")


        except:
            print("file formatation error")
            await interaction.response.send_message("wrong file format!")

    except:
        print("bot error:  ")
        await interaction.response.send_message("sometrhing went wrong... ")


@bot.tree.command(name="convert_to_text", description="convert to text")
@app_commands.describe(size= "size (240 for ultra whide, 180 for normal)", file="picture") 
async def convert_to_text(interaction: discord.Interaction,size: int, file: discord.Attachment):
    try:
        if size<20:
            size =20
        if size>240:
            size = 240

        url = file.url
        data = requests.get(url)
        file_content = Image.open(BytesIO(data.content))
        if file_content is None:
            print("No image")
        try:

            width, height = file_content.size

            width2 = 750
            height2 = width2 * height // width

            file_content = file_content.resize((width2, height2))
            file_content = file_content.convert('RGB')

            output_buffer = BytesIO()

            file_content.save(output_buffer, 'JPEG')

            output_buffer.seek(0)
            file_content = output_buffer.getvalue()

            try:
                data = ASCII_txt.run(size, file_content)

                try:
                    if data is None:
                        print("No image")
                    else:
                        print("image ok")
                    await interaction.response.send_message(file = discord.File(io.BytesIO(data.encode()), filename='data.txt'))


                except:
                    print("message send error:  ")
                    await interaction.response.send_message("WRONG FILE FORMAT \n please use jpg, png, e.t.c \n dont use unusual format\n i try fix it as soon as possible")


            except:
                print("conv error:  ")
                await interaction.response.send_message("sometrhing went wrong... try to change some inputs")


        except:
            print("file formatation error")
            await interaction.response.send_message("wrong file format!")

    except:
        print("bot error:  ")
        await interaction.response.send_message("sometrhing went wrong... ")

 

bot.run("") #токен