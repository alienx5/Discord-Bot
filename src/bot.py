import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

activity = discord.Activity(name = '/help', type = discord.ActivityType.playing)

bot = commands.Bot(command_prefix = '/', intents = intents, activity = activity)

@bot.event
async def on_ready():
    await load_extensions()
    print(f'{bot.user} has connected to the server')

async def load_extensions():
    for filename in os.listdir('./command'):
        if filename.endswith('.py') and filename != '__init__.py':
            try:
                await bot.load_extension(f'command.{filename[:-3]}')
                print(f'Loaded extension {filename}')
            except Exception as e:
                print(f'Failed to load extension {filename} {e}')

bot.run(TOKEN)