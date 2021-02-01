import os
import random
import discord
import csv

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
        with open('leaderboard.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            found = 0
            for x in message.content:
                if x == "💦":
                    await message.channel.send(file=discord.File("Images/"+random.choice(os.listdir('Images/'))))
                    for row in csv_reader:
                        if row[0] == message.author:
                            row[1]=row+1
                            found = 1
                    if found == 0:
                        with open('leaderboard.csv', mode='a') as csvw_file:
                            csv_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                            fields = [message.author,"1"]
                            csv_writer.write(fields)
                
    if "🍆" in message.content:
        print("Eggplant detected")
        await message.channel.send("👀")
        
    if " :rotating_light:" in message.content:
        print("Anti Coomer bot detected")
        await message.channel.send(":rotating_light:BEAN ALERT:rotating_light:")

    if "leaderboard" in message.content:
        with open('leaderboard.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            top_users = [None]*5
            top_scores = [None]*5
            for x in range(5):
                for row in csv_reader:
                    if row[1]>top_scores[x]:
                        if row[0] not in top_users:
                            top_users[x]=row[0]
                            top_scores[x]=row[1]
                    line_count += 1
                print(f'Processed {line_count} lines.')

client.run(TOKEN)
