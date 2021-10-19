import discord
import time
import birb_token as token
from discord import embeds
from discord.ext import commands
from discord.flags import alias_flag_value
from cogs import bsc_cmd

client = commands.Bot(command_prefix='\'')
c = '```'
#erase default !help command
client.remove_command('help')

#load bsc_cmd cog
client.load_extension('cogs.bsc_cmd')
wait = time.sleep(.5)


#on_Ready
@client.event
async def on_ready():
    wait
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game('Professor Birb | Get \'help'))
    print('BOT IS READY!')


#HELP COMMAND: Configurations
@client.command(aliases=['HELP', 'Help'])
async def help(ctx):
    embed_help = discord.Embed(title="Professor Birb Commands",
                               description="All things that I can do, Chirp!",
                               color=0x00ffbf)
    embed_help.add_field(name="'help",
                         value="All list of commands",
                         inline=True)
    embed_help.add_field(name="'calc",
                         value="Calculates given equation.",
                         inline=True)
    embed_help.add_field(name="'sqrt",
                         value="Square root of a number",
                         inline=True)
    embed_help.add_field(name="'sq",
                         value="Get the square of a number",
                         inline=True)
    embed_help.set_footer(icon_url=ctx.author.avatar_url,
                          text="Written using python language")
    wait
    await ctx.send(embed=embed_help)


client.run(token.TOKEN)