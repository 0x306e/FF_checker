import psycopg2


class Postgres:
    def __init__(self, user='postgres', host='localhost', port=None, password=None, dbname='ff_checker'):
        self.__user = user
        self.__hostname = host
        self.__port = port
        self.__password = password
        self.__dbname = dbname
        self.connection = psycopg2.connect(f"host={self.__hostname} port={self.__port} dbname={self.__dbname} user={self.__user} password={self.__password}")
        self.cursor = self.connection.cursor()

    def cursor(self):
        return self.__cursor
