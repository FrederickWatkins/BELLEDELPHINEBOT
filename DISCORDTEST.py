import os
import random
import discord
from dotenv import load_dotenv

print("Program started")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

print("Token loaded")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    await client.wait_until_ready()
    if message.author == client.user:
        return

    if "💦" in message.content:
        print("Splash found in message")
        for x in message.content:
            if x == "💦":
                await message.channel.send(file=discord.File("Images/"+random.choice(os.listdir('Images/'))))
    if "🍆" in message.content:
        print("Eggplant detected")
        await message.channel.send("👀")

client.run(TOKEN)
