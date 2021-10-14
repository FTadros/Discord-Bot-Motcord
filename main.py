import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from pathlib import Path
from cogs.utility import Utility

load_dotenv()
my_secret = os.getenv('TOKEN')

description = '''Pain and Suffering discord bot, developed with discord.py, @notfelo\n'''

felo = 211639706444627969


class Pain(commands.Bot):
    def __init__(self):
        self._cogs = [Utility]
        super().__init__(command_prefix='*', description=description)

    def setup(self):
        print("Setting up shop...")
        print(self._cogs)

        for cog in self._cogs:
            self.add_cog(cog(self))
            print("Loaded" , cog, 'cog')
        print("Setup Compelte")

    def run(self):
        self.setup()
        print("Bot is now running...")
        super().run(my_secret, reconnect=True)

    async def on_ready(self):
        self.me = False
        if self.user.id == 772683777503789066:
            self.me = True

        print('WE ARE IN THE MAINFRAME')
        # cogs
        await self.change_presence(
            status=discord.Status.dnd,
            activity=discord.Game(
                name="This game called 'Life', but not for long | *help"))

    async def on_message(self, msg):
        if not msg.author.bot:
            if 'dababy' in msg.clean_content.lower():
                await msg.add_reaction("👶")

            if (msg.author.id == felo or msg.author.id == 177870770758746113) and ('rychee' in msg.clean_content.lower()):
                await msg.add_reaction("<:RD:860414084305125406>")

            if 'shpd' in msg.clean_content.lower():
                idsuo = ["🇮", "🇩", "🇸", "🇺", "🇴"]
                for i in idsuo:
                    await msg.add_reaction(i)
            await self.process_commands(msg)

    async def on_command_error(self, error, ctx):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.author.send(
                'This command cannot be used in private messages.')
        elif isinstance(error, commands.DisabledCommand):
            await ctx.channel.send(':x:  This command has been deactivated')
