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

    def search_articles(self, search):
        '''
        Takes multiple keywords and retrieves all articles matching those keywords from db.
        Matches title, authors, abstract, venue and year fields (case insensitive).
        Used for: Phase 2 part 1
        Author: Connor
        params:
            search : str
        returns list[json]    matching articles 
        '''
        assert type(search) is str
        search_and = "\"" + "\" \"".join(search.split()) + "\""
        result = self.db.dblp.find({"$text": {"$search": search_and}}, projection = ["id","title","year","venue","abstract","authors"])
        return list(result)

    def get_referees(self, aid):
        '''
        Gets all articles referring to a particular article
        Used for: Phase 2 part 1
        Author: Connor
        params:
            aid: str    Article id
        returns list(dict)  matching articles
        '''
        assert type(aid) is str
        result = self.db.dblp.find({"references": aid}, projection = ["id","title","year"])
        return list(result)

    def search_authors(self, keyword):
        '''
        Used for: Phase 2 part 2
        Author: Leon
        '''
        table = self.db["dblp"]
        results = table.distinct("authors", {"authors": { "$regex": f"\\b{keyword}\\b", "$options" :"i"}})
        return results
        
    def get_total_pubs(self, author_name):
        '''
        Returns total publications for an author.
        Used for: Phase 2 part 2
        Author: Leon, Connor
        '''
        return self.db.dblp.count_documents({"authors": author_name})

    def get_author_details(self, author_name):
        '''
        Gets details about a particular author.
        Used for: Phase 2 part 2
        Author: Leon, Connor
        '''
        return self.db.dblp.find({"authors": author_name}).sort("year", -1)
    
    def list_venues(self, n):
        '''
        Used for: Phase 2 part 3
        Author: Brandon, Leon 
        '''

        table = self.db["dblp"]

        results = table.aggregate([
            {"$group":{
                    "_id": "$venue",
                    "Articles": {"$sum":1}
                }
             },
             {"$sort": {"References_venue": -1}

              },

             {"$limit":n
              }

            ])
        for item in results:
            print(item)
    
    def add_article(self):
        '''
        Used for: Phase 2 part 4
        Author: Brandon
        '''
        authors=[]
        input_id=input("Enter the unique id:")
        input_title=input("Enter the title:")
        input_numofauthors=int(input("Enter the number of authors:"))
        for i in range(0,input_numofauthors):
            ele=[input("Enter the name of the authors:")]
            authors.append(ele)
        input_year=int(input("Enter the year:"))
        doc={
                "id": input_id,
                "title": input_title,
                "authors": authors,
                "venue": None,
                "year": input_year,
                "n_citation": 0,
                "references": [],
                "abstract": None
                }
        try:
            self.db.dblp.insert_one(doc)
            return True
        except Exception as e:
            print("Error occured:",e)
            return False

