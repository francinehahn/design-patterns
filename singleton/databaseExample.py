import sqlite3

class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        #cls in this case represents the class Database
        if not cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]

class Database(metaclass=Singleton):
    connection = None

    def connect(self):
        if self.connection is None:
            print("There's no connection established yet...")
            self.connection = sqlite3.connect('db.geek')
            self.cursor = self.connection.cursor()
        return self.cursor

db1 = Database().connect()
db2 = Database().connect()