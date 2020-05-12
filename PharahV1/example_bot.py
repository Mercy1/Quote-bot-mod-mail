import discord
import asyncio
from discord.voice_client import VoiceClient
from discord.ext import commands
import random
import os
from dotenv import load_dotenv
import youtube_dl

client = discord.Client()

#Youtube stuff not working?
async def main_loop():
    print('Working')
    vc = client.guild[0].voice.channels
    targ = vc[len(vc)-1]
    vc_client = await targ.connect()
    url = 'https://www.youtube.com/watch?v=s9wtZKTDufM&list=PL5zohYERz9XC5UKb4Btf3KLcpaVqTWWvH'
    player = await vc_client.create_ytdl_player(url)
    player.start()

@client.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await main_loop()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


#responces/quotes
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello!'):
        await message.channel.send('Hello!')

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
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    elif message.content == 'loggit':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


#music v2

    

client.run('NDYzNzQ0NjE2NzczMTg5NjMy.XnSIMA.2tEE66dodUuXRh83YKF3XjNni8U')
