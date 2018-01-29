import json


class Configger:
    def __init__(self, path):
        self.__file = open(path)
        self.conf = json.load(open(self.__file))['user']
        self.__file.close()
        self.consumer_key = self.conf['consumer_key']
        self.consumer_secret = self.conf['consumer_secret']
        self.access_token = self.conf['access_token']
        self.access_token_secret = self.conf['access_token_secret']
