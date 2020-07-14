import discord
from discord.ext import commands
import random
import datetime
import asyncio
import nltk
from nltk.stem import WordNetLemmatizer
import yfinance as yf
import datetime



lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from keras.models import load_model

model = load_model('chatbot_model.h5')
import json
import random

intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return (np.array(bag))


def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for tg in list_of_intents:
        if (tg['tag'] == tag):
            responses = random.choice(tg['responses'])
            break
    return responses


def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res

#GaemBot v1.3

client = commands.Bot(command_prefix = "g!")
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Yoink Simulator v3000"))
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
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
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

    embed.set_footer(text = "Written by ultraman3214 #1357 and HelloItsAStupidName #4234")
    embed.set_image(url="https://discordapp.com/channels/642513671943094291/651622911475449898/731511206065733743")
    embed.add_field(name="g!ping", value="Returns Pong!", inline=False)
    embed.add_field(name="g!8ball <query>", value="Returns a random answer for a question you ask", inline=False)
    embed.add_field(name="g!stock <stock abbreviation>", value="Tells you the current stock price, as well as the change from yesterday's close", inline=False)
    embed.add_field(name="g!createrole <rolename>", value="Creates a role called rolename with no basic perms", inline=False)
    embed.add_field(name="Role assigning capabilities", value="Can assign reaction roles, just change the message id for which message the reactios go on in the code", inline=True)
    embed.add_field(name="g!kick <member name>", value="Kicks the member. Perms required", inline=False)
    embed.add_field(name="g!ban <member name>", value="Bans the member. Perms required", inline=False)
    embed.add_field(name="g!quickpoll <poll question> <first response> <second response> ... <fifth response>", value="creates a poll in the poll channel, assigns reactions", inline=False)
    embed.add_field(name="g!bignate", value="Shows the newest bignate comic from gocomics", inline=False)
    embed.add_field(name="g!xkcd <number>", value="Shows the comic based on the integer you enter, e.g. to see the first comic you would say 1", inline=False)
    embed.add_field(name="g!calvinhobbes ", value="Shows the latest calvin and hobbes comic", inline=False)
    embed.add_field(name="g!foxtrot", value="Shows the latest foxtrot comic", inline=False)
    embed.add_field(name="g!searchcalvinhobbes <date in yy/mm/dd>", value="Shows an archived Calvin and Hobbes comic", inline=False)
    embed.add_field(name="g!searchbignate <date in yy/mm/dd>", value="Shows an archived bignate comic", inline=False)
    embed.add_field(name="g!chat <prompt>", value="uses machine learning to respond to what you say", inline=False)
    embed.add_field(name="g!funnyvid", value="Brings up a funny vid. If you have a recommendation for a funny vid to add, pls contact ultraman3214#1357", inline=True)
    embed.add_field(name="g!searchurban <word>", value="Searches urban dictionary for a word that you tell the bot", inline=False)

    await ctx.send(embed=embed)


