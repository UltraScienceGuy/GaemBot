import discord
from discord.ext import commands
import random
import datetime

#GaemBot v1.3

client = commands.Bot(command_prefix = "g!")
client.remove_command('help')

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

@client.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(

        title = "Commands (thus far)",
        description = "help commands",
        colour = discord.Colour.blue()
    )

    embed.set_footer(text = "Written by ultraman3214 #1357")
    embed.set_image(url="https://discordapp.com/channels/642513671943094291/651622911475449898/731511206065733743")
    embed.add_field(name="g!ping", value="Returns Pong!", inline=False)
    embed.add_field(name="g!8ball <query>", value="Returns a random answer for a question you ask", inline=False)
    embed.add_field(name="g!createrole <rolename>", value="Creates a role called rolename with no basic perms", inline=False)
    embed.add_field(name="Role assigning capabilities", value="Can assign reaction roles, just change the message id for which message the reactios go on in the code", inline=False)
    embed.add_field(name="g!uno <member name1> <member name2> <member name3>", value="Starts an uno game, WIP currently (do not use it).", inline=False)
    embed.add_field(name="g!kick <member name>", value="Kicks the member. Perms required", inline=False)
    embed.add_field(name="g!ban <member name>", value="Bans the member. Perms required", inline=False)
    embed.add_field(name="g!bignate", value="Shows the newest bignate comic from gocomics", inline=False)
    embed.add_field(name="g!xkcd <number>", value="Shows the comic based on the integer you enter, e.g. to see the first comic you would say 1", inline=False)
    embed.add_field(name="g!calvinhobbes ", value="Shows the latest calvin and hobbes comic", inline=False)
    embed.add_field(name="g!foxtrot", value="Shows the latest foxtrot comic", inline=False)
    embed.add_field(name="g!searchcalvinhobbes <date in yy/mm/dd>", value="Shows an archived Calvin and Hobbes comic", inline=False)
    embed.add_field(name="g!searchbignate <date in yy/mm/dd>", value="Shows an archived bignate comic", inline=False)

    await ctx.send('A list of commands has been sent to your dms')

    await author.send(embed=embed)

@client.command()
async def gayrate(ctx, member):
    await ctx.send(f'{member} is ' + str(random.randrange(100)) + "% gay")

@client.command()
async def bignate(ctx):

    today = datetime.date.today()
    await ctx.send("https://gocomics.com/bignate/" + str(today.year) + "/" + str(today.month) + "/" + str(today.day))

@client.command()
async def searchbignate(ctx, date):

    await ctx.send("https://gocomics.com/bignate/" + str(date))

@client.command()
async def calvinhobbes(ctx):

    today = datetime.date.today()
    await ctx.send("https://gocomics.com/calvinandhobbes/" + str(today.year) + "/" + str(today.month) + "/" + str(today.day))

@client.command()
async def searchcalvinhobbes(ctx, date):

    await ctx.send("https://gocomics.com/calvinandhobbes/" + str(date))

@client.command()
async def xkcd(ctx, numcomic):

    await ctx.send("https://xkcd.com/" + str(f'{numcomic}') + "/")

@client.command()
async def foxtrot(ctx):
    await ctx.send("https://gocomics.com/foxtrot/2020/07/05")

@client.command(pass_context=True)
async def uno(ctx, member1: discord.Member, member2: discord.Member, member3: discord.Member):
    uno = ["Red 0", "Green 0", "Yellow 0", "Blue 0", "Red 1", "Green 1", "Yellow 1", "Blue 1", "Red 2", "Green 2",
           "Yellow 2", "Blue 3", "Red 4", "Green 4", "Yellow 4", "Blue 4", "Red 5", "Green 5", "Yellow 5", "Blue 5",
           "Red 6", "Green 6", "Yellow 6", "Blue 6", "Red 7", "Green 7", "Yellow 7", "Blue 7", "Red 8", "Green 8",
           "Yellow 8", "Blue 8", "Red 9", "Green 9", "Yellow 9", "Blue 9", "Red +2", "Green +2", "Yellow +2", "Blue +2",
           "Red Skip", "Green Skip", "Yellow Skip", "Blue Skip", "Red Reverse", "Green Reverse", "Yellow Reverse",
           "Blue Reverse", "+4", "+4", "+4", "+4", "Wild", "Wild", "Wild"]

    author = ctx.message.author

    embed = discord.Embed()
    embed.set_author(name="Test")
    for _ in range(7):
        embed.add_field(name="Test-Uno", valuere=f'{random.choice(uno)}', inline=False)

    embed1 = discord.Embed()
    embed1.set_author(name="Test")
    for _ in range(7):
        embed1.add_field(name="Test-Uno", value=f'{random.choice(uno)}', inline=False)

    embed2 = discord.Embed()
    embed2.set_author(name="Test")
    for _ in range(7):
        embed2.add_field(name="Test-Uno", value=f'{random.choice(uno)}', inline=False)

    embed3 = discord.Embed()
    embed3.set_author(name="Test")
    for _ in range(7):
        embed3.add_field(name="Test-Uno", value=f'{random.choice(uno)}', inline=False)

    await author.send(author, embed=embed)
    await member1.send(embed=embed1)
    await member2.send(embed=embed2)
    await member3.send(embed=embed3)

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
    if message_id == 731554807474684024:
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
        elif payload.emoji.name == "vardhan":
            role = discord.utils.get(guild.roles, name="uno")

        #you're not just limited to these games, you can also add other ones
        #make sure that you have appropriate custom emojis as well as role names
        #you can create rolenames using g!createrole <rolename here>
        #(you also dont have to create just gaming roles)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done")

client.run('sorry cant put my token here cus otherwise it would keep resetting lol')
