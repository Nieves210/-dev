import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def topla(ctx, s1=5, s2=0):
    await ctx.send(s1+s2)   

@bot.command()
async def carpma(ctx,s3=4, s4=0):
    await ctx.send(s3*s4)    

@bot.command()
async def cikarma(ctx,s5=4, s6=0):
    await ctx.send(s5-s6) 

@bot.command()
async def bolme(ctx,s7=4, s8=0):
    await ctx.send(s7/s8)     

@bot.command()
async def yazitura(ctx,tahmin):
    a=["yazı","tura"]
    b=random.choice(a)
    if tahmin==b:
        await ctx.send("doğru tahmin ettin")
    else:
        await ctx.send(f"yanlış tahmin ettin, cevap {b}")



class PersistentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Green', style=discord.ButtonStyle.green, custom_id='persistent_view:green')
    async def green(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is green.', ephemeral=True)

    @discord.ui.button(label='Red', style=discord.ButtonStyle.red, custom_id='persistent_view:red')
    async def red(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is red.', ephemeral=True)

    @discord.ui.button(label='Grey', style=discord.ButtonStyle.grey, custom_id='persistent_view:grey')
    async def grey(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is grey.', ephemeral=True)


class PersistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents)

    async def setup_hook(self) -> None:
        self.add_view(PersistentView())

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


bot = PersistentViewBot()


@bot.command()
@commands.is_owner()
async def prepare(ctx: commands.Context):
    """Starts a persistent view."""
    await ctx.send("What's your favourite colour?", view=PersistentView())


@bot.command()
async def mem(ctx):
    with open('C:/Users/kayra/Desktop/python/__pycache__/images/M2L1-T2-1_tlaheo.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


@bot.command()
async def meem(ctx):
    resim= random.choice(os.listdir ("C:/Users/kayra/Desktop/python/__pycache__/images"))
    with open(f'C:/Users/kayra/Desktop/python/__pycache__/images/{resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''dog komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)


def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['link']


@bot.command('fox')
async def fox(ctx):
    '''fox komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)




@bot.command("animals")
async def animals(ctx):
    afx_image_url= get_fox_image_url()
    adg_image_url= get_dog_image_url()
    adk_image_url= get_duck_image_url()
    a=afx_image_url
    b=adg_image_url
    c=adk_image_url
    x=random.randint(1,3)
    if x==1:
        await ctx.send(a)
    elif x==2:
        await ctx.send(b)    
    else:
        await ctx.send(c)
