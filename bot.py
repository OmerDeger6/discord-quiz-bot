import discord
from discord.ext import commands

TOKEN = "YOUR_BOT_TOKEN"  #Buraya kendi bot token'ini koy

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yaptım!")

@bot.command()
async def test(ctx):
    await ctx.send("Bot çalışıyor!")

bot.run(TOKEN)
