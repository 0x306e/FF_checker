import psycopg2


class Postgres:
    def __init__(self, user='postgres', host='localhost', port=None, password=None, dbname='ff_checker'):
        self.__user = user
        self.__hostname = host
        self.__port = port
        self.__password = password
        self.__dbname = dbname
        self.__connection = psycopg2.connect(
            f"host={self.__hostname} port={self.__port} dbname={self.__dbname}"
            f"user={self.__user} password={self.__password}"
        )
        self.__cursor = self.__connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def cursor(self):
        return self.__cursor

    def execute(self, sql: str):
        self.__cursor.execute(sql)

    def create_table(self, uid: int):
        self.execute(f"CREATE TABLE {uid} (uid BIGINT, following bool, follower bool)")

    def get_following(self, uid):
        self.__cursor.execute("SELECT * FROM %s WHERE following==True", (uid, ))
        return self.__cursor.fetchall()

    def get_follower(self, uid):
        self.__cursor.execute("SELECT * FROM %s WHERE follower==True", (uid, ))
        return self.__cursor.fetchall()

    def set_following(self, uid, newer_uid):
        self.__cursor.execute(f"INSERT INTO {uid}(uid, following) VALUES ({newer_uid}, True, ) "
                              f"ON CONFLICT ({newer_uid}) DO UPDATE SET uid={newer_uid} following=True")

    def set_following(self, uid, newer_uid):
        self.__cursor.execute(f"INSERT INTO {uid}(uid, follower) VALUES ({newer_uid}, True, ) "
                              f"ON CONFLICT ({newer_uid}) DO UPDATE SET uid={newer_uid} follower=True")


if __name__ == '__main__':
    pg = Postgres()
    cur = pg.cursor()
