from discord.ext import commands
import os
import traceback
import discord
import logging

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def neko(ctx):
    await ctx.send('にゃあ')
    
@bot.command()
async def tundere(ctx):
    await ctx.send('べっ、別に兄さんのことなんか好きじゃないんだからねっ!!!')

bot.run(token)
