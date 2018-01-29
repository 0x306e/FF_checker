from core.client import Client
from core.configger import Configger

if __name__ == '__main__':
    conf = Configger('./data/411320186.json')
    client = Client(conf)
