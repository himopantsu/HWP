import discord
import glob
from discord.ext import commands,tasks
import gspread
import random  # おみくじで使用
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import pandas as pd
import datetime
import os
import urllib.request, urllib.error
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from datetime import timedelta
import io
import time
from PIL import Image

bot_token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()  # 接続に使用するオブジェクト
omikuji_array = np.array(["大凶","大凶","凶","凶","末吉","末吉","小吉","小吉","小吉","吉","吉","吉","中吉","中吉","大吉","大吉"])
star_array = np.array(["☆☆☆☆☆","★☆☆☆☆","★★☆☆☆","★★★☆☆","★★★★☆","★★★★★"])

@client.event
async def on_ready():
	"""起動時に通知してくれる処理"""
	print('ログインしました')
	print(client.user.name)  # ボットの名前
	print(client.user.id)  # ボットのID
	print(discord.__version__)  # discord.pyのバージョン
	print('------')
	
@client.event
async def on_message(message):
	"""メッセージを処理"""
	if message.author.bot:  # ボットのメッセージをハネる
		return
	
	elif message.content.startswith("/dice"):
		bun = message.content
		syou = int(bun[bun.find(" ")+1:bun.rfind(" ")])
		dai = int(bun[bun.rfind(" ")+1:])
		if syou > dai:
			await message.channel.send(f'{syou}より{dai}のほうが小さいよ')
			await message.channel.send(f'/dice 小さい数字 大きい数字 の順番で指定してね')
			return
		elif syou == dai:
			await message.channel.send(f'{syou}')
			return
		else:
			await message.channel.send(f'ぽん！**{np.random.randint(syou,dai)}**')
			return
		
	elif message.content == "('o')ｷｬｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww":
		await message.channel.send(f"うるせえぞタピオカ")
		
	elif message.content == "!やるじゃん":
		await message.channel.send(f"ありがとう")
		
	elif message.content == "!えっち":
		await message.channel.send(f'きゃー！{message.author.mention}さんのえっち！！', file=discord.File("4ba65a1c.jpg"))
		
	elif message.content == "!ハンバーグ":
		await message.channel.send(f"ハンバアアアアアアアアアアアアアアアアアアアアアアアアアアアグ！！！！！！")
	
	elif message.content == "!やってないじゃん":
		await message.channel.send(f"ごめんなさい")
		
	elif message.content == "!あるよ":
		await message.channel.send(f'あるよ', file=discord.File("aruyo.jpg"))
		
	elif message.content == "!ゆきやこんこ":
		await message.channel.send(f"⛄雪や⛄\n\n❄❅❆❄❅❆❄❅❆❄\n▉▉▉ ◥◣　　 ▉▉▉ \n　　▉ 　　◢◤ 　　▉ \n▉▉▉ ◢▉◤　 ▉▉▉ \n❄❅❆❄❅❆❄❅❆❄\n\n🚽ケツから🚽\n\n💩💩💩💩💩💩💩💩\n　▉\n▉▉▉▉◥◣　　▉▉▉\n▉　◢◤　　◢◤　　▉\n　◢◤　◢▉◤　▉▉▉\n💩💩💩💩💩💩💩💩")
		
	elif message.content == "juruli":
		await message.channel.send(f"そのキャラはキャラデリしました")
		
	elif message.content == "たまよ！":
		await message.channel.send(f"パンティーテックス！")
		
	elif message.content == "!ごみくじ":
		# Embedを使ったメッセージ送信 と ランダムで要素を選択
		embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",color=0x2ECC69)
		embed.set_thumbnail(url=message.author.avatar_url)
		embed.add_field(name="[運勢] ", value=random.choice(('大吉', '中吉', '吉', '小吉', '末吉', '凶', '大凶')), inline=False)
		await message.channel.send(embed=embed)
		
	elif message.content == "!おみくじ":
		#today = str(datetime.date.today().year)+str(datetime.date.today().month)+str(datetime.date.today().day)
		#id = int(message.author.id + int(today))
		#np.random.seed(id%((2**32)-1))
		kinnun = np.random.randint(0,6) 
		np.random.seed((id**2)%((2**32)-1))
		sigoto = np.random.randint(0,6)
		np.random.seed((id**3)%((2**32)-1))
		rennai = np.random.randint(0,6)
		goukei = kinnun + sigoto + rennai
		
		embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",color=0x00FF00)
		embed.set_thumbnail(url=message.author.avatar_url)
		embed.add_field(name="総合運",value=omikuji_array[goukei],inline=False)
		embed.add_field(name="恋愛運",value=star_array[rennai],inline=False)
		embed.add_field(name="金運",value=star_array[kinnun],inline=False)
		embed.add_field(name="仕事運",value=star_array[sigoto],inline=False)
		await message.channel.send(embed=embed)	
		
	elif message.content == "!ダイス":
		embed = discord.Embed(title="ダイス", description=f"{message.author.mention}さんの結果",color=0x2ECC69)
		embed.set_thumbnail(url=message.author.avatar_url)
		embed.add_field(name="[結果] ", value=random.randint(0,100), inline=False)
		await message.channel.send(embed=embed)
		
	elif message.content == "!ダイレクトメッセージ":
		# ダイレクトメッセージ送信
		dm = await message.author.create_dm()
		await dm.send(f"{message.author.mention}さんにダイレクトメッセージ")
		
	elif message.content == "!ダンス寿司":
		if message.author.voice is None:
			await message.channel.send("ボイスチャンネルに接続してね")
			return
		await message.author.voice.channel.connect()
		message.guild.voice_client.play(discord.FFmpegPCMAudio("dancesushi.mp3"))
		await message.channel.send("終わったら「!終わった」ってしてね")
		
	elif message.content == "!ギャル":
		if message.author.voice is None:
			await message.channel.send("ボイスチャンネルに接続してね")
			return
		await message.author.voice.channel.connect()
		message.guild.voice_client.play(discord.FFmpegPCMAudio("gyaru.mp3"))
		await message.channel.send("終わったら「!終わった」ってしてね")
		
	elif message.content == "!たまむし":
		if message.author.voice is None:
			await message.channel.send("ボイスチャンネルに接続してね")
			return
		await message.author.voice.channel.connect()
		message.guild.voice_client.play(discord.FFmpegPCMAudio("tamamushi.mp3"))
		await message.channel.send("終わったら「!終わった」ってしてね")
		
	elif message.content == "!おっぱい":
		if message.author.voice is None:
			await message.channel.send("ボイスチャンネルに接続してね")
			return
		await message.author.voice.channel.connect()
		message.guild.voice_client.play(discord.FFmpegPCMAudio("titimoge.mp3"))
		await message.channel.send("終わったら「!終わった」ってしてね")
		
	elif message.content == "!はやね":
		if message.author.voice is None:
			await message.channel.send("ボイスチャンネルに接続してね")
			return
		await message.author.voice.channel.connect()
		message.guild.voice_client.play(discord.FFmpegPCMAudio("hayane.mp3"))
		await message.channel.send("終わったら「!終わった」ってしてね")
		
	elif message.content == "!よびこみ":
		if message.author.voice is None:
			await message.channel.send("ボイスチャンネルに接続してね")
			return
		await message.author.voice.channel.connect()
		message.guild.voice_client.play(discord.FFmpegPCMAudio("yobikomi.mp3"))
		await message.channel.send("終わったら「!終わった」ってしてね")
		
	elif message.content == "!終わった":
		await message.channel.send("じょあの")
		await message.guild.voice_client.disconnect()
		
client.run(bot_token)
