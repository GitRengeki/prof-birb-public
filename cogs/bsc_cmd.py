import discord
import math
import time
from discord.ext import commands

wait = time.sleep(.25)
c = '```'


class bsc_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

#CALC COMMAND: Configurations

    @commands.command(aliases=['CALC', 'Calc'])
    async def calc(self, ctx, *, args):
        try:
            get_user = ctx.message.author
            result = eval(args)
            await ctx.send(f'{c}{get_user}\nThe answer is {result:,.2f}{c}')
            return
        except:
            await ctx.send(f'{c}OOPS! Encountered an error （＞人＜；){c}')
            return

#SQRT COMMAND: Configurations

    @commands.command(aliases=['SQRT', 'Sqrt'])
    async def sqrt(self, ctx, args):
        try:
            get_user = ctx.message.author
            wait
            result = math.sqrt(float(args))
            await ctx.send(f'{c}{get_user}\nThe answer is {result:,.2f}{c}')
            return
        except:
            await ctx.send(f'{c}OOPS! Encountered an error （＞人＜；){c}')
            return


#SQ COMMAND: Configurations

    @commands.command(aliases=['SQ', 'Sq'])
    async def sq(self, ctx, args):
        try:
            get_user = ctx.message.author
            wait
            result = float(args) * float(args)
            await ctx.send(f'{c}{get_user}\nThe answer is {result:,.2f}{c}')
            return
        except:
            await ctx.send(f'{c}OOPS! Encountered an error （＞人＜；){c}')
            return


def setup(client):
    client.add_cog(bsc_cmd(client))
