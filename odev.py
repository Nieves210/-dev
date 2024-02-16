import discord
import random

def sifree (uzunluk):


    harfler="abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sayilar="1234567890"
    semboller="+-/*!&$#?=@"

    sifre=""

    for i in range(uzunluk):

        if i % 3 ==0:
            sifre += random.choice(harfler)
        if i % 3 ==1:
            sifre += random.choice(sayilar)    
        if i % 3 ==2:
            sifre += random.choice(semboller)

    return sifre



def yazi_tura():
    para = random.randint(0, 2)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"
    
    
def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)


# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith("şifre oluştur"):
        await message.channel.send(sifree(20))
    elif message.content.startswith('$smile'):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith('$coin'):
        await message.channel.send(yazi_tura())
    else:
        await message.channel.send(message.content)

client.run("TOKEN")
