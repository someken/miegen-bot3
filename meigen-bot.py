# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:07:01 2024

@author: somek
"""

import tweepy
import pandas as pd
import random

# Consumer Keys
ck = 'dytd9aJ8XjGyJ3Dvudr7IXBiF' #API KEYが入ります
cs = 'YL3Hjyi3qTI2W3PGnbi18WEaNaSdElTyp7Js3sGkprUfR0r1tB' #API KEY SECRETが入ります

# Authentication Tokens
bt = 'AAAAAAAAAAAAAAAAAAAAAIDRwwEAAAAAVxXO4DNcGuOUghuP8cbB0ziJOB8%3D0X4HA6LNdOsRxaoqV8NJTbW5BAlA25qIeNBPVWFx4pa7O9b2Pp' #Bearer Tokenが入ります
at = '1370346248868225024-ehrwago5FM51DKSgxfNSDESPH1kMpQ' #ACCESS TOKENが入ります
ats = 'bn5Rf2cP4iExZmOUz350pgC0zWA3HUSMWoeqQ57XKwk99' #ACCESS TOKEN SECRETが入ります

# 認証
client = tweepy.Client(
    bearer_token=bt,
    consumer_key=ck, consumer_secret=cs,
    access_token=at, access_token_secret=ats
)

# CSVファイルの読み込み
# 修正後のファイルパス
file_path = r"C:\Users\somek\.spyder-py3\名言_500.csv"

# CSVの読み込み
df = pd.read_csv(file_path, encoding='shift_jis')


# ランダムに名言、人名、職業を選択
random_quote = random.choice(df['Column1'])
random_name = random.choice(df['Column2'])
random_job = random.choice(df['Column3'])

# ツイート内容を作成
tweet_content = f'"{random_quote}" - {random_name}, {random_job}'

# ツイート
client.create_tweet(text=tweet_content)