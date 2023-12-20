import nextcord
from openai import OpenAI

client = OpenAI(api_key='Insert API key here')

intents = nextcord.Intents.default()
intents.message_content = True

token = 'Insert Token here'

clientD = nextcord.Client(intents=intents)

@clientD.event
async def on_ready():
    print("Logged in as {0.user}".format(clientD))


@clientD.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    print(username + " said " + user_message.lower() + " in " + channel)

    if message.channel.name == clientD.user:
        return
    
    if message.channel.name == "school":
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}],
        max_tokens=3000
        )        
        # return response.choices[0].message.content
        print(response.choices[0].message.content)
           

clientD.run(token)