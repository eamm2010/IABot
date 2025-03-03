import discord
from discord.ext import commands
from model import predict_image, class_names

TOKEN = "0MTI4NTI1NDI5ODkyNTY2NjM0NA.G8wB5i.YMcwkMvMC36OT5E4-w7G_XR2BSDCjhf2sO_gEw"
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            file_name = archivo.filename
            file_url = archivo.url
            await archivo.save(f"images/{file_name}")
            await ctx.send(predict_image(image = f"images/{file_name}"))
    else:
        await ctx.send("No se ha adjuntado ningún archivo")

bot.run(TOKEN)