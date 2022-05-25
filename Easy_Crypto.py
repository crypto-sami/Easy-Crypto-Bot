import json
import time
import random
import discord
from discord import client
from discord.ext import commands
from discord.ext.commands import Bot
import cryptocompare
from datetime import datetime
import asyncio
from discord.user import User
from datetime import date

bitc = 0
ether = 0
add10btc = 10
adminperm = 344370497666023435
workstation = 1
minerate = 25
money = 0
price_last = 0
date_last = 0
github_link = "http://easycrypto.us.to"
mine1 = 0.001
mine2 = 0.0001
mine3 = 0.00001

basiccommands = (f"\n**?help** - Display this list \n**?create** - Create a new user under your discord ID \n**?del** - Delete your account and data\n**?btc** - Receive the latest Bitcoin price\n**?eth** - Receive the latest Ethereum price\n")
excommands1 = (f"**?mb** - Use your wokrstation to mine Bitcoin\n**?me** - Use your workstation to mine Ethereum\n**?sell btc** - Sell all your bitcoin\n**?sell eth** - Sell all your ethereum\n**?workstation** - View your current workstation specifications\n**?upgrade** - Upgrade your workstation to the next level - Each upgrade costs $500\n**?inventory** - View your levels of Bitcoin and Ethereum and also your account money\n")

work1mine = 25
work1_success = 2
cpul1 = (f"The level 1 CPU \nIntel Core I5-7600K")
ram1 = (f"The level 1 RAM \n8Gb running at 2400Mhz")
gpu1 = (f"The level 1 GPU \nGTX 1070 with 8Gb VRAM")
psu1 = (f"The level 1 Power Supply \nSeasonic 550 Watt PSU")

work2mine = 20
work2_success = 2
cpul2 = (f"The level 2 CPU \nIntel Core I7-7700K")
ram2 = (f"The level 2 RAM \n16Gb running at 2400Mhz")
gpu2 = (f"The level 2 GPU \nGTX 1080 with 8Gb VRAM")
psu2 = (f"The level 2 Power Supply \nThermaltake 650 Watt PSU")

work3mine = 15
work3_success = 2
cpul3 = (f"The level 3 CPU \nIntel Core I7-11700K")
ram3 = (f"The level 3 RAM \n16Gb running at 3200Mhz")
gpu3 = (f"The level 3 GPU \nRTX 2070 with 8Gb VRAM")
psu3 = (f"The level 3 Power Supply \nCooler Master 750 Watt PSU")

work4mine = 10
work4_success = 2
cpul4 = (f"The level 4 CPU \nIntel Core I9-10900K")
ram4 = (f"The level 4 RAM \n32Gb running at 3000Mhz")
gpu4 = (f"The level 4 GPU \nRTX 3080 with 10Gb VRAM")
psu4 = (f"The level 4 Power Supply \nEVGA 950 Watt PSU")

work5mine = 5
work5_success = 2
cpul5 = (f"The level 5 CPU \nIntel Core I9-11900K")
ram5 = (f"The level 5 RAM \n64Gb running at 3600Mhz")
gpu5 = (f"The level 5 GPU \nRTX 3090 with 24Gb VRAM")
psu5 = (f"The level 5 Power Supply \nEVGA 1100 Watt PSU")


welcome1 = (f"Welcome to 'Easy Crypto', a bot designed and developed by Sami Turk. With this bot you can use your workstation to mine Bitcoin and/or Ethereum.\n")
welcome2 = (f"When you mine a portion of a certain coin, you'll be shwon the 'sell now' price, its up to you wether to sell now, or battle the fluctuating Crytpo market. Good Luck!\n")
welcome3 = (f"\nDuring your time using Easy Crypto, you may encouter an unknown bug, if this is the case, please let Sami#3255 know about this as soon as possible.\n")
welcome4 = (f"Normally, to get started with this bot, you would need to do ?create to create an account, but i've already done that for you.\n")
welcome5 = (f"Your account is created so start mining by either ?mb for bitcoin or ?me for ethereum. For more information, ?help is your friend")

bot = Bot(command_prefix='?')
TOKEN = json.loads(open("token.json", "r").read())

