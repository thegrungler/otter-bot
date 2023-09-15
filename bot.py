#! /usr/bin/env python3

import discord
from discord import app_commands
from dotenv import load_dotenv
import os
import pickle

intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)
tree = app_commands.CommandTree(client)

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

banned_words = []

try:
  f = open("words.pkl", "x")
  f.close()
except:
  print("words.pkl already exists")

with open("words.pkl", "rb") as myFile:
  try:
    banned_words = pickle.load(myFile)
  except:
    print("words file empty")
  myFile.close()

def save_words():
    with open("words.pkl", "wb") as myFile:
        pickle.dump(banned_words, myFile)
        myFile.close()

@client.event
async def on_message(message):
    if message.content.upper() == "HI":
       await message.channel.send("hi "+message.author.display_name+"!")
    if message.content.upper() == "BYE":
       await message.channel.send("see you later alligator")
    if "STROGANOFF" in message.content.upper():
       await message.channel.send("@bridget9124")
    if message.content.upper() == "I LOVE YOU":
       await message.channel.send("i love you too "+message.author.display_name+"! 💜")
    if ":A_HuStare:" in message.content:
       await message.add_reaction("<:heliosfalse:1136775548677394582>")
    if "https://tenor.com/view/fnb-get-this-man-a-true-gif-25257480" in message.content:
       await message.channel.send("<:HydeTrue:1138316187403559022><:soltrue:1136771377827946607><:BadSolTrue:1152360743417675796>")
    for word in banned_words:
        #print (word.upper())
        #print (message.content.upper())
        if word.upper() in message.content.upper():
            if message.author.id != 1152333124303343617:
                await message.delete()
            print("deleted message \""+message.content+"\" from user "+message.author.display_name)

@client.event
async def on_member_join(member):
   channel = client.get_channel(1136707030858612830)
   await channel.send("hi "+member.display_name+"!")

@client.event 
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Game(name="with poke's sanity"))
  print("Syncinc commands")
  await tree.sync()
  print("Bot is Ready!")

@tree.command(name="add_word",
              description="add new word to be auto removed")
@app_commands.describe(word="the word to be auto removed")
async def add_word(interaction, word: str):
    if interaction.user.id == 379424322361622528:
        if word not in banned_words: 
            banned_words.append(word)
            save_words()
            print("added word "+word+" and saved")
            await interaction.response.send_message("added word "+word+" and saved")
        else:
            await interaction.response.send_message("word already banned")
    await interaction.response.send_message("you don't have permission to use this command")

@tree.command(name="greet",
              description="say hi to an user")
@app_commands.describe(user = "user to say hi to")
async def add_word(interaction, user: discord.Member):
   await interaction.response.send_message("hi <@"+str(user.id)+">!")

@tree.command(name="kill",
              description="fucking murder someone")
@app_commands.describe(user = "user to annihilate")
async def add_word(interaction, user: discord.Member):
   await interaction.response.send_message("<@"+str(user.id)+"> has fucking died")
        
client.run(DISCORD_TOKEN)