import os
import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

# Replace 'file_extension' with the file type you are interested in, ".jpg" or ".exe"
file_extension = 'file_extension'

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.attachments:
        for attachment in message.attachments:
            if attachment.filename.endswith(file_extension):
                await attachment.save(os.path.join(os.getcwd(), attachment.filename))

# Replace 'discord_server_id' with the ID of the server you want to scrape
client.run(os.getenv('DISCORD_TOKEN'))
