# -- coding: utf-8 --
import oauth2 as oauth


class OAuth:
    def __init__(self, consumer_key, consumer_secret):
        self.consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
        self.conf_dic = ({})
        self.keys_dic = ({})

    def get_url(self):
        client = oauth.Client(self.consumer)
        resp, content = client.request('https://api.twitter.com/oauth/request_token', 'GET')

        conf = [t.split() for t in content.decode('utf-8').split("&")]
        for t in conf:
            var = t[0].split("=")
            self.conf_dic.update({var[0]: var[1]})
        return "https://api.twitter.com/oauth/authorize?oauth_token=" + self.conf_dic['oauth_token']

    def get_token(self, pin):
        token = oauth.Token(self.conf_dic['oauth_token'].encode('utf-8'),
                            self.conf_dic['oauth_token_secret'].encode('utf-8'))
        client = oauth.Client(self.consumer, token)
        resp, keys = client.request("https://api.twitter.com/oauth/access_token", "POST",
                                        body="oauth_verifier={0}".format(pin))
        keys_list = [key.split() for key in keys.decode('utf-8').split('&')]
        for t in keys_list:
            var = t[0].split('=')
            self.keys_dic.update({var[0]: var[1]})
        return self.keys_dic['oauth_token'], self.keys_dic['oauth_token_secret']

    def get_uid(self):
        return self.keys_dic['user_id']
