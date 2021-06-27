import os
import discord
import requests
import json
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']

client = discord.Client()

def get_movie_info(key):
  url = "https://raw.githubusercontent.com/FEND16/movie-json-data/master/json/top-rated-movies-01.json"

  response = requests.get(url)
  json_data = response.json()

  i = 0

  while True:
    try:
      if(json_data[i]['title'] == (key)):

        movie_info = "\n\n Title - " + json_data[i]['title'] + "\n Release Date - " + str(json_data[i]['releaseDate']) + "\nIMDB Rating - " + str(json_data[i]['imdbRating']) + "\nStoryline - " + str(json_data[i]['storyline']) + "\nGenre - " + str(json_data[i]['genres'])

        return(movie_info)

    except IndexError:
      return("No  match!")      

    i += 1

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('#hello'):            
    await message.channel.send('Hello!')


  if message.content.startswith('#movie_name'):
    await message.channel.send(get_movie_info(message.content[12:]))

keep_alive()
client.run(my_secret)


