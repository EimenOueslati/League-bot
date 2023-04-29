import discord
import requests
import os
from decouple import config
import json
import summoner

GREETING_MESSAGE = "Hello there! \nI am a friendly discord bot that will help you track some statistics about you league of legends account. \nIf you want some advice on how to improve, or just want some people to play with, don't hesitate to send a message in the league of legends channel and I am sure everyone will be happy to help."
GET_SUMMONER_BY_NAME_ENDPOINT = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
GET_ENTRIES_BY_SUMID = "https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/"
API_KEY = {'api_key' : str(config('KEY'))}
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
    summoner_name = message.content.lstrip("&elo")
    summoner_name = summoner_name.strip()
    encrypted_summ_id = get_summoner_id(summoner)
    if encrypted_summ_id is None:
      await message.channel.send("Sorry! Could not find you account stats. Maybe try checking if the name you entered is correct.")
      return
    summoner_obj = get_summoner_stats(encrypted_summ_id)



def get_summoner_id(name):
  response = requests.get(GET_SUMMONER_BY_NAME_ENDPOINT + name, params=API_KEY )

  if response.status_code != 200:
    return None
  
  return json.loads(response.text)['id']
    


