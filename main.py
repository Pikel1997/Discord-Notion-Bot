import discord
import os
from discord.ext import commands
from call import add_req, ret_req


client = commands.Bot(command_prefix='#', intents = discord.Intents.all())

@client.event
async def on_ready():
  print("On {0.user}".format(client))

@client.command(name="addItem")
async def add_item_to_list(ctx, *msg):
  j = " ".join(msg)
  add_req(j)
  await ctx.channel.send("Item added")

@client.command(name="getAll")
async def retrieve_data(ctx):
  info = ret_req()
  await ctx.channel.send(info)

client.run(os.environ['DISCORD_KEY'])
