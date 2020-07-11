import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = "g!")

@client.event
async def on_ready():
    print("Bot is ready. ")

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!')


@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason=reason)

@client.command()
async def createrole(ctx, *, role:str, fields=None):
    await ctx.guild.create_role(name = role, reason=None)

@client.command(aliases = ["8ball"])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes – definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 731321289234710528:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == "minecraft":
            role = discord.utils.get(guild.roles, name="minecraft")
        elif payload.emoji.name == "gtav":
            role = discord.utils.get(guild.roles, name="gtav")
        elif payload.emoji.name == "cod":
            role = discord.utils.get(guild.roles, name="cod")
        elif payload.emoji.name == "LoL":
            role = discord.utils.get(guild.roles, name="LoL")
        elif payload.emoji.name == "csgo":
            role = discord.utils.get(guild.roles, name="csgo")

        #you're not just limited to these games, you can also add other ones
        #make sure that you have appropriate custom emojis as well as role names
        #you can create rolenames using g!createrole <rolename here>



        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done")


@client.event
async def on_raw_reaction_remove(payload):
    pass

client.run('NzMxMjY3NjY2NDc5OTM5NjU0.Xwkx9g.k0RyelhattMrWwDkXa7Cr4cbc7w')
