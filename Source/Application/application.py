"""
Stores all the methods pertaining to the Data Access Layer (DAL)
"""

from pymongo import MongoClient


class Application:
    def __init__(self, ip, port, db_name):
        assert type(port) is int
        assert type(ip) is str
        assert type(db_name) is str

        self.ip = ip
        self.port = port
        self.db_name = db_name

        self.client = MongoClient(self.ip, self.port)
        self.db = self.client[db_name]
        return

    def search_articles(self, keywords):
        '''
        Author: Connor
        '''
        assert type(keywords) is list
        # TODO
        pass

    def search_authors(self, keyword):
        # TODO
        pass
    
    def list_venues(self):
        # TODO
        pass
    
    def add_article(self):
        # TODO
        pass
