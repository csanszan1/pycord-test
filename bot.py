import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send('Hello!')

client.run('MTA1NTE0NzM0NDA2MjA1ODQ5Nw.GfbZxe.-zWKXjnKTN-MvqAhAzWkk56FOl1HNkbTyGs698')
