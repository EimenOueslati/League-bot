import discord

greetingMessage = "Hello there! \nI am a friendly discord bot that will help you track some statistics about you league of legends account. \nIf you want some advice on how to improve, or just want some people to play with, don't hesitate to send a message in the league of legends channel and I am sure everyone will be happy to help."

client = discord.client()

@client.event
async def on_ready():
  print('we have loged in as {0.user}'
  .format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  elif message.content.lower().startswith("&helo"):
    await message.channel.send(greetingMessage)

  elif message.cotent.lower().startwith("&elo"):
    summoner = message.content.lstrip("&elo")
    summoner = summoner.strip()
    # stats = 

 
