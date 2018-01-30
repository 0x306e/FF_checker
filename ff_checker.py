import os

if __name__ == '__main__':
    accounts = os.listdir('./data/')
    for account in accounts:
        if account != 'sample.json':
            hoge.start(f'./data/{account}')
