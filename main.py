import discord
from discord.ext import commands
from cogs.utility import Utility
import cogs.help
import os
from dotenv import load_dotenv

load_dotenv()

my_secret = os.getenv('TOKEN')

description = '''Pain and Suffering discord bot, developed with discord.py, @notfelo\n'''


class Pain(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='*', description=description)

    async def on_ready(self):
        if self.user.id == 772683777503789066:
            self.me = True
        else:
            self.me = False
        '''logger.info('Logged in.')
        logger.info(f'Bot-Name: {self.user.name} | ID: {self.user.id}')
        logger.info(f'Dev Mode: {self.me}, Felo: {felo}')
        logger.info('------')'''
        print('WE ARE IN')
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
        await self.process_commands(message)

    async def on_command_error(self, error, ctx):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.author.send(
                'This command cannot be used in private messages.')
        elif isinstance(error, commands.DisabledCommand):
            await ctx.channel.send(':x:  This command has been deactivated')


bot = Pain()
bot.run(my_secret)
