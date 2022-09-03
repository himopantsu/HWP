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
color = np.array(["藍色 (あいいろ)","藍鼠 (あいねず)","青 (あお)","青竹色 (あおたけいろ)","青丹 (あおに)","青鈍 (あおにび)","青緑 (あおみどり)","青紫 (あおむらさき)",
		  "赤 (あか)","赤朽葉 (あかくちば)","赤香 (あかこう)","赤錆色 (あかさびいろ)","赤橙 (あかだいだい)","赤茶 (あかちゃ)","茜色 (あかねいろ)","赤紫 (あかむらさき)",
		  "灰汁色 (あくいろ)","浅葱色 (あさぎいろ)","浅緋 (あさひ)","浅緑 (あさみどり)","小豆色 (あずきいろ)","油色 (あぶらいろ)","亜麻色 (あまいろ)","飴色 (あめいろ)",
		  "菖蒲色 (あやめいろ)","洗柿 (あらいがき)","洗朱 (あらいしゅ)","暗紅色 (あんこうしょく)","杏色 (あんずいろ)","暗緑色 (あんりょくしょく)","苺色 (いちごいろ)",
		  "一斤染 (いっこんぞめ)","今様色 (いまよういろ)","鶯色 (うぐいすいろ)","鶯茶 (うぐいすちゃ)","鬱金色 (うこんいろ)","薄色 (うすいろ)","薄紅 (うすくれない)",
		  "薄香 (うすこう)","薄墨色 (うすずみいろ)","薄茶 (うすちゃ)","薄緑 (うすみどり)","空五倍子色 (うつぶしいろ)","卯の花色 (うのはないろ)","梅鼠 (うめねず)",
		  "裏葉柳 (うらばやなぎ)","潤朱 (うるみしゅ)","江戸茶 (えどちゃ)","江戸紫 (えどむらさき)","海老色 (えびいろ)","葡萄染 (えびぞめ)","海老茶 (えびちゃ)",
		  "臙脂 (えんじ)","鉛丹色 (えんたんいろ)","鉛白 (えんぱく)","老竹色 (おいたけいろ)","楝色 (おうちいろ)","黄土色 (おうどいろ)","黄丹 (おうに)","柿色 (かきいろ)",
		  "柿渋色 (かきしぶいろ)","杜若色 (かきつばたいろ)","勝色 (かちいろ)","褐色 (かっしょく)","樺色 (かばいろ)","樺茶 (かばちゃ)","瓶覗き (かめのぞき)",
		  "韓紅色 (からくれないいろ)","芥子色 (からしいろ)","唐茶 (からちゃ)","刈安色 (かりやすいろ)","枯色 (かれいろ)","土器色 (かわらけいろ)","萱草色 (かんぞういろ)",
		  "黄赤 (きあか)","黄色 (きいろ)","桔梗色 (ききょういろ)","麹塵 (きくじん)","黄茶 (きちゃ)","狐色 (きつねいろ)","生成色 (きなりいろ)","黄蘗色 (きはだいろ)",
		  "黄緑 (きみどり)","伽羅色 (きゃらいろ)","京紫 (きょうむらさき)","金赤 (きんあか)","金茶 (きんちゃ)","銀鼠 (ぎんねず)","草色 (くさいろ)",
		  "梔子色 (くちなしいろ)","朽葉色 (くちばいろ)","栗色 (くりいろ)","涅色 (くりいろ)","栗梅 (くりうめ)","胡桃色 (くるみいろ)","黒 (くろ)","黒茶 (くろちゃ)",
		  "桑染 (くわぞめ)","桑茶 (くわちゃ)","群青色 (ぐんじょういろ)","消炭色 (けしずみいろ)","滅紫 (けしむらさき)","憲房色 (けんぽういろ)","濃藍 (こいあい)",
		  "香色 (こういろ)","柑子色 (こうじいろ)","紅梅色 (こうばいいろ)","黄櫨染 (こうろぜん)","焦香 (こがれこう)","濃色 (こきいろ)","苔色 (こけいろ)",
		  "焦茶 (こげちゃ)","古代紫 (こだいむらさき)","琥珀色 (こはくいろ)","媚茶 (こびちゃ)","胡粉色 (ごふんいろ)","小麦色 (こむぎいろ)","紺藍 (こんあい)",
		  "紺色 (こんいろ)","紺青 (こんじょう)","桜色 (さくらいろ)","錆浅葱 (さびあさぎ)","錆色 (さびいろ)","錆納戸 (さびなんど)","珊瑚色 (さんごいろ)",
		  "雌黄 (しおう)","紫苑色 (しおんいろ)","芝翫茶 (しかんちゃ)","紫紺 (しこん)","漆黒 (しっこく)","東雲色 (しののめいろ)","渋紙色 (しぶがみいろ)",
		  "赤銅色 (しゃくどういろ)","朱色 (しゅいろ)","猩々緋 (しょうじょうひ)","菖蒲色 (しょうぶいろ)","白茶 (しらちゃ)","白 (しろ)","真紅 (しんく)",
		  "新橋色 (しんばしいろ)","蘇芳 (すおう)","煤竹色 (すすたけいろ)","砂色 (すないろ)","墨色 (すみいろ)","菫色 (すみれいろ)","青磁色 (せいじいろ)",
		  "仙斎茶 (せんざいちゃ)","象牙色 (ぞうげいろ)","赭 (そお)","空色 (そらいろ)","退紅色 (たいこうしょく)","代赭色 (たいしゃいろ)","橙色 (だいだいいろ)",
		  "煙草色 (たばこいろ)","卵色 (たまごいろ)","団十郎茶 (だんじゅうろうちゃ)","蒲公英色 (たんぽぽいろ)","千草色 (ちぐさいろ)","千歳緑 (ちとせみどり)",
		  "茶色 (ちゃいろ)","茶鼠 (ちゃねず)","中黄 (ちゅうき)","丁字色 (ちょうじいろ)","丁字茶 (ちょうじちゃ)","土色 (つちいろ)","躑躅色 (つつじいろ)",
		  "露草色 (つゆくさいろ)","鉄色 (てついろ)","鉄黒 (てつぐろ)","鉄紺 (てつこん)","鉄納戸 (てつなんど)","鴇色 (ときいろ)","常磐色 (ときわいろ)",
		  "木賊色 (とくさいろ)","砥粉色 (とのこいろ)","鳶色 (とびいろ)","鳥の子色 (とりのこいろ)","苗色 (なえいろ)","茄子紺 (なすこん)","撫子色 (なでしこいろ)",
		  "菜の花色 (なのはないろ)","生壁色 (なまかべいろ)","鉛色 (なまりいろ)","納戸色 (なんどいろ)","納戸茶 (なんどちゃ)","丹色 (にいろ)","似紫 (にせむらさき)",
		  "肉桂色 (にっけいいろ)","鈍色 (にびいろ)","乳白色 (にゅうはくしょく)","人参色 (にんじんいろ)","濡羽色 (ぬればいろ)","根岸色 (ねぎしいろ)","鼠色 (ねずみいろ)",
		  "練色 (ねりいろ)","濃紺 (のうこん)","灰色 (はいいろ)","梅幸茶 (ばいこうちゃ)","灰桜 (はいざくら)","灰茶 (はいちゃ)","灰緑 (はいみどり)","黄櫨色 (はじいろ)",
		  "肌色 (はだいろ)","鳩羽色 (はとばいろ)","縹色 (はなだいろ)","薔薇色 (ばらいろ)","緋色 (ひいろ)","秘色 (ひそく)","向日葵色 (ひまわりいろ)","白群 (びゃくぐん)",
		  "白緑 (びゃくろく)","鶸色 (ひわいろ)","檜皮色 (ひわだいろ)","鶸茶 (ひわちゃ)","深川鼠 (ふかがわねず)","深緋 (ふかひ)","深緑 (ふかみどり)","藤色 (ふじいろ)",
		  "藤納戸 (ふじなんど)","藤紫 (ふじむらさき)","二藍 (ふたあい)","紅赤 (べにあか)","紅色 (べにいろ)","紅海老茶 (べにえびちゃ)","紅樺色 (べにかばいろ)",
		  "紅緋 (べにひ)","弁柄色 (べんがらいろ)","牡丹色 (ぼたんいろ)","真赭 (まそお)","抹茶色 (まっちゃいろ)","松葉色 (まつばいろ)","蜜柑色 (みかんいろ)",
		  "水浅葱 (みずあさぎ)","水色 (みずいろ)","緑 (みどり)","海松色 (みるいろ)","紫 (むらさき)","萌黄 (もえぎ)","萌葱色 (もえぎいろ)","桃色 (ももいろ)",
		  "柳色 (やなぎいろ)","山鳩色 (やまばといろ)","山吹色 (やまぶきいろ)","雄黄 (ゆうおう)","駱駝色 (らくだいろ)","離寛茶 (りかんちゃ)","利休茶 (りきゅうちゃ)",
		  "利休鼠 (りきゅうねず)","竜胆色 (りんどういろ)","瑠璃色 (るりいろ)","瑠璃紺 (るりこん)","煉瓦色 (れんがいろ)","緑青色 (ろくしょういろ)","路考茶 (ろこうちゃ)",
		  "若草色 (わかくさいろ)","若竹色 (わかたけいろ)","若苗色 (わかなえいろ)","若葉色 (わかばいろ)","若緑 (わかみどり)","山葵色 (わさびいろ)",
		  "勿忘草色 (わすれなぐさいろ)","アイアンブルー (iron blue)","アイスグリーン (ice green)","アイビーグリーン (ivy green)","アイボリー (ivory)",
		  "アイボリーブラック (ivory black)","アガット (agate)","アクアマリン (aquamarine)","アザーブルー (azure blue)","アッシュグレー (ash grey)",
		  "アップルグリーン (apple green)","アプリコット (apricot)","アメジスト (amethyst)","アンバー (amber)","イエロー (yellow)","イエローオーカー (yellow ocher)",
		  "インディアンレッド (indian red)","インディゴ (indigo)","ウィスタリア (wistaria)","ウィローグリーン (willow green)",
		  "ウルトラマリンブルー (ultramarine blue)","エクルベージュ (ecru beige)","エバーグリーン (ever green)","エボニー (ebony)",
		  "エメラルドグリーン (emerald green)","エルムグリーン (elm green)","オーキッド (orchid)","オールドローズ (old rose)","オイスターホワイト (oyster white)",
		  "オパールグリーン (opal green)","オリーブ (olive)","オリーブグリーン (olive green)","オリーブドラブ (olive drab)","オリエンタルブルー (oriental blue)",
		  "オレンジ (orange)","カーキー (khaki)","カージナルレッド (cardinal red)","ガーネット (garnet)","カーマイン (carmine)","カドミウムイエロー (cadmium yellow)",
		  "カナリーイエロー (canary yellow)","ガンメタルグレー (gunmetal grey)","キャメル (camel)","キャラメル (caramel)","キャロットオレンジ (carrot orange)",
		  "グラスグリーン (grass green)","クリームイエロー (cream yellow)","グリーン (green)","クリムソン (crimson)","グレー (grey)","クロッカス (crocus)",
		  "クロムイエロー (chrome yellow)","クロムオレンジ (chrome orange)","クロムグリーン (chrome green)","コーヒーブラウン (coffee brown)",
		  "コーラルピンク (coral pink)","コーラルレッド (coral red)","ゴールデンイエロー (golden yellow)","ココアブラウン (cocoa brown)",
		  "ココナッツブラウン (coconut brown)","コチニールレッド (cochineal red)","コバルトグリーン (cobalt green)","コバルトブルー (cobalt blue)",
		  "コルク (cork)","サーモンピンク (salmon pink)","サックスブルー (saxe blue)","サファイアブルー (sapphire blue)","サフランイエロー (saffron yellow)",
		  "サルビアブルー (salvia blue)","サルファーイエロー (sulphur yellow)","サンド (sand)","サンフラワー (sunflower)","シーグリーン (sea green)",
		  "シアン (cyan)","ジェードグリーン (jade green)","ジェイブルー (jay blue)","シェルピンク (shell pink)","シグナルレッド (signal red)",
		  "シクラメンピンク (cyclamen pink)","シナモン (sinnamon)","ジャスパーグリーン (jasper green)","シャモア (chamois)",
		  "シャルトルーズイエロー (chartreuse yellow)","シャルトルーズグリーン (chartreuse green)","シャンパン (champagne)","シュリンプピンク (shrimp pink)",
		  "ジョンブリアン (jaune brillant)","シルバーグレー (silver grey)","スカーレット (scarlet)","スカイグレー (sky grey)","スカイブルー (sky blue)",
		  "スチールグレー (steel grey)","ストローイエロー (straw yellow)","ストロベリー (strawberry)","スノーホワイト (snow white)",
		  "スプリンググリーン (spring green)","スプルース (spruce)","スマルト (smalt)","スレートグレー (slate grey)","セージグリーン (sage green)",
		  "ゼニスブルー (zenith blue)","セピア (sepia)","セラドン (celadon)","セルリアンブルー (cerulean blue)","セレストブルー (celeste blue)",
		  "ターコイズブルー (turquoise blue)","ダックブルー (duck blue)","ダブグレー (dove grey)","タン (tan)","タンジェリンオレンジ (tangerine orange)",
		  "チェスナットブラウン (chestnut brown)","チェリー (cherry)","チェリーピンク (cherry pink)","チャイニーズレッド (chinese red)",
		  "チャコールグレー (charcoal grey)","チョコレート (chocholate)","チリアンパープル (tyrian purple)","テラコッタ (terracotta)","トープ (taupe)",
		  "ドーンピンク (dawn pink)","トパーズ (topaz)","トマトレッド (tomato red)","ナイルブルー (nile blue)","ネープルスイエロー (naples yellow)",
		  "ネールピンク (nail pink)","ネイビーブルー (navy blue)","バーガンディー (burgundy)","パーチメント (parchment)","パープル (purple)",
		  "バーミリオン (vermilion)","パールグレー (pearl grey)","パールホワイト (pearl white)","バーントアンバー (burnt umber)","バーントオレンジ (burnt orange)",
		  "バーントシェンナ (burnt sienna)","バイオレット (violet)","ハニー (honey)","バフ (buff)","パロットグリーン (parrot green)","パンジー (pansy)",
		  "ハンターグリーン (hunter green)","バンダイクブラウン (van dyck brown)","バンブー (bamboo)","パンプキン (pumpkin)","ピーグリーン (pea green)",
		  "ピーコックグリーン (peacock green)","ピーコックブルー (peacock blue)","ピーチ (peach)","ピアニー (peony)","ビスケット (biscuit)",
		  "ピスタチオグリーン (pistachio green)","ヒヤシンス (hyacinth)","ビリジアン (viridian)","ビリヤードグリーン (billiard green)","ピンク (pink)",
		  "ブーゲンビリア (bougainvillaea)","ファイアーレッド (fire red)","フォーン (fawn)","フォグブルー (fog blue)","フォゲットミーノット (forget me not)",
		  "フォレストグリーン (forest green)","フクシアパープル (fuchsia purple)","フクシアピンク (fuchsia pink)","ブラウン (brown)","ブラック (black)",
		  "フラミンゴ (flamingo)","ブリックレッド (brick red)","ブルー (blue)","プルシャンブルー (prussian blue)","フレッシュ (flesh)","ブロンズ (bronze)",
		  "ブロンド (blond)","ベージュ (beige)","ヘーゼルブラウン (hazel brown)","ベゴニア (begonia)","ベビーピンク (baby pink)","ベビーブルー (baby blue)",
		  "ヘリオトロープ (heliotrope)","ベルディグリ (verdigris)","ヘンナ (henna)","ボトルグリーン (bottle green)","ポピーレッド (poppy red)",
		  "ホリゾンブルー (horizon blue)","ボルドー (bordeaux)","ホワイト (white)","マウスグレー (mouse grey)","マスタード (mustard)","マゼンタ (magenta)",
		  "マホガニー (mahogany)","マラカイトグリーン (malachite green)","マリーゴールド (marigold)","マリンブルー (marine blue)","マルーン (maroon)",
		  "マルベリー (mulberry)","マンダリンオレンジ (mandarin orange)","ミッドナイトブルー (midnight blue)","ミルキーホワイト (milky white)",
		  "ミントグリーン (mint green)","メイズ (maize)","モーブ (mauve)","モスグリーン (moss green)","モスグレイ (moss grey)","ライムイエロー (lime yellow)",
		  "ライムグリーン (lime green)","ライラック (lilac)","ラズベリー (raspberry)","ラセットブラウン (russet brown)","ラピスラズリ (lapis lazuli)",
		  "ラベンダー (lavender)","ランプブラック (lamp black)","リーフグリーン (leaf green)","ルビーレッド (ruby red)","レグホーン (leghorn)","レッド (red)",
		  "レモンイエロー (lemon yellow)","ローアンバー (raw umber)","ローシェンナ (raw sienna)","ローズ (rose)","ローズグレイ (rose grey)",
		  "ローズピンク (rose-pink)","ローズマダー (rose madder)","ローズレッド (rose red)","ロイヤルパープル (royal purple)","ロイヤルブルー (royal blue)",
		  "ワインレッド (wine red)","ヴィオレ (violet)","ヴェール (vert)","オランジュ (orange)","グリ (gris)","ジョーヌ (jaune)","ノワール (noir)",
		  "ブラン (blanc)","ブラン (brun)","ブルー (bleu)","ルージュ (rouge)","ローズ (rose)","ローズ ソーモン (rose saumon)","ローズ テ (rose the)","松崎しげる色(Shigeru Matsuzaki)"])


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
	
	elif message.content.startswith("!飲む人"):
		if message.author.voice is None:
			await message.channel.send("ボイスチャンネルに接続してね")
			return
		
		bun = message.content
		team_num = int(bun[bun.find(" ")+1:])
		member = [i.name for i in message.author.voice.channel.members]
		
		if team_num > len(member):
			await message.channel.send(f'チャンネル参加人数より飲む人のほうが多いよおお。')
			return
		
		embed = discord.Embed(title="飲む人", description=f"飲む人！",color=0xFF0000)
		random.shuffle(member)
		for i in range(team_num):
			embed.add_field(name=f"飲む人**{i+1}**",value=member[i],inline=False)
		await message.channel.send(embed=embed)	
	
	elif message.content.startswith("!team"):
		if message.author.voice is None:
			await message.channel.send("ボイスチャンネルに接続してね")
			return

		bun = message.content
		#intents=discord.Intents.all() 
		team_num = int(bun[bun.find(" ")+1:])
		member = [i.name for i in state.channel.members]
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
		
	elif message.content == "!らますむ":
		await message.channel.send(f"削除しました")
		
	elif message.content == "!Oさんかっこいい":
		await message.channel.send(f"https://twitter.com/taric_OTP/status/1476856907000614915")
		
	elif message.content == "!まあくん":
		await message.channel.send(file=discord.File("maakun.png"))
		
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
		color_num = np.random.randint(0,len(color))
		embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",color=0x00FF00)
		embed.set_thumbnail(url=message.author.avatar_url)
		embed.add_field(name="総合運",value=omikuji_array[goukei],inline=False)
		embed.add_field(name="恋愛運",value=star_array[rennai],inline=False)
		embed.add_field(name="金運",value=star_array[kinnun],inline=False)
		embed.add_field(name="仕事運",value=star_array[sigoto],inline=False)
		embed.add_field(name="ラッキーカラー",value=color[color_num],inline=False)
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
		
	elif message.content == "!らますむXXX":
		if message.author.voice is None:
			await message.channel.send("ボイスチャンネルに接続してね")
			return
		await message.author.voice.channel.connect()
		message.guild.voice_client.play(discord.FFmpegPCMAudio("ramasumu.mp3"))
		await message.channel.send("終わったら「!終わった」ってしてね")
		
	elif message.content == "!ねむる":
		if message.author.voice is None:
			await message.channel.send("ボイスチャンネルに接続してね")
			return
		await message.author.voice.channel.connect()
		message.guild.voice_client.play(discord.FFmpegPCMAudio("nemuru.mp3"))
		await message.channel.send("終わったら「!終わった」ってしてね")
		
	elif message.content == "!終わった":
		await message.channel.send("じょあの")
		await message.guild.voice_client.disconnect()
		
client.run(bot_token)
