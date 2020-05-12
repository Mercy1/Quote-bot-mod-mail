import discord
import asyncio
from discord.voice_client import VoiceClient
from discord.ext import commands
import random
import os
from dotenv import load_dotenv
import youtube_dl

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


#responces/quotes
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    hello_things = [
        'hello there',
        'Hi %user%',
        'What do you need? ^^',
    ]

        
    if message.content =='hey!':
        responce = random.choice(hello_things)
        await message.channel.send(responce)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        'The English language can not fully capture the depth and complexity of my thoughts, so I’m incorporating emojis into my speech to better express myself. 😉.',
        'Great, I’d like your $8-est bottle of wine, please.',
        'Captain Wuntch. Good to see you. But if you’re here, who’s guarding Hades?',
        'https://giphy.com/gifs/brooklynninenine-nbc-brooklyn-nine-b99-RkJv73bPgwp9crecB2',
        'https://gph.is/g/4AjOlPQ',

        
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    elif message.content == 'logit':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


#music v2

    

client.run('Hi there ^^')
