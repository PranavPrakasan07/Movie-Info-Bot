import os
import discord
import requests
import json

my_secret = os.environ['TOKEN']

client = discord.Client()

def get_movie_info(name):
  url = "https://raw.githubusercontent.com/FEND16/movie-json-data/master/json/top-rated-movies-01.json"

  movie_name = name[12:]
  print(movie_name)

  response = requests.get(url)
  json_data = response.json()

  i = 0

  while True:
    try:
      if(json_data[i]['title'] == (movie_name)):

        movie_info = json_data[i]['title'] + "\n - " + str(json_data[i]['releaseDate']) + "\n - " + str(json_data[i]['imdbRating']) + "\n - " + str(json_data[i]['storyline'])

        return(movie_info)

        break
    except IOError:
      return("No  match!")      
      break

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
    await message.channel.send(get_movie_info(message.content))

client.run(my_secret)


