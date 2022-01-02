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
	
	elif message.content == "!参加":
		dm = await message.author.create_dm()
		CHANNEL_ID = 923672626168234044
		channel = client.get_channel(CHANNEL_ID)
		#await channel.send(f"{message.author.mention} さんがゲームを開始しました")
		await client.get_channel(CHANNEL_ID).send(f"{message.author.mention} さんがゲームを開始しました")
		
		
		await dm.send(f"{message.author.mention}さんゲーム参加ありがとう！俺は野原ひろし。これからゲームの説明をするね\nこれから俺が問題を出して行くから答えがわかったら回答してくれ\n")
		await dm.send(f"あ、解答するときは前に[!]を付けてひらがなは全てカタカナにしてくれよな")
		await dm.send(f"(例:解答が「かき氷機」の場合「!カキ氷機」と送信してください。")
		await dm.send(f"!は半角ね")
		await dm.send(f"ではスタート!第1問！")
		await dm.send(file=discord.File("mondai_001.png"))
	
	elif message.content == "!イヌ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第2問!")
		await dm.send(file=discord.File("mondai_002.png"))
		
	elif message.content == "!スタッフ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第3問!")
		await dm.send(file=discord.File("mondai_003.png"))
		
	elif message.content == "!マツボックリ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第4問!")
		await dm.send(file=discord.File("mondai_004.png"))
		
	elif message.content == "!ミサイル":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第5問!")
		await dm.send(file=discord.File("mondai_005.png"))
		
	elif message.content == "!マリ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第6問!")
		await dm.send(file=discord.File("mondai_006.png"))
		
	elif message.content == "!東京":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第7問!")
		await dm.send(file=discord.File("mondai_007.png"))
		
	elif message.content == "!デンシャ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第8問!")
		await dm.send(file=discord.File("mondai_008.png"))
		
	elif message.content == "!カミ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第9問!")
		await dm.send(file=discord.File("mondai_009.png"))
		
	elif message.content == "!コイン":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第10問!")
		await dm.send(file=discord.File("mondai_010.png"))
		
	elif message.content == "!キョウリュウ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第11問!")
		await dm.send(file=discord.File("mondai_011.png"))
		
	elif message.content == "!タクアン":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第12問!")
		await dm.send(file=discord.File("mondai_012.png"))
		
	elif message.content == "!ラッパ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第13問!")
		await dm.send(file=discord.File("mondai_013.png"))
		
	elif message.content == "!エイ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第14問!")
		await dm.send(file=discord.File("mondai_014.png"))
		
	elif message.content == "!マインクラフト":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第15問!")
		await dm.send(file=discord.File("mondai_015.png"))
		
	elif message.content == "!タンバリン":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第16問!")
		await dm.send(file=discord.File("mondai_016.png"))
		
	elif message.content == "!トキ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第17問!")
		await dm.send(file=discord.File("mondai_017.png"))
		
	elif message.content == "!問題":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第18問!")
		await dm.send(file=discord.File("mondai_018.png"))
		
	elif message.content == "!カッパ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第19問!")
		await dm.send(file=discord.File("mondai_019.png"))
		
	elif message.content == "!題名":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第20問!")
		await dm.send(file=discord.File("mondai_020.png"))
		
	elif message.content == "!パイロット":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第21問!")
		await dm.send(file=discord.File("mondai_021.png"))
		
	elif message.content == "!ノコギリ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第22問!")
		await dm.send(file=discord.File("mondai_022.png"))
		await dm.send(file=discord.File("time.gif"))
		
	elif message.content == "!時間":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第23問!")
		await dm.send(file=discord.File("mondai_023.png"))
		
	elif message.content == "!コエ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第24問!")
		await dm.send(file=discord.File("mondai_024.png"))
		
	elif message.content == "!ツリ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第25問!")
		await dm.send(file=discord.File("mondai_025.png"))
		
	elif message.content == "!タコ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第26問!")
		await dm.send(file=discord.File("mondai_026.png"))
		
	elif message.content == "!コンサート":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第27問!")
		await dm.send(file=discord.File("mondai_027.png"))
		
	elif message.content == "!エイガカン":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第28問!")
		await dm.send(file=discord.File("mondai_028.png"))
		
	elif message.content == "!リンゴ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第29問!")
		await dm.send(file=discord.File("mondai_029.png"))
		
	elif message.content == "!ガビョウ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第30問!")
		await dm.send(file=discord.File("mondai_030.png"))
		
	elif message.content == "!壁":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第31問!")
		await dm.send(file=discord.File("mondai_031.png"))
		
	elif message.content == "!三":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第32問!")
		await dm.send(file=discord.File("mondai_032.png"))
		
	elif message.content == "!教師":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第33問!")
		await dm.send(file=discord.File("mondai_033.png"))
		
	elif message.content == "!モリ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第34問!")
		await dm.send(file=discord.File("mondai_034.png"))
		
	elif message.content == "!カモノハシ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第35問!")
		await dm.send(file=discord.File("mondai_035.png"))
		
	elif message.content == "!ジシャク":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第36問!")
		await dm.send(file=discord.File("mondai_036.png"))
		
	elif message.content == "!フィギュア":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第37問!")
		await dm.send(file=discord.File("mondai_037.png"))
		
	elif message.content == "!ノリ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第38問!")
		await dm.send(file=discord.File("mondai_038.png"))
		
	elif message.content == "!ワシ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第39問!")
		await dm.send(file=discord.File("mondai_039.png"))
		
	elif message.content == "!問イ合ワセ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第40問!")
		await dm.send(file=discord.File("mondai_040.png"))
		
	elif message.content == "!サカナ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第41問!")
		await dm.send(file=discord.File("mondai_041.png"))
		
	elif message.content == "!ダイコン":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第42問!")
		await dm.send(file=discord.File("mondai_042.png"))
		
	elif message.content == "!ヒマラヤ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第43問!")
		await dm.send(file=discord.File("mondai_043.png"))
		
	elif message.content == "!イワ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第44問!")
		await dm.send(file=discord.File("mondai_044.png"))
		
	elif message.content == "!ガス":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第45問!")
		await dm.send(file=discord.File("mondai_045.png"))
		
	elif message.content == "!ノラネコ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第46問!")
		await dm.send(file=discord.File("mondai_046.png"))
		
	elif message.content == "!クジ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第47問!")
		await dm.send(file=discord.File("mondai_047.png"))
		
	elif message.content == "!番人":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第48問!")
		await dm.send(file=discord.File("mondai_048.png"))
		
	elif message.content == "!スクリーン":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第49問!")
		await dm.send(file=discord.File("mondai_049.png"))
		
	elif message.content == "!ゴウトウ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第50問!")
		await dm.send(file=discord.File("mondai_050.png"))
		
	elif message.content == "!キャンプ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第51問!")
		await dm.send(file=discord.File("mondai_051.png"))
		
	elif message.content == "!ウチュウ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第52問!")
		await dm.send(file=discord.File("mondai_052.png"))
		
	elif message.content == "!中国":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第53問!")
		await dm.send(file=discord.File("mondai_053.png"))
		
	elif message.content == "!メンダコ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第54問!")
		await dm.send(file=discord.File("mondai_054.png"))
		
	elif message.content == "!鉄":
		dm = await message.author.create_dm()
		CHANNEL_ID = 923672626168234044
		channel = client.get_channel(CHANNEL_ID)
		await channel.send(f"{message.author.mention} さんが54問目をクリアしました")
		await dm.send(f"正解！次はこれ!第55問!")
		await dm.send(file=discord.File("mondai_055.png"))
		
	elif message.content == "!ノートパソコン":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第56問!")
		await dm.send(file=discord.File("mondai_056.png"))
		
	elif message.content == "!クモ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第57問!")
		await dm.send(file=discord.File("mondai_057.png"))
		
	elif message.content == "!モモ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第58問!")
		await dm.send(file=discord.File("mondai_058.png"))
		
	elif message.content == "!ウマ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第59問!")
		await dm.send(file=discord.File("mondai_059.png"))
		
	elif message.content == "!ジュース":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第60問!")
		CHANNEL_ID = 923672626168234044
		channel = client.get_channel(CHANNEL_ID)
		await channel.send(f"{message.author.mention} さんが60問目をクリアしました")
		await dm.send(file=discord.File("mondai_060.png"))
		
	elif message.content == "!タヌキ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第61問!")
		await dm.send(file=discord.File("mondai_061.png"))
		
	elif message.content == "!オツマミ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第62問!")
		await dm.send(file=discord.File("mondai_062.png"))
		
	elif message.content == "!潜水艦":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第63問!")
		await dm.send(file=discord.File("mondai_063.png"))
		
	elif message.content == "!アカイロ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第64問!")
		await dm.send(file=discord.File("mondai_064.png"))
		
	elif message.content == "!スイソウ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第65問!")
		await dm.send(file=discord.File("mondai_065.png"))
		
	elif message.content == "!イス":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第66問!")
		await dm.send(file=discord.File("mondai_066.png"))
		
	elif message.content == "!イノシシ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第67問!")
		await dm.send(file=discord.File("mondai_067.png"))
		
	elif message.content == "!サツマイモ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第68問!")
		await dm.send(file=discord.File("mondai_068.png"))
		
	elif message.content == "!ウィンター":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第69問!")
		await dm.send(file=discord.File("mondai_069.png"))
		
	elif message.content == "!ツリボリ":
		dm = await message.author.create_dm()
		CHANNEL_ID = 923672626168234044
		channel = client.get_channel(CHANNEL_ID)
		await channel.send(f"{message.author.mention} さんが70問目をクリアしました")
		await dm.send(f"正解！次はこれ!第70問!")
		await dm.send(file=discord.File("mondai_070.png"))
		
	elif message.content == "!工場":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第71問!")
		await dm.send(file=discord.File("mondai_071.png"))
		
	elif message.content == "!カイダン":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第72問!")
		await dm.send(file=discord.File("mondai_072.png"))
		
	elif message.content == "!ウグイス":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第73問!")
		await dm.send(file=discord.File("mondai_073.png"))
		
	elif message.content == "!ライター":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第74問!")
		await dm.send(file=discord.File("mondai_074.png"))
		
	elif message.content == "!ストロー":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第75問!")
		await dm.send(file=discord.File("mondai_075.png"))
		
	elif message.content == "!ヌカヅケ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第76問!")
		await dm.send(file=discord.File("mondai_076.png"))
		
	elif message.content == "!木綿":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第77問!")
		await dm.send(file=discord.File("mondai_077.png"))
		
	elif message.content == "!キツツキ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第78問!")
		await dm.send(file=discord.File("mondai_078.png"))
		
	elif message.content == "!スイッチ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第79問!")
		await dm.send(file=discord.File("mondai_079.png"))
		
	elif message.content == "!ダシマキタマゴ":
		dm = await message.author.create_dm()
		CHANNEL_ID = 923672626168234044
		channel = client.get_channel(CHANNEL_ID)
		await channel.send(f"{message.author.mention} さんが80問目をクリアしました")
		await dm.send(f"正解！次はこれ!第80問!")
		await dm.send(file=discord.File("mondai_080.png"))
		
	elif message.content == "!目":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第81問!")
		await dm.send(file=discord.File("mondai_081.png"))
		
	elif message.content == "!シソ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第82問!")
		await dm.send(file=discord.File("mondai_082.png"))
		
	elif message.content == "!バラ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第83問!")
		await dm.send(file=discord.File("mondai_083.png"))
		
	elif message.content == "!テブクロ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第84問!")
		await dm.send(file=discord.File("mondai_084.png"))
		
	elif message.content == "!土星":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第85問!")
		await dm.send(file=discord.File("mondai_085.png"))
		
	elif message.content == "!上下":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第86問!")
		await dm.send(file=discord.File("mondai_086.png"))
		
	elif message.content == "!チョコレート":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第87問!")
		await dm.send(file=discord.File("mondai_087.png"))
		
	elif message.content == "!カラアゲ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第88問!")
		await dm.send(file=discord.File("mondai_088.png"))
		
	elif message.content == "!ドレス":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第89問!")
		await dm.send(file=discord.File("mondai_089.png"))
		
	elif message.content == "!ラクダ":
		dm = await message.author.create_dm()
		CHANNEL_ID = 923672626168234044
		channel = client.get_channel(CHANNEL_ID)
		await channel.send(f"{message.author.mention} さんが90問目をクリアしました")
		await dm.send(f"正解！次はこれ!第90問!")
		await dm.send(file=discord.File("mondai_090.png"))
		
	elif message.content == "!ケチャップ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第91問!")
		await dm.send(file=discord.File("mondai_091.png"))
		
	elif message.content == "!順":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第92問!")
		await dm.send(file=discord.File("mondai_092.png"))
		
	elif message.content == "!タカラ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第93問!")
		await dm.send(file=discord.File("mondai_093.png"))
		
	elif message.content == "!番号札":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第94問!")
		await dm.send(file=discord.File("mondai_094.png"))
		
	elif message.content == "!幸運":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第95問!")
		await dm.send(file=discord.File("mondai_095.png"))
		
	elif message.content == "!ニラ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第96問!")
		await dm.send(file=discord.File("mondai_096.png"))
		
	elif message.content == "!カイゾク":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第97問!")
		await dm.send(file=discord.File("mondai_097.png"))
		
	elif message.content == "!ヨル":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第98問!")
		await dm.send(file=discord.File("mondai_098.png"))
		
	elif message.content == "!ギリシャ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第99問!")
		await dm.send(file=discord.File("mondai_099.png"))
		
	elif message.content == "!メス":
		dm = await message.author.create_dm()
		CHANNEL_ID = 923672626168234044
		channel = client.get_channel(CHANNEL_ID)
		await channel.send(f"{message.author.mention} さんが100問目をクリアしました")
		await dm.send(f"正解！次はこれ!第100問!")
		await dm.send(file=discord.File("mondai_100.png"))
		
	elif message.content == "!オウカン":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第101問!")
		await dm.send(file=discord.File("mondai_101.png"))
		
	elif message.content == "!バズーカ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第102問!")
		await dm.send(file=discord.File("mondai_102.png"))
		
	elif message.content == "!マッチ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第103問!")
		await dm.send(file=discord.File("mondai_103.png"))
		
	elif message.content == "!ワタガシ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第104問!")
		await dm.send(file=discord.File("mondai_104.png"))
		
	elif message.content == "!トランク":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第105問!")
		await dm.send(file=discord.File("mondai_105.png"))
		
	elif message.content == "!カイガラ":
		dm = await message.author.create_dm()
		await dm.send(f"正解！次はこれ!第106問!")
		await dm.send(file=discord.File("mondai_106.png"))
		
	elif message.content == "!マンモス":
		dm = await message.author.create_dm()
		CHANNEL_ID = 923672626168234044
		channel = client.get_channel(CHANNEL_ID)
		await channel.send(f"{message.author.mention} さんが107問目をクリアしました")
		await dm.send(f"正解！次はこれ!第107問!")
		await dm.send(file=discord.File("mondai_107.png"))
		
	elif message.content == "!ルーレット":
		dm = await message.author.create_dm()
		await dm.send(f"正解！これが最後の問題だ!第108問!")
		await dm.send(f"最後の問題は!![解答]を入力してくれ!")
		await dm.send(f"例:解答がかき氷の場合　→　!!カキ氷")
		await dm.send(file=discord.File("mondai_108.png"))
		
	elif message.content == "!!寅":
		dm = await message.author.create_dm()
		CHANNEL_ID = 923672626168234044
		channel = client.get_channel(CHANNEL_ID)
		await channel.send(f"{message.author.mention} さんが108問目をクリアしました!全クリ！")
		await dm.send(f"謎解き全問正解！全クリおめでとう！！！")
		
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
	
	elif message.content.startswith("!飲む人"):
		if message.author.voice is None:
			await message.channel.send("ボイスチャンネルに接続してね")
			return
		
		bun = message.content
		team_num = int(bun[bun.find(" ")+1:])
		
		if team_num > len(member):
			await message.channel.send(f'チャンネル参加人数より飲む人のほうが多いよおお。')
			return
		
		member = [i.name for i in message.author.voice.channel.members]
		embed = discord.Embed(title="チーム", description=f"飲む人！",color=0xFF0000)
		random.shuffle(member)
		for i in range(team_num):
			embed.add_field(name=f"飲む人**{i}**",value=member[i],inline=False)
		await message.channel.send(embed=embed)	
	
	elif message.content.startswith("!team"):
		if message.author.voice is None:
			await message.channel.send("ボイスチャンネルに接続してね")
			return

		bun = message.content
		#intents=discord.Intents.all() 
		team_num = int(bun[bun.find(" ")+1:])
		member = [i.name for i in message.author.voice.channel.members]
		embed = discord.Embed(title="チーム", description=f"{team_num}つのチームに編成！",color=0xFF0000)
		
		print(team_num,len(member))
		print(member)
		print(message.author.voice.channel.members)
		
		if team_num > len(member):
			await message.channel.send(f'チャンネル参加人数よりチーム数のほうが多い為チーム分けできませんでした。')
			return
		
		random.shuffle(member)
		if len(member)%team_num != 0:
			ans = team_num - (len(member)%team_num)
			for i in range(ans):
				member.append(" ")
		team_count = int(len(member)/team_num)
		for i in range(team_num):
			embed.add_field(name=f"チーム**{i}**",value=member[team_count*i:team_count*i+team_count],inline=False)
		await message.channel.send(embed=embed)		
		
	elif message.content == "('o')ｷｬｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww":
		await message.channel.send(f"うるせえぞタピオカ")
		
	elif message.content == "!やるじゃん":
		await message.channel.send(f"ありがとう")
		
	elif message.content == "!えっち":
		await message.channel.send(f'きゃー！{message.author.mention}さんのえっち！！', file=discord.File("4ba65a1c.jpg"))
		
	elif message.content == "!ドラえもん":
		await message.channel.send(file=discord.File("doraemon.gif"))
		
	elif message.content == "!ヒロシ":
		await message.channel.send(file=discord.File("hiroshi.gif"))
		
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
		
	elif message.content == "!いい加減寝ろ":
		await message.channel.send(f"はよ寝ろやゴミ糞カメムシが")
		
	elif message.content == "たまよ！":
		await message.channel.send(f"パンティーテックス！")
		
	elif message.content == "!Oさんかっこいい":
		await message.channel.send(f"https://twitter.com/taric_OTP/status/1476856907000614915")
		
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
		#np.random.seed((id**2)%((2**32)-1))
		sigoto = np.random.randint(0,6)
		#np.random.seed((id**3)%((2**32)-1))
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
		
	elif message.content == "!まいむまいむ":
		if message.author.voice is None:
			await message.channel.send("ボイスチャンネルに接続してね")
			return
		await message.author.voice.channel.connect()
		message.guild.voice_client.play(discord.FFmpegPCMAudio("mimemime.mp3"))
		await message.channel.send("終わったら「!終わった」ってしてね")
		
	elif message.content == "!たまよ":
		if message.author.voice is None:
			await message.channel.send("ボイスチャンネルに接続してね")
			return
		await message.author.voice.channel.connect()
		message.guild.voice_client.play(discord.FFmpegPCMAudio("tamayo.mp3"))
		await message.channel.send("終わったら「!終わった」ってしてね")
		
	elif message.content == "!らますむ":
		if message.author.voice is None:
			await message.channel.send("ボイスチャンネルに接続してね")
			return
		await message.author.voice.channel.connect()
		message.guild.voice_client.play(discord.FFmpegPCMAudio("ramasumu.mp3"))
		await message.channel.send("終わったら「!終わった」ってしてね")
		
	elif message.content == "!終わった":
		await message.channel.send("じょあの")
		await message.guild.voice_client.disconnect()
		
client.run(bot_token)