def getstockprice(code):
    price = cryptocompare.get_price("code", currency="GBP")
    return price

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
            elif data[user]["workstation"] == 4:
                embedVar=discord.Embed(title="Your current operational workstation", url="", color=0x00ff00)
                embedVar.add_field(name="CPU", value=f"{cpul4}")
                embedVar.add_field(name="RAM", value=f"{ram4}")
                embedVar.add_field(name="GPU", value=f"{gpu4}")
                embedVar.add_field(name="Power Supply", value=f"{psu4}")
                embedVar.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
                embedVar.set_author(name=message.author.display_name, url="", icon_url=message.author.avatar_url)
                await message.reply(embed=embedVar)
            elif data[user]["workstation"] == 5:
                embedVar=discord.Embed(title="Your current operational workstation", url="", color=0x00ff00)
                embedVar.add_field(name="CPU", value=f"{cpul5}")
                embedVar.add_field(name="RAM", value=f"{ram5}")
                embedVar.add_field(name="GPU", value=f"{gpu5}")
                embedVar.add_field(name="Power Supply", value=f"{psu5}")
                embedVar.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
                embedVar.set_author(name=message.author.display_name, url="", icon_url=message.author.avatar_url)
                await message.reply(embed=embedVar)
        else:
            await message.reply("No account registered, please use ?create to register")


    if message.content == ("?get started"):
        await message.reply(f"{welcome1}{welcome2}{welcome3}{welcome4}{welcome5}")
        user = message.author.id
        if user in data:
            await message.reply(f"Account already created user: {user}")
        else:
            data[str(user)] = {"user": user, "bitc": bitc, "ether": ether, "workstation": workstation, "minerate": minerate, "money": money}
            save()

    if message.content == ("?2help"):  
        embedVar = discord.Embed(title="Welcome to the Help menu", description="View Bot commands below", color=0x00ff00)
        embedVar.set_author(name="Easy Crypto by Sami Turk")
        embedVar.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
        embedVar.add_field(name="Basic Commands", value=f"{basiccommands}{excommands1}")
        embedVar.set_footer(text="Help menu requested by: {}".format(message.author.display_name))
        await message.reply(embed=embedVar)

    if message.content == ("?help"):
        embedVar=discord.Embed(title="Crypto Help Centre", url="", color=0x00ff00)
        embedVar.add_field(name="Commands", value=f"{basiccommands}{excommands1}")
        embedVar.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
        embedVar.set_footer(text=f"Track the development at {github_link}")
        await message.reply(embed=embedVar)

    if message.content == ("?inventory"):
        user = str(message.author.id)
        usercash = data[user]["money"]
        userbtc = data[user]["bitc"]
        usereth = data[user]["ether"]
        await message.reply(f"Cash Balance: {usercash} \nBitcoin Amount: {userbtc} \nEthereum amount: {usereth}")

    if message.content == ("?mb"):
        user = str(message.author.id)
        await message.reply("Mining started, please wait 1 Minute")
        await asyncio.sleep(60)
        if user in data:
            minesuccess = random.randint(1,3)
            if minesuccess == 1:
                data[user]["bitc"]+=0.001
                amountadded = 0.001
                save()
            elif minesuccess == 2:
                data[user]["bitc"]+=0.0001
                amountadded = 0.0001
                save()
            elif minesuccess == 3:
                data[user]["bitc"]+=0.0001
                amountadded = 0.0001
                save()
            else: await message.reply("Error Counting BTC")
            save()
            userbtcamount = data[user]["bitc"]
            embedVar=discord.Embed(title=f"{amountadded} Bitcoin added to account!", url="", color=0x00ff00)
            embedVar.add_field(name=f"Your balance is now {userbtcamount}", value=f"The latest BTC price is {getbtcprice()}")
            embedVar.set_image(url="https://wompampsupport.azureedge.net/fetchimage?siteId=7575&v=2&jpgQuality=100&width=700&url=https%3A%2F%2Fi.kym-cdn.com%2Fentries%2Ficons%2Foriginal%2F000%2F029%2F959%2FScreen_Shot_2019-06-05_at_1.26.32_PM.jpg")
            embedVar.set_footer(text="Bitcoin added to user: {}".format(message.author.display_name))
            bitcoinamount = data[user]["bitc"]
            sellnowprice = bitcoinamount*getbtcprice()
            embedVar.add_field(name="Bitcoin sell now", value=f"Sell all Bitcoin now for {sellnowprice}")
            await message.reply(embed=embedVar)
        else:
            await message.reply("No account, please use ?create")




    if message.content.startswith("?price"):
        messsage_len = len(message)
        if messsage_len == 10:
            await message.reply("10")

        if messsage_len == 11:
            await message.reply("11")

    if message.content == ("?me"):
        user = str(message.author.id)
        await message.reply("Mining started, please wait 1 Minute")
        await asyncio.sleep(60)
        if user in data:
            minesuccess = random.randint(1,3)
            if minesuccess == 1:
                data[user]["ether"]+=0.001
                amountadded = 0.001
                save()
            elif minesuccess == 2:
                data[user]["ether"]+=0.0001
                amountadded = 0.0001
                save()
            elif minesuccess == 3:
                data[user]["ether"]+=0.0001
                amountadded = 0.0001
                save()
            else: await message.reply("Error Counting ETH")
            userethamount = data[user]["ether"]
            embedVar=discord.Embed(title=f"{amountadded} Ethereum added to account!", url="", color=0x00ff00)
            embedVar.add_field(name=f"Your balance is now {userethamount}", value=f"The latest ETH price is {getethprice()}")
            embedVar.set_image(url="https://wompampsupport.azureedge.net/fetchimage?siteId=7575&v=2&jpgQuality=100&width=700&url=https%3A%2F%2Fi.kym-cdn.com%2Fentries%2Ficons%2Foriginal%2F000%2F029%2F959%2FScreen_Shot_2019-06-05_at_1.26.32_PM.jpg")
            embedVar.set_footer(text="Ethereum added to user: {}".format(message.author.display_name))
            etheramount = data[user]["ether"]
            sellnowprice = etheramount*getethprice()
            embedVar.add_field(name="Ethereum sell now", value=f"Sell all Ethereum now for {sellnowprice}")
            await message.reply(embed=embedVar)
        else:
            await message.reply("No account, please use ?create")

    
    if message.content == '?create':
        user = message.author.id
        if user in data:
            await message.reply(f"Account already created user: {user}")
        else:
            data[str(user)] = {"user": user, "bitc": bitc, "ether": ether, "workstation": workstation, "minerate": minerate, "money": money, "price_last": price_last, "date_last": date_last}
            save()
            await message.reply(f"New Member created under ID: {user}")

    if message.content == ("?sell btc"):
        user = str(message.author.id)
        ammtoadd = data[user]["bitc"]*getbtcprice()
        data[user]["money"]+=ammtoadd
        data[user]["bitc"]=0
        usercash = data[user]["money"]
        await message.reply(f"All bitcoin sold, your account funds are now: {usercash}")

    if message.content == ("?sell eth"):
        user = str(message.author.id)
        ammtoadd = data[user]["ether"]*getethprice()
        data[user]["money"]+=ammtoadd
        data[user]["ether"]=0
        usercash = data[user]["money"]
        await message.reply(f"All ethereum sold, your account funds are now: {usercash}")
     

    if message.content == ("?upgrade"):
        user = str(message.author.id)
        currentstation = data[user]["workstation"]
        if currentstation < 5:
            if data[user]["money"] > 500:
                data[user]["money"]-=500
                save()
                userfunds = data[user]["money"]
            
                embedVar=discord.Embed(title="Workstation Upgraded!", url="", color=0x00ff00)
                embedVar.add_field(name="Price", value=f"$500 Reduced from account")
                embedVar.add_field(name="Remanining funds", value=f"{userfunds} is remaining in your account")
                embedVar.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
                embedVar.set_footer(text="Workstation upgrade requested by: {}".format(message.author.display_name))
                await message.reply(embed=embedVar)
            else:
                await message.reply("Insufficient money, upgrade cost $500")


    if message.content == '?del':
        user = str(message.author.id)
        if user in data:
            del data[user]
            save()
            await message.reply(f"Account Deleted {user}")
        else:
            await message.reply("No account registered to delete")
         

    if message.content.startswith('?btc'):
        user = str(message.author.id)
        current_time = datetime.now()
        current_date = str(date.today())
        current_btc_price = getbtcprice()
        last_price = data[user]["price_last"]
        last_date = data[user]["date_last"]
        embedVar = discord.Embed(title=f"Bitcoin Price is {current_btc_price}", description=f"Your last price was on ***{last_date}*** and the price was ***{last_price}***", color=0x00ff00)
        embedVar.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
        await message.reply(embed=embedVar)
        if user in data:
            data[user]["date_last"]=current_date
            data[user]["price_last"]=current_btc_price
            save()

    if message.content == ("?eth"):
        current_time1 = datetime.now()
        current_time = current_time1.strftime("%H:%M:%S")
        current_eth_price = getethprice()
        embedVar = discord.Embed(title=f"Ethereum Price is {current_eth_price}", description=f"Correct as of: {current_time}", colour =0x00ff00 )
        embedVar.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
        embedVar.set_footer(text="Price Compare has not been implemeted for Ethereum yet")
        await message.reply(embed=embedVar)

bot.run(TOKEN)