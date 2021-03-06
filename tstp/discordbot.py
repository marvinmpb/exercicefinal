import discord
import os

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

client.run('ODA0MTE1MzA0MDU3MTQzMzE2.YBHovA.Ibjn_0FUqNOjZnVIthz1hgh3CAE')