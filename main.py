import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
my_secret = os.getenv('TOKEN')

description = '''Pain and Suffering discord bot, developed with discord.py, @notfelo\n'''

felo = 211639706444627969


class Pain(commands.Bot):
    def __init__(self):
        self._cogs = [p.stem for p in Path(".").glob("./bot/cogs/*.py")]
        super().__init__(command_prefix='*', description=description)

    def setup(self):
        print("Setting up shop...")

        for cog in self._cogs:
            self.load_extension(bot.cogs.cog)
            print("Loaded" + cog +'cog')

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
        await bot.change_presence(
            status=discord.Status.dnd,
            activity=discord.Game(
                name="This game called 'Life', but not for long | *help"))
        self.add_cog(Utility(self))
        self.add_cog(cogs.help.Help(self))
        self.help_command = cogs.help.HelpCommand()

    async def on_message(self, msg):
        if not msg.author.bot:
            if 'dababy' in msg.clean_content.lower():
                await msg.add_reaction("👶")

            if (msg.author.id == felo or msg.author.id == 177870770758746113) and ('rychee' in message.clean_content.lower()):
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


bot = Pain()
bot.run(my_secret)
