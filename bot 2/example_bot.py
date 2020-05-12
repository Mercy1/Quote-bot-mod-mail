import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')   

client.run('NDYzNzQ0NjE2NzczMTg5NjMy.XnSIMA.2tEE66dodUuXRh83YKF3XjNni8U')
