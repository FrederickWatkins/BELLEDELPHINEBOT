import os
import random
import discord

print("Program started")

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
        
    if " :rotating_light:" in message.content:
        print("Anti Coomer bot detected")
        await message.channel.send(":rotating_light:BEAN ALERT:rotating_light:")

client.run(TOKEN)
