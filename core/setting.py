import json


class Setting:
    PATH = './settings.json'

    def __init__(self):
        fp = open(Setting.PATH, 'r')
        self.__json = json.load(fp)
        fp.close()
        self.key = self.__json['keys']
        self.general = self.__json['general']
