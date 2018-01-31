import json


class Configger:
    def __init__(self, path=None):
        self.path = path
        fp = open(path, 'r')
        self.__json = json.load(fp)
        fp.close()
        self.consumer_key = self.__json['user']['consumer_key']
        self.consumer_secret = self.__json['user']['consumer_secret']
        self.access_token = self.__json['user']['access_token']
        self.access_token_secret = self.__json['user']['access_token_secret']
        self.following = self.__json['following']
        self.follower = self.__json['follower']
