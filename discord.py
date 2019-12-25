import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.id)
    print(client.user.name)
    print("-----------------")

@client.event
async def on_message(message)
    if message.content.startswith("안녕"):
        await message.channel.send("안녕하세요")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
