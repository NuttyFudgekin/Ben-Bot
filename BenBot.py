import nextcord
import random
import sys
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!ben", intents=intents)

TOKEN = 'MTE4NjY4MDAxMTcxMzk1Mzg3NA.GHFO0x.3rIOkQshoXQ-9srTGhtMfhg-21Ns48SiQ7OEAA'

PICKUP = ("https://tenor.com/view/ben-talking-ben-ben-talking-talking-ben-call-ben-call-gif-25083332")
YES = ("https://tenor.com/view/talking-ben-yes-gif-27130395")
NO = ("https://tenor.com/view/talking-ben-talking-talking-ben-no-gif-25277070")
BLUH = ("https://tenor.com/view/talking-ben-talking-tongue-out-tongue-talking-ben-tongue-gif-25277068")
LAUGH = ("https://tenor.com/view/talking-ben-laugh-ho-ho-ho-gif-25061559")
HANGUP = ("https://tenor.com/view/talking-ben-phone-hang-up-gif-25061552")

@client.event
async def on_message(message):
    gif_link = [YES, NO, BLUH, LAUGH]
    username = str(message.author).split("#")[0]
    bye = "!ben goodbye ben"

    if bye in message.content.lower():
        await message.channel.send("Bye " + username + "!")
        await message.channel.send(HANGUP)
        print(f"{client.user.name} has logged out")
        sys.exit()
    elif message.content.startswith("!ben"):
        await message.channel.send(random.choice(gif_link))

@client.event
async def on_ready():
    print(f"Logged in as: {client.user.name}")
    await client.get_channel(575429202359222302).send("Ben...")
    await client.get_channel(575429202359222302).send(PICKUP)
  
if __name__ == "__main__":
    client.run(TOKEN)