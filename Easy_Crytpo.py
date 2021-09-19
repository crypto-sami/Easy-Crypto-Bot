import json
import random
import discord
from discord import client
from discord.ext import commands
from discord.ext.commands import Bot
import cryptocompare
from datetime import datetime

from discord.user import User

bitc = 0
add10btc = 10
adminperm = 344370497666023435


basiccommands = (f"\n**?help** - Display this list \n**?create** - Create a new user under your discord ID \n**?del** - Delete your account and data\n")
excommands1 = (f"**?mine** - Use all your resources to mine crypto (the default mining currency is BTC)\n**?inventory** - View your inventory, including workstations and crypto amounts\n**?upgrades** - View detailed upgrade levels for your workstation(s) and their benefits\n**?workstation** - View your current workstation specifications")
wup1 = ("Upgrade Level 1 - ")


bot = Bot(command_prefix='?')
TOKEN = json.loads(open("token.json", "r").read())  

def getbtcprice():
    string = cryptocompare.get_price('BTC', currency='GBP')
    btcprice = string['BTC']['GBP']
    return(btcprice)

def getethprice():
    string = cryptocompare.get_price("ETH", currency="GBP")
    ethprice = string['ETH']["GBP"]
    return(ethprice)



@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    await bot.change_presence(activity = discord.Game('?help')) 

def save():
  global data
  open("data.json", "w").write(json.dumps(data))

try:
    data = json.loads(open("data.json", "r").read())
except:
    open("data.json", "w").write(json.dumps({}))
    data = {}


@bot.event
async def on_message(message):
    command = message.content.split(" ")

    #if message.content == ("?upgrades"):
    #    await

    if message.content == ("?2help"):
        #await message.reply(f"```{basiccommands}\n{excommands1}```")
        #async def embedvar():  
        embedVar = discord.Embed(title="Welcome to the Help menu", description="View Bot commands below", color=0x00ff00)
        embedVar.set_author(name="Sami's Bot by Sami Turk")
        embedVar.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
        embedVar.add_field(name="Basic Commands", value=f"{basiccommands}{excommands1}")
        embedVar.set_footer(text="Help menu requested by: {}".format(message.author.display_name))
        await message.channel.send(embed=embedVar)

    if message.content == ("?help"):
        embedVar=discord.Embed(title="Crypto Help Centre", url="", color=0x00ff00)
        embedVar.add_field(name="Commands", value=f"{basiccommands}{excommands1}")
        embedVar.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
        #embedVar.set_author(name=message.author.display_name, url="", icon_url=message.author.avatar_url)
        embedVar.set_footer(text="Help menu requested by: {}".format(message.author.display_name))
        await message.channel.send(embed=embedVar)



    
    if message.content == '?create':
        user = message.author.id
        if user in data:
            await message.reply(f"Account already created user: {user}")
        else:
            data[str(user)] = {"user": user, "bitc": bitc}
            save()
            await message.reply(f"New Member created under ID: {user}")




    if command[0] == '?addbtc':
        del command[0]
        user = message.author.id
        data[str(user)]["bitc"]+=float(command[0])
        await message.reply(f"{command[0]} Bitcoin added under ID {user}")
        save()
        



    if message.content == '?del':
        user = message.author.id
        for key in data:
            if 'user' in data[key]:
                del data[key]
                await message.reply(f"Member ID: {user} deleted")
                save()
                break

    #if message.content == ("?btc"):
        #await message.reply(f"The latest bitcoin price is {getbtcprice()} GBP")

    if message.content.startswith('?btc'):
        current_time = datetime.now()
        embedVar = discord.Embed(title="Bitcoin Price (GBP)", description=f"The latest BTC price is **{getbtcprice()}**", color=0x00ff00)
        embedVar.add_field(name="Time", value=f"Correct as of: {current_time}", inline=False)
        await message.reply(embed=embedVar)

    if message.content == ("?eth"):
        current_time = datetime.now()
        embedVar = discord.Embed(title="Ethereum Price (GBP)", description=f"The latest ETH price is **{getethprice()}**", colour =0x00ff00 )
        embedVar.add_field(name="Time", value=f"Correct as of: {current_time}", inline=False)
        await message.reply(embed=embedVar)













bot.run(TOKEN)