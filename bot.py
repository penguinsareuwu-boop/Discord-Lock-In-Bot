import discord
import re
import os

BLOCKED_WORDS = [
    "word1",  # replace these with your actual words
    "word2",
    "word3",
]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def replace_slurs(text):
    result = text
    for word in BLOCKED_WORDS:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        result = pattern.sub("skibidi", result)
    return result

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    text_lower = message.content.lower()
    if any(word in text_lower for word in BLOCKED_WORDS):
        clean = replace_slurs(message.content)
        author = message.author.display_name
        channel = message.channel
        await message.delete()
        await channel.send(f"**{author}:** {clean}")

client.run(os.environ.get("TOKEN"))
