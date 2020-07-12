import discord
from discord.ext import commands
import random
import datetime
import asyncio

client = commands.Bot(command_prefix = "g!")
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Yoink Simulator v3000"))
    print("Bot is ready to play uno")

@client.command(pass_context=True)
async def uno(ctx, member1: discord.Member, member2: discord.Member, member3: discord.Member):
    uno = ["Red 0", "Green 0", "Yellow 0", "Blue 0", "Red 1", "Green 1", "Yellow 1", "Blue 1", "Red 2", "Green 2",
           "Yellow 2", "Blue 3", "Red 4", "Green 4", "Yellow 4", "Blue 4", "Red 5", "Green 5", "Yellow 5", "Blue 5",
           "Red 6", "Green 6", "Yellow 6", "Blue 6", "Red 7", "Green 7", "Yellow 7", "Blue 7", "Red 8", "Green 8",
           "Yellow 8", "Blue 8", "Red 9", "Green 9", "Yellow 9", "Blue 9", "Red +2", "Green +2", "Yellow +2", "Blue +2",
           "Red Skip", "Green Skip", "Yellow Skip", "Blue Skip", "Red Reverse", "Green Reverse", "Yellow Reverse",
           "Blue Reverse", "+4", "+4", "+4", "+4", "Wild", "Wild", "Wild"]

    author = ctx.message.author

    list = []

    num = 0;

    embed = discord.Embed()
    embed.set_author(name="Test")
    for i in range(7):
        randcard = random.choice(uno)
        embed.add_field(name="Test-Uno", value=f'{randcard}', inline=False)
        list.append(randcard)

    embed1 = discord.Embed()
    embed1.set_author(name="Test")
    for i in range(7):
        embed1.add_field(name="Test-Uno", value=f'{random.choice(uno)}', inline=False)

    embed2 = discord.Embed()
    embed2.set_author(name="Test")
    for i in range(7):
        embed2.add_field(name="Test-Uno", value=f'{random.choice(uno)}', inline=False)

    embed3 = discord.Embed()
    embed3.set_author(name="Test")
    for i in range(7):
        embed2.add_field(name="Test-Uno", value=f'{random.choice(uno)}', inline=False)




    await author.send(author, embed=embed)
    await member1.send(embed=embed1)
    await member2.send(embed=embed2)
    await member3.send(embed=embed3)

    print(list)

client.run('cant show u the token')
