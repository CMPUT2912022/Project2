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
        table = self.db["dblp"]
        grouped_table = table.aggregate([
            {$match:{
                venue: 
                
                },
            {$group:
                {venue: "$venue"
                    }
                }
            ])
        


        # TODO
        pass
    
    def add_article(self):
        '''
        Author: Brandon
        '''
        authors=[]
        input_id=input("Enter the unique id:")
        input_title=input("Enter the title:")
        input_numofauthors=int(input("Enter the number of authors:"))
        for i in rangee(0,input_numofauthors):
            ele=[input("Enter the name of the authors:")]
            authors.append(ele)
            input_year=int(input("Enter the year:")
        doc=
            {
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
            return true
        except Exception as e:
            print("Error occured:",e)
            return false



