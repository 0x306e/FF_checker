import tweepy


class Client:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def __init__(self, conf):
        self.auth = tweepy.OAuthHandler(conf.consumer_key, conf.consumer_secret)
        self.auth.set_access_token(conf.access_token, conf.access_token_secret)
        self.api = tweepy.API(self.auth)

    def get_following(self):
        id_sn = {}
        for user in tweepy.Cursor(self.api.friends, cursor=-1).items():
            id_sn[user.id] = user.screen_name
        return id_sn

    def get_follower(self):
        id_sn = {}
        for user in tweepy.Cursor(self.api.followers, cursor=-1).items():
            id_sn[user.id] = user.screen_name
        return id_sn

    def send_direct_message(self, uid, message):
        self.api.send_direct_message(user_id=uid, text=message)
