import threading

from core.checker import Checker
from core.client import Client
from core.configger import Configger


class Main(threading.Thread):
    def __init__(self, account=None):
        super(Main, self).__init__()
        self.account = account

    def run(self):
        conf = Configger(f'./data/{self.account}')
        client = Client.create_from_conf(conf)
        following_currently = client.get_following()
        follower_currently = client.get_follower()
        follower_checker = Checker(conf.follower, follower_currently)
        following_checker = Checker(conf.following, following_currently)

        message = follower_checker.create_message_follower() + following_checker.create_message_following()
        if message != '':
            client.send_direct_message(client.api.me().id, message)
            conf.update('following', following_currently)
            conf.update('follower', follower_currently)
            conf.store()
