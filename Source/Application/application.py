"""
Stores all the methods pertaining to the Data Access Layer (DAL)
"""

from pymongo import MongoClient


class Application:
    def __init__(self, ip, port, db_name):
        # TODO: This will have to be refactored
        assert type(port) is int
        assert type(ip) is str
        assert type(db_name) is str

        self.ip = ip
        self.port = port
        self.db_name = db_name

        self.client = MongoClient(self.ip, self.port)
        self.db = self.client[db_name]


        return

    def init_db(self):
        pass
