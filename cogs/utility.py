import discord
import traceback
from discord.ext import commands
import random
import sys

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        print('Error in {0.command.qualified_name}: {1}'.format(ctx, error))

    @commands.command(name = 'wiki', help = 'returns wiki link of argument')
    async def wiki(self, ctx, *arg):
        arg = '_'.join(arg)
        response = ('https://en.wikipedia.org/wiki/' + arg) 
        await ctx.send(response)
    
    @commands.command(name = 'roll', help = 'ask me a question')
    async def roll(self, ctx, *arg):
        roll_quotes = [
        "Yes", "No" "Dont be stupid, stupid", "Why not",
        "Sounds ok, I guess",
        "Are u dumb or are u stupid?", "No?",
        "Lol? Nice joke?",
        "You do not look handsome! Loser!",
        "You must have inherited your mother’s genes! Loser!",
        "It must be lonely at the bottom, huh?", "LOSER!",
        "You are very ugly! Loser!", "Stop talking, idiot",
        "My theory was correct.",
        "Born a loser, dying one.",
        "Would a retard know theyre retarded? If not, now u know.",
        "The worst type of pain is when you’re smiling just to stop the tears from falling", ":sad:"
        ] 
        response = (random.choice(roll_quotes))
        await ctx.send(response)
    
    @commands.command(name = 'shutdown', help = 'disconnects', aliases=['quit'], hidden=True)
    @commands.has_permissions(administrator=True)
    async def shutdown(self, ctx):
        await ctx.send('Deuces, Logging out of Pain and Suffering')
        await self.bot.logout()  

    @commands.command(name = 'hello', help = 'says hi to user', aliases=['hi', 'wsp', 'hey'])
    async def hi(self, ctx):
        hi_quotes = [
            'hi', 'no', 'xd?', 'SUP SUP'
        ]
        response =  (random.choice(hi_quotes))
        await ctx.send(response)