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
from PIL import Image

bot_token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()  # 接続に使用するオブジェクト

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
		
	elif message.content == "!おみくじ":
		# Embedを使ったメッセージ送信 と ランダムで要素を選択
		embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",color=0x2ECC69)
		embed.set_thumbnail(url=message.author.avatar_url)
		embed.add_field(name="[運勢] ", value=random.choice(('大吉', '吉', '凶', '大凶')), inline=False)
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
		vc = await message.author.voice.channel.connect()
		vc.play(discord.FFmpegPCMAudio('dancesushi.mp3'))

client.run(bot_token)
