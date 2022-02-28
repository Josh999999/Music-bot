import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

client.run("OTQ1MDA5ODUyNzMwNzAzOTEy.YhJ7Ag.mC-tBthijKsfgPOPRp7B-nsju_I")