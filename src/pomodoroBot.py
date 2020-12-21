import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import time

class Pom(discord.Client):

    def __init__(self, **options):
        super().__init__(**options)
        self.BOT_PREFIX      =   os.getenv('BOT_PREFIX')

        self.MINI_BREAKS     =   int(os.getenv('MINI_BREAKS'))                # how many mini breaks between long breaks
        self.WORK_TIME       =   int(os.getenv('WORK_TIME'))          * 60    # seconds
        self.MINI_BREAK_TIME =   int(os.getenv('MINI_BREAK_TIME'))    * 60    # seconds
        self.BREAK_TIME      =   int(os.getenv('BREAK_TIME'))         * 60    # seconds

    async def on_ready(self):
        print('Pom is ready!')

    async def on_message(self, message):
        # do not listen to the bot's own messages
        if message.author == self.user:
            return
        
        msg = message.content

        if msg == (self.BOT_PREFIX + "config"):
            await message.channel.send('MINI_BREAKS:\t{}\nWORK_TIME:\t{}min\nMINI_BREAK_TIME:\t{}min\nBREAK_TIME:\t{}min'.format(self.MINI_BREAKS, self.WORK_TIME/60, self.MINI_BREAK_TIME/60, self.BREAK_TIME/60))
        elif msg == (self.BOT_PREFIX + "default"):
            self.setdefault()

    def setdefault(self):
        self.MINI_BREAKS     =   int(os.getenv('MINI_BREAKS'))                # how many mini breaks between long breaks
        self.WORK_TIME       =   int(os.getenv('WORK_TIME'))          * 60    # seconds
        self.MINI_BREAK_TIME =   int(os.getenv('MINI_BREAK_TIME'))    * 60    # seconds
        self.BREAK_TIME      =   int(os.getenv('BREAK_TIME'))         * 60    # seconds

"""
@client.command()
async def config(ctx, *args):
    if isinstance(str(args[0]), str):
        if str(args[0]) == 'default':
            MINI_BREAKS     =   int(os.getenv('MINI_BREAKS'))                # how many mini breaks between long breaks
            WORK_TIME       =   int(os.getenv('WORK_TIME'))          * 60    # seconds
            MINI_BREAK_TIME =   int(os.getenv('MINI_BREAK_TIME'))    * 60    # seconds
            BREAK_TIME      =   int(os.getenv('BREAK_TIME'))         * 60    # seconds
            await ctx.send('set default values successfuly')
        elif str(args[0]) == 'set':
            if len(args) != 5:
                await ctx.send('wrong number of arguments given to "{}config set"'.format(BOT_PREFIX))
                return
            try:
                if isinstance(int(args[1]), int) and isinstance(int(args[2]), int) and isinstance(int(args[3]), int) and isinstance(int(args[4]), int):
                    MINI_BREAKS     =   int(args[1])            # how many mini breaks between long breaks
                    WORK_TIME       =   int(args[2])    * 60    # seconds
                    MINI_BREAK_TIME =   int(args[3])    * 60    # seconds
                    BREAK_TIME      =   int(args[4])    * 60    # seconds
                    await ctx.send('set given values successfuly')
            except(ValueError):
                await ctx.send('arguments could not be set, are all arguments integers?')
        elif str(args[0]) == 'print':
            await ctx.send('MINI_BREAKS:{} \n WORK_TIME:{} \n MINI_BREAK_TIME:{} \n BREAK_TIME:{} \n'.format(MINI_BREAKS, WORK_TIME, MINI_BREAK_TIME, BREAK_TIME))
        else:
            await ctx.send('could not find command ">config {}"'.format(args[0]))


@client.command()
async def put(ctx):
    await ctx.send(MINI_BREAK_TIME)
"""

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

pom = Pom()
pom.run(DISCORD_TOKEN)