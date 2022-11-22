"""
Stores all the methods pertaining to the Data Access Layer (DAL)
"""

import re
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
        Takes multiple keywords and retrieves all articles matching those keywords from db.
        Matches title, authors, abstract, venue and year fields (case insensitive).

        Author: Connor

        params:
            keywords : list[str]
        returns matching articles : list[json]
        '''
        assert type(keywords) is list
        regex_keys = ["/(?:" + kw + ")/gi" for kw in keywords]
        self.db.dblp.find({"title" : {"$in": regex_keys}}, 
                          {"authors" : {"$in": regex_keys}},
                          {"abstract" : {"$in": regex_keys}},
                          {"venue" : {"$in": regex_keys}},
                          {"year" : {"$in": regex_keys}}
                          )
        return

    def search_authors(self, keyword):
        '''
        Author: Leon
        '''
        # TODO
        pass
    
    def list_venues(self):
        '''
        Author: Brandon
        '''
        # TODO
        pass
    
    def add_article(self):
        '''
        Author: Brandon
        '''
        # TODO
        pass
