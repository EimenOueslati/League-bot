import discord
import requests
import os
from decouple import config
import json
import summoner
from typing import List

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
    await message.channel.send(GREETING_MESSAGE)

  elif message.cotent.lower().startwith("&elo"):
    summoner_name = message.content.lstrip("&elo")
    summoner_name = summoner_name.strip()
    encrypted_summ_id = get_summoner_id(summoner_name)
    if encrypted_summ_id is None:
      await message.channel.send("Sorry! Could not find you account stats. Maybe try checking if the name you entered is correct.")
      return
    summoner_obj = get_summoner_stats(encrypted_summ_id, summoner_name)
    if summoner_obj.soloQ is None and summoner_obj.flex is None:
      await message.channel.send(f"Sorry! No stats are available for {summoner_name} .")
      return
    await message.channel.send(parse_stats(summoner_obj))



def get_summoner_id(name):
  response = requests.get(GET_SUMMONER_BY_NAME_ENDPOINT + name, params=API_KEY )

  if response.status_code != 200:
    return None
  
  return json.loads(response.text)['id']
    

def get_summoner_stats(id, name):

  response = requests.get(GET_ENTRIES_BY_SUMID + id, params=API_KEY)

  if response != 200:
    return None
  
  response = json.loads(response.text)
  stats: List[summoner.Ranked]
  for stat in response:
    stats.append(summoner.Parce_ranked(stat))

  if stats = []:
    return summoner.Summoner(name, None, None)
  elif len(stats) = 1:
    ranked = stats[0]
    if ranked.queueType == "RANKED_FLEX_SR":
      return summoner.Summoner(name, ranked, None)
    else:
      return summoner.Summoner(name, None, ranked)
  else:
    return summoner.Summoner(name, stats[0], stats[1])

def parse_stats(summ: summoner.Summoner) -> str:
  ret = f"{summ.summonerName}: \n"
  if summ.soloQ is not None:
     soloQ = summ.getSoloQ()
     ret = ret + f"SOLOQ: rank: {soloQ[0]}{soloQ[1]}, LP: {soloQ[2]}, {int(soloQ[3]) + int(soloQ[4])} games, wins: {soloQ[3]}, losses{soloQ[4]}" 

  if summ.soloQ is not None:
     flex = summ.flex()
     ret = ret + f"SOLOQ: rank: {flex[0]}{flex[1]}, LP: {flex[2]}, {int(flex[3]) + int(flex[4])} games, wins: {flex[3]}, losses{flex[4]}"

  return ret

  
  