@client.command()
async def funnyvid(ctx):
    funnyvids = ['https://www.youtube.com/watch?v=2nMfuqAIyjA&list=PLJN-Y5f_oTajpnpOwMSPGQRGBrkNd_d9v&index=2&t=0s',
                 'https://www.youtube.com/watch?v=6rEkKWXCcR4&list=PLJN-Y5f_oTajpnpOwMSPGQRGBrkNd_d9v&index=2',
                 'https://www.youtube.com/watch?v=IOh-7NaA28A&list=PLJN-Y5f_oTajpnpOwMSPGQRGBrkNd_d9v&index=3',
                 'https://www.youtube.com/watch?v=viLyfEtLn-M&list=PLJN-Y5f_oTajpnpOwMSPGQRGBrkNd_d9v&index=4',
                 'https://www.youtube.com/watch?v=AuZJlroSSHY&list=PLJN-Y5f_oTajpnpOwMSPGQRGBrkNd_d9v&index=5',
                 'https://www.youtube.com/watch?v=fMezlGSrwkQ&list=PLJN-Y5f_oTajpnpOwMSPGQRGBrkNd_d9v&index=6',
                 'https://www.youtube.com/watch?v=R0UHzjj_Ydo&list=PLJN-Y5f_oTajpnpOwMSPGQRGBrkNd_d9v&index=7',
                 'https://www.youtube.com/watch?v=WApuXPDR5Q0&list=PL30BFB50685A0252B',
                 'https://www.youtube.com/watch?v=-5Ilq3kFxek&list=PL30BFB50685A0252B&index=5',
                 'https://www.youtube.com/watch?v=blpe_sGnnP4&list=PL30BFB50685A0252B&index=4',
                 'https://www.youtube.com/watch?v=aRsWk4JZa5k', 'https://www.youtube.com/watch?v=AndzyIDU-kQ',
                 'https://www.youtube.com/watch?v=iIgEWRb61IQ', 'https://www.youtube.com/watch?v=Dfhh0slknlo',
                 'https://www.youtube.com/watch?v=--NFjjcQ8Ug', 'https://www.youtube.com/watch?v=AXrHbrMrun0',
                 'https://www.youtube.com/watch?v=eEa3vDXatXg', 'https://www.youtube.com/watch?v=-yr-Akpte4w', 'https://www.youtube.com/watch?v=xpqlBYHNUgk', 'https://www.youtube.com/watch?v=Hk3T1FSlkYw', 'https://www.youtube.com/watch?v=xQaySnBRyp0', 'https://www.youtube.com/watch?v=dP9kNruuWGI', 'https://www.youtube.com/watch?v=AqsdmomR4p0', 'https://www.youtube.com/watch?v=a8uyilHatBA', 'https://www.youtube.com/watch?v=WiK6SRvI3XU']
    await ctx.send(f'{random.choice(funnyvids)}')

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
    await ctx.send("https://www.gocomics.com/foxtrot/2020/07/12")

@client.command()
async def chat(ctx, *, question):
    msg = question

    if msg != '':
        await ctx.send(f'You: {question}')
        res = chatbot_response(msg)
        await ctx.send(f'Bot: {res}')

@client.command(pass_context=True)
async def quickpoll(ctx, question, *options: str):
    channel = client.get_channel(692069601579892757)

    if len(options) <= 1:
        await client.say('You need more than one option to make a poll!')
        return
    if len(options) > 5:
        await client.say('You cannot make a poll for more than 5 things!')
        return

    if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
        reactions = ['✅', '❌']
    elif len(options) == 3:
        reactions = ['1️⃣','2️⃣','3️⃣']
    elif len(options) == 4:
        reactions = ['1️⃣','2️⃣','3️⃣','5️⃣']
    else:
        reactions = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣']

    description = []
    for x, option in enumerate(options):
        description += '\n {} {}'.format(reactions[x], option)
    embed = discord.Embed(title=question, description=''.join(description))
    react_message = await channel.send(embed=embed)
    for reaction in reactions[:len(options)]:
        await message.add_reaction(react_message, reaction)
    embed.set_footer(text='Poll ID: {}'.format(react_message.id))
    await client.edit_message(react_message, embed=embed)

@client.command()
async def activity(ctx, user):
    ctx.guild.get_member(user)
    now = datetime.datetime.now()
    print(now)
    Activity = discord.Activity()
    print(Activity.start)
    time = now-Activity.start
    #await ctx.send(f'{user} has been playing {Activity} for {time}')

@client.command()
async def searchurban(ctx, word):
    await ctx.send('https://www.urbandictionary.com/define.php?term=' + str(word))

@client.command()
async def stock(ctx, tickersymbol):
    tickerdata = yf.Ticker(tickersymbol)
    tickerinfo = tickerdata.info
    investment = tickerinfo['shortName']
    await ctx.send(investment)

    today = datetime.date.today()

    date = str(today.year) + "-" + str(today.month) + "-" + str(today.day)

    tickerDF = tickerdata.history(period='1d', start='2020-1-1', end=date)
    priceLast = tickerDF['Close'].iloc[-1]
    priceYest = tickerDF['Close'].iloc[-2]
    pctdiff = round(((priceLast-priceYest)/priceYest)*100, 2)
    await ctx.send(priceLast)
    if pctdiff < 0:
        await ctx.send(f'{investment} is down {pctdiff} percent from yesterday')
    else:
        await ctx.send(f'{investment} is up {pctdiff} percent from yesterday')


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

        #you're not just limited to these games, you can also add other ones
        #make sure that you have appropriate custom emojis as well as role names
        #you can create rolenames using g!createrole <rolename here>
        #(you also dont have to create just gaming roles)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done")

client.run('Token censored')
