import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print('Hello there, my name is PomodoroBot. You can call me Pom though! Let\'s start being productive shall we!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    
    if msg.startswith('$pom'):
        await message.channel.send('Hello from Pom!')

client.run(DISCORD_TOKEN)