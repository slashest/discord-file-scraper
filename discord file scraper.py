import os
import discord
from dotenv import load_dotenv

load_dotenv()


file_extension = '.jpg'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

@client.event
async def on_message(message):
    if message.attachments:
        for attachment in message.attachments:
            if attachment.filename.endswith(file_extension):
                save_path = os.path.join(os.getcwd(), attachment.filename)
                await attachment.save(save_path)
                print(f'Saved {attachment.filename} from {message.author} in {message.channel}')
                
client.run(os.getenv('DISCORD_TOKEN'))
