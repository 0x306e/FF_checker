import json


class Configger:
    def __init__(self, path):
        self.file = open(path, 'r')
        self.conf = json.load(self.file)
        self.file.close()
        self.consumer_key = self.conf['user']['consumer_key']
        self.consumer_secret = self.conf['user']['consumer_secret']
        self.access_token = self.conf['user']['access_token']
        self.access_token_secret = self.conf['user']['access_token_secret']
        self.following = self.conf['following']
        self.follower = self.conf['follower']
