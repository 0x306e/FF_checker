# -- coding: utf-8 --
import yaml
import webbrowser
from core.oauth import OAuth

if __name__ == '__main__':
    setting = yaml.safe_load(open('./settings.yml'))
    auth = OAuth(setting['consumer_key'], setting['consumer_secret'])
    url = auth.get_url()
    webbrowser.open(url)
    print(f'if don`t open Twitter authorization, please access {url} and accept.')
    print('Enter pin code : ', end='')
    pin = input()
    access_token, access_token_secret = auth.get_token(pin)
    uid = auth.get_uid()

    config = {
        'user_id': int(uid),
        'consumer_key': setting['consumer_key'],
        'consumer_secret': setting['consumer_secret'],
        'access_token': access_token,
        'access_token_secret': access_token_secret
    }
    f = open(f'./data/{uid}.yml', 'wt')
    yaml.dump(config, f, default_flow_style=False, encoding='utf-8')
    f.close()

    print('Account successfully added!')
    input('Press enter to close.')
