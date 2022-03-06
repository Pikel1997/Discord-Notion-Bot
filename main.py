import discord
import os
from discord.ext import commands
from call import add_req, ret_req, trun


client = commands.Bot(command_prefix='#', intents = discord.Intents.all())

@client.event
async def on_ready():
  print("On {0.user}".format(client))

@client.command(name="addItem")
async def add_item_to_list(ctx, *msg):
  j = " ".join(msg)
  add_req(j)
  await ctx.channel.send("Item added to Notion database \n https://www.notion.so/d8712d240dfa4bcbb47c71d0d834d932?v=680314a8daa848c4aebf9d2adcef4de4")

@client.command(name="getAll")
async def retrieve_data(ctx):
  emp_l = ret_req()
  await ctx.channel.send(emp_l)

@client.command(name="delAll")
async def truncate(ctx):
  trun()
  await ctx.channel.send("Database Truncated")

client.run(os.environ['bruh'])
