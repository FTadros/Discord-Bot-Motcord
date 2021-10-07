import discord
from discord.ext import commands
from cogs.utility import Utility
import cogs.help
import os
from dotenv import load_dotenv

load_dotenv()

my_secret = os.getenv('TOKEN')

description = '''Pain and Suffering discord bot, developed with discord.py, @notfelo\n'''

felo = 211639706444627969

class Pain(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='*', description=description)

    async def on_ready(self):
        self.me = False
        if self.user.id == 772683777503789066:
            self.me = True

        print('WE ARE IN THE MAINFRAME')
        #cogs
        await bot.change_presence(
            status=discord.Status.dnd,
            activity=discord.Game(
                name="This game called 'Life', but not for long | *help"))
        self.add_cog(Utility(self))
        self.add_cog(cogs.help.Help(self))
        self.help_command = cogs.help.HelpCommand()

    async def on_message(self, message):
        if 'dababy' in message.clean_content.lower():
            await message.add_reaction("👶")
        
        if (message.author.id == felo or message.author.id == 177870770758746113) and ('rychee' in message.clean_content.lower()):
            await message.add_reaction("<:RD:860414084305125406>")

        if 'shpd' in message.clean_content.lower():
            idsuo = ["🇮", "🇩", "🇸", "🇺", "🇴"]
            for i in idsuo:
                await message.add_reaction(i) 
        await self.process_commands(message)

    async def on_command_error(self, error, ctx):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.author.send(
                'This command cannot be used in private messages.')
        elif isinstance(error, commands.DisabledCommand):
            await ctx.channel.send(':x:  This command has been deactivated')


bot = Pain()
bot.run(my_secret)
