import json
import random
import discord
from discord import client
from discord.ext import commands
from discord.ext.commands import Bot
import cryptocompare
from datetime import datetime
import asyncio
from discord.user import User

bitc = 0
add10btc = 10
adminperm = 344370497666023435
workstation = 1


basiccommands = (f"\n**?help** - Display this list \n**?create** - Create a new user under your discord ID \n**?del** - Delete your account and data\n**?btc** - Receive the latest Bitcoin price\n**?eth** - Receive the latest Ethereum price\n")
excommands1 = (f"**?mine** - Use all your resources to mine crypto (the default mining currency is BTC)\n**?inventory** - View your inventory, including workstations and crypto amounts\n**?upgrades** - View detailed upgrade levels for your workstation(s) and their benefits\n**?workstation** - View your current workstation specifications")

work1mine = 25
cpul1 = (f"The basic CPU \nIntel Core I5-7600K")
ram1 = (f"The basic RAM \n8Gb running at 2400Mhz")
gpu1 = (f"The basic GPU \nGTX 1070 with 8Gb VRAM")
psu1 = (f"The basic Power Supply \nSeasonic 550 Watt PSU")

work2mine = 20
cpul2 = (f"The more advanced CPU \nIntel Core I7-7700K")
ram2 = (f"The more advanced RAM \n16Gb running at 2400Mhz")
gpu2 = (f"The more advanced GPU \nGTX 1080 with 8Gb VRAM")
psu2 = (f"The more advanced Power Supply \nThermaltake 650 Watt PSU")

work3mine = 15
cpul3 = (f"The even more advanced CPU \nIntel Core I7-11700K")
ram3 = (f"The even more advanced RAM \n16Gb running at 3200Mhz")
gpu3 = (f"The even more advanced GPU \nRTX 2070 with 8Gb VRAM")
psu3 = (f"The even more advanced Power Supply \nCooler Master 750 Watt PSU")


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

    if message.content == ("?workstation"):
        user = str(message.author.id)
        if user in data:
            if data[user]["workstation"] == 1:
                embedVar=discord.Embed(title="Your current operational workstation", url="", color=0x00ff00)
                embedVar.add_field(name="CPU", value=f"{cpul1}")
                embedVar.add_field(name="RAM", value=f"{ram1}")
                embedVar.add_field(name="GPU", value=f"{gpu1}")
                embedVar.add_field(name="Power Supply", value=f"{psu1}")
                embedVar.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
                embedVar.set_author(name=message.author.display_name, url="", icon_url=message.author.avatar_url)
                await message.reply(embed=embedVar)
            elif data[user]["workstation"] == 2:
                embedVar=discord.Embed(title="Your current operational workstation", url="", color=0x00ff00)
                embedVar.add_field(name="CPU", value=f"{cpul2}")
                embedVar.add_field(name="RAM", value=f"{ram2}")
                embedVar.add_field(name="GPU", value=f"{gpu2}")
                embedVar.add_field(name="Power Supply", value=f"{psu2}")
                embedVar.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
                embedVar.set_author(name=message.author.display_name, url="", icon_url=message.author.avatar_url)
                await message.reply(embed=embedVar)
            elif data[user]["workstation"] == 3:
                embedVar=discord.Embed(title="Your current operational workstation", url="", color=0x00ff00)
                embedVar.add_field(name="CPU", value=f"{cpul3}")
                embedVar.add_field(name="RAM", value=f"{ram3}")
                embedVar.add_field(name="GPU", value=f"{gpu3}")
                embedVar.add_field(name="Power Supply", value=f"{psu3}")
                embedVar.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
                embedVar.set_author(name=message.author.display_name, url="", icon_url=message.author.avatar_url)
                await message.reply(embed=embedVar)
        else:
            await message.reply("No account registered, please use ?create to register")


    if message.content == ("?2help"):
        #await message.reply(f"```{basiccommands}\n{excommands1}```")
        #async def embedvar():  
        embedVar = discord.Embed(title="Welcome to the Help menu", description="View Bot commands below", color=0x00ff00)
        embedVar.set_author(name="Sami's Bot by Sami Turk")
        embedVar.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
        embedVar.add_field(name="Basic Commands", value=f"{basiccommands}{excommands1}")
        embedVar.set_footer(text="Help menu requested by: {}".format(message.author.display_name))
        await message.reply(embed=embedVar)

    if message.content == ("?help"):
        embedVar=discord.Embed(title="Crypto Help Centre", url="", color=0x00ff00)
        embedVar.add_field(name="Commands", value=f"{basiccommands}{excommands1}")
        embedVar.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
        #embedVar.set_author(name=message.author.display_name, url="", icon_url=message.author.avatar_url)
        embedVar.set_footer(text="Help menu requested by: {}".format(message.author.display_name))
        await message.reply(embed=embedVar)



    
    if message.content == '?create':
        user = message.author.id
        if user in data:
            await message.reply(f"Account already created user: {user}")
        else:
            data[str(user)] = {"user": user, "bitc": bitc, "workstation": workstation}
            save()
            await message.reply(f"New Member created under ID: {user}")




    if command[0] == '?addbtc':
        del command[0]
        user = message.author.id
        data[str(user)]["bitc"]+=float(command[0])
        await message.reply(f"{command[0]} Bitcoin added under ID {user}")
        save()
        



    if message.content == '?del':
        user = str(message.author.id)
        if user in data:
            del data[user]
            save()
            await message.reply(f"Account Deleted {user}")
        else:
            await message.reply("No account registered to delete")
       
      

    #if message.content == ("?btc"):
        #await message.reply(f"The latest bitcoin price is {getbtcprice()} GBP")

    if message.content.startswith('?btc'):
        current_time = datetime.now()
        embedVar = discord.Embed(title="Bitcoin Price (GBP)", description=f"The latest BTC price is **{getbtcprice()}**", color=0x00ff00)
        embedVar.add_field(name="Time", value=f"Correct as of: {current_time}", inline=False)
        embedVar.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
        await message.reply(embed=embedVar)

    if message.content == ("?eth"):
        current_time = datetime.now()
        embedVar = discord.Embed(title="Ethereum Price (GBP)", description=f"The latest ETH price is **{getethprice()}**", colour =0x00ff00 )
        embedVar.add_field(name="Time", value=f"Correct as of: {current_time}", inline=False)
        embedVar.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
        await message.reply(embed=embedVar)













bot.run(TOKEN)