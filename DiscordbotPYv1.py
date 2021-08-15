import discord
import json
from discord.ext import commands
from discord.utils import get

file = open('config.json', 'r')
config = json.load(file)
token = config['token']
prefix = config['prefix']

bot = commands.Bot(command_prefix=prefix)
color = discord.Colour(0xffff00)
footer = '© Trials Recoveries 2021'

@bot.event
async def on_connect():
    print(f'{bot.user} is now online')
    
@bot.command(name='ping')
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send('Pong!')
    
@bot.command(name='info')
@commands.has_permissions(administrator=True)
async def _info(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        title='Trials Recoveries Services',
        color=color,
        description='**Carries (You play with us on your account)**\n**⟶** x1 flawless = $15 USD\n**⟶** x2 flawless = $30 USD\n**⟶** x3 flawless = $45 USD\n\n**Recoveries (We sign into your account)**\n**⟶** x1 flawless = $10 USD\n**⟶** x2 flawless = $20 USD\n**⟶** x3 flawless = $30 USD\n\n**Payment Methods**\n**⟶** Cashapp or Venmo (Preferred)\n**⟶** Paypal\n\nGuaranteed flawless at a 100% rate\n\nOpen a ticket in <#874023341554536548> to make an order')
    embed.set_image(url='https://i.ytimg.com/vi/Gooi0jKJ7GY/maxresdefault.jpg')
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)
    
@bot.command(name='recov')
async def _recov(ctx, user:discord.Member):
    if user == None:
        await ctx.send('Please specify a user!')
        return
    embed = discord.Embed(
        title='Welcome to Trials Recoveries',
        color=color,
        description='This is an automated message to collect information that our recovery team will need to make a recovery on your account.\n\n If you are ready to continue please reply **yes**.')
    embed.set_footer(text=footer)
    await user.send(embed=embed)
    msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    if msg.content == 'yes':
        embed2 = discord.Embed(
            description='Enter your steam account username (check capitalization).',
            color=color
        )
        embed2.set_footer(text=footer)
        await user.send(embed=embed2)
        username = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
        embed3 = discord.Embed(
            description='Enter your steam account password (check capitalization).',
            color=color
        )
        embed3.set_footer(text=footer)
        await user.send(embed=embed3)
        password = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
        accounts_channel = bot.get_channel(876139971487096843)
        embed4 = discord.Embed(
            title='Recovery Account Collected',
            color=color)
        embed4.add_field(name='Username', value=username.content, inline=False)
        embed4.add_field(name='Password', value=password.content, inline=False)
        embed4.add_field(name='Account Owner', value=user, inline=False)
        embed4.set_footer(text=footer)
        await accounts_channel.send(embed=embed4)
        embed5 = discord.Embed(description='Thanks! Our recovery team will now go ahead and perform a recovery on your account.', color=color)
        embed5.set_footer(text=footer)
        embed5.set_image(url='https://i.ytimg.com/vi/Gooi0jKJ7GY/maxresdefault.jpg')
        await user.send(embed=embed5)
        return
    else:
        await user.send('Looks like you didnt say **yes**, if you decide you change your mind and are ready for the process contact Aml#8097 (bot owner)')
        return


bot.run(token)