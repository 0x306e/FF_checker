# -- coding: utf-8 --
import tweepy
import json
import webbrowser

if __name__ == '__main__':
    setting = json.loads(open('./settings.json', 'r').read())
    auth = tweepy.OAuthHandler(setting['consumer_key'], setting['consumer_secret'])
    url = auth.get_authorization_url()
    webbrowser.open_new(url)
    print(f'if don`t open Twitter authorization, please access {url} and accept.')
    print('Enter pin code : ', end='')
    pin = input()
    auth.get_access_token(pin)
    api = tweepy.API(auth)
    uid = api.me().id

    config = {
        'user': {
            'user_id': int(uid),
            'consumer_key': setting['consumer_key'],
            'consumer_secret': setting['consumer_secret'],
            'access_token': auth.access_token,
            'access_token_secret': auth.access_token_secret
        },
        'following': {
        },
        'follower': {
        }
    }

    f = open(f'./data/{uid}.json', 'w')
    json.dump(config, f, indent=True)
    f.close()

    print('Account successfully added!')
    input('Press enter to close.')
