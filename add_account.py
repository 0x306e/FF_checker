# -- coding: utf-8 --
import tweepy
import json
import webbrowser
from core.client import Client
from core.setting import Setting

if __name__ == '__main__':
    setting = Setting()
    auth = tweepy.OAuthHandler(setting['key']['consumer_key'], setting['key']['consumer_secret'])
    url = auth.get_authorization_url()
    webbrowser.open_new(url)
    print(f'if don`t open Twitter authorization, please access {url} and accept.')
    print('Enter pin code : ', end='')
    pin = input()
    auth.get_access_token(pin)
    client = Client(
        consumer_key=setting['consumer_key'],
        consumer_secret=setting['consumer_secret'],
        access_token=auth.access_token,
        access_token_secret=auth.access_token_secret
    )
    uid = client.api.me().id

    config = {
        'user': {
            'id': int(uid),
            'screen_name': client.api.me().screen_name,
            'consumer_key': setting['consumer_key'],
            'consumer_secret': setting['consumer_secret'],
            'access_token': auth.access_token,
            'access_token_secret': auth.access_token_secret
        },
        'following': client.get_following(),
        'follower': client.get_follower()
    }

    f = open(f'./data/{uid}.json', 'w')
    json.dump(config, f, indent=True)
    f.close()

    print('Account successfully added!')
    input('Press enter to close.')
