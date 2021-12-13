import os
import discord
from discord.colour import Color
from discord.ext import commands, tasks
from discord.ext.commands import bot
from randoms import random_value


client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    game = discord.Game("LOOP FOR MG BOT")
    await client.change_presence(status = discord.Status.online, activity = game)

@tasks.loop(seconds=240)
async def refresh():
    from refresh import refresh
    refresh()

# @tasks.loop(seconds=5)
# async def restock():
#     from restock import restock
#     restock()


@client.command(name='start')
async def start(ctx, *text):
    if len(text) == 2:
        order = text[0]
        pw = text [1]

        if str(pw) == "6213" and order == 'refresh':
            refresh.start()
            print("start process - refresh")
            embed = discord.Embed(title = "Sussess Start",
            description = "Start Loop - `ReFresh`" , color = discord.Color.dark_gold()
            )

            await ctx.send(embed=embed)

        # elif str(pw) == "6213" and order == 'restock':
        #     restock.start()
        #     print("start process - restock")
        #     embed = discord.Embed(title = "Sussess Start",
        #     description = "Start Loop - `ReStcok`" , color = discord.Color.dark_gold()
        #     )

        #     await ctx.send(embed=embed)

        else:
            embed = discord.Embed(title = "Wrong PassWord",
            description = "Start Loop" , color = discord.Color.dark_red()
            )

            await ctx.send(embed=embed)

    elif len(text) == 1:
        await ctx.send('Input Password!')

@client.command(name='stop')
async def stop(ctx, *text):
    if len(text) == 2:
        order = text[0]
        pw = text [1]

        if str(pw) == "6213" and order == 'refresh':
            refresh.stop()
            print("stop process - refresh")
            embed = discord.Embed(title = "Sussess Stop",
            description = "Stop Loop - `ReFresh`" , color = discord.Color.dark_gold()
            )

            await ctx.send(embed=embed)

        # elif str(pw) == "6213" and order == 'restock':
        #     restock.stop()
        #     print("stop process - restcok")
        #     embed = discord.Embed(title = "Sussess Stop",
        #     description = "Stop Loop - `ReStcok`" , color = discord.Color.dark_gold()
        #     )

        #     await ctx.send(embed=embed)

        else:
            embed = discord.Embed(title = "Wrong PassWord",
            description = "Stop Loop" , color = discord.Color.dark_red()
            )

            await ctx.send(embed=embed)
            
    elif len(text) == 1:
        await ctx.send('Input Password!')

client.run(os.environ['token'])