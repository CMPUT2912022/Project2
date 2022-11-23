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
        returns list[json]    matching articles 
        '''
        assert type(keywords) is list
        regex_keys = ''.join(["(?=.*" + key + ")" for key in keywords])
        result = self.db.dblp.find({"$or" : 
                                    [{"title" : {"$regex": regex_keys, "$options": "i"}}, 
                                     {"authors" : {"$regex": regex_keys, "$options": "i"}},
                                     {"abstract" : {"$regex": regex_keys, "$options": "i"}},
                                     {"venue" : {"$regex": regex_keys, "$options": "i"}},
                                     {"year" : {"$regex": regex_keys, "$options": "i"}}
                                     ]
                           })
        return list(result)

    def get_referees(self, aid):
        '''
        Gets all articles referring to a particular article
        Author: Connor
        params:
            aid: str    Article id
        returns list(dict)  matching articles
        '''
        assert type(aid) is str
        result = self.db.dblp.find({"references": aid})
        return list(result)

    def search_authors(self, keyword):
        '''
        Author: Leon
        '''
        table = self.db["dblp"]
        results = table.find({"authors": { "$regex": f"{keyword}", "$options" :"i"}})
        
        for item in results:
            name_index = 0
            n_publications = 0
            for name in item["authors"]:
                if keyword.lower() in name.lower():
                    name_index = item["authors"].index(name)
                    n_publications = table.count_documents({"authors": name})
            print(f"Author: {item['authors'][name_index] : <30}Publications: {n_publications}")

        
        chosen = input("Select an author:")
        if chosen.lower() == "back":
            return
        else:
            return
        
        #returns nothingn all work is done here
        return
    
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
