import discord
import traceback
from discord.ext import commands
import random
from cogs.utility import Utility
import cogs.help
import sys
import os

my_secret = os.environ['TOKEN']

description = '''Pain and Suffering discord bot, developed with discord.py, @notfelo\n'''

felo = 211639706444627969

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
        send_felo = await self.fetch_user(211639706444627969)
        #cogs
        await bot.change_presence(status = discord.Status.dnd, activity = discord.Game(name="This game called 'Life', but not for long | *help"))
        self.add_cog(Utility(self))
        self.add_cog(cogs.help.Help(self))
        self.help_command = cogs.help.HelpCommand()

    async def on_message(self, message):
        if 'dababy' in message.clean_content.lower():
            await message.add_reaction("👶")
        await self.process_commands(message)

    async def on_error(self, event, *args, **kwargs):
        if self.me:
            traceback.print_exc()
        else:
            embed = discord.Embed(title=':x: Event Error', colour=0xe74c3c) #Red
            embed.add_field(name='Event', value=event)
            embed.description = '```py\n%s\n```' % traceback.format_exc()
            try:
                await send_felo.send(embed=embed)
            except:
                pass
    
    async def on_command_error(self, error, ctx):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.author.send('This command cannot be used in private messages.')
        elif isinstance(error, commands.DisabledCommand):
            await ctx.channel.send(':x:  This command has been deactivated')
        elif isinstance(error, commands.CommandInvokeError):
            if self.dev:
                raise error
            else:
                embed = discord.Embed(title=':x: Command Error', colour=0x992d22) #Dark Red
                embed.add_field(name='Error', value=error)
                embed.add_field(name='Guild', value=ctx.guild)
                embed.add_field(name='Channel', value=ctx.channel)
                embed.add_field(name='User', value=ctx.author)
                embed.add_field(name='Message', value=ctx.message.clean_content)
                try:
                    await send_felo.send(embed=embed)
                except:
                    pass
    

bot = Pain()
bot.run(my_secret)