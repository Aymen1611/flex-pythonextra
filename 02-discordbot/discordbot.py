import discord

intents = discord.Intents.default()
intents.messages= True


client = discord.Client(intents=intents)
@client.event
async def on_ready():
    guild = client.guilds[0]

    print(client.user, "has connected to discord")
    print(guild.name, "is the name of the server")

    general = guild.text_channels[0]
    print(general.name, "is the name of the channel")
    await general.send("I'm online!")
@client.event
async def on_message(message):
     print(message.channel.name, "the message was posted from this channel")
     print(message.content)
     print(message.author,"is the user who wrote the message")
     print(message.created_at,"is when the message was posted")
     print(message.channel,"is the channel this message was posted in")

     if message.author.bot == False:
        await message.channel.send("Hello " + str(message.author))

client.run("token ")

