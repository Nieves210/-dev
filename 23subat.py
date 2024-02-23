import discord
from discord.ext import commands
import random
import asyncio

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


bot.run("MTIwNTU4MTY1OTcyMjg3OTAxOA.GKXmYH.SXjN7-w9GZd_URT71f6LKmUDrsrwmOj9gDicmw")
