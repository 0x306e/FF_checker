import os

from core.Main import Main

if __name__ == '__main__':
    accounts = os.listdir('./data/')
    for account in accounts:
        if account != 'sample.json':
            Main(account).start()
