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
        Author: Connor
        params:
            keywords : list(str)
        returns list[json]    matching articles 
        '''
        assert type(search) is str
        search_and = "\"" + "\" \"".join(search.split()) + "\""
        result = self.db.dblp.find({"$text": {"$search": search_and}}, projection = ["id","title","year","venue"])
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
        result = self.db.dblp.find({"references": aid}, projection = ["id","title","year"])
        return list(result)

    def search_authors(self, keyword):
        '''
        Author: Leon
        '''
        table = self.db["dblp"]
        #results = table.distinct("authors", {"authors": keyword})
        results = table.distinct("authors", {"authors": { "$regex": f"{keyword}", "$options" :"i"}})
        
        authors = []
        ran = 0
        print()
        for name in results:
            ran = 1
            name_index = 0
            n_publications = 0
            if keyword.lower() in name.lower():
                authors.append(name)
                n_publications = table.count_documents({"authors": name})
                print(f"Author: {name : <30}Publications: {n_publications}")
        if not ran:
            print("Nothing found...  (╯°□° ）╯︵ ┻━┻")
            return
        while 1:
            print()
            chosen = input("Select an author: ")
            if chosen.lower() == "back":
                return
            else:
                found = 0
                print()
                for name in authors:
                    if chosen == name:
                        found = 1
                        info = table.find({"authors": name}).sort("year", -1)
                        for element in info:
                            print(f"Title: {element['title']:<70} | Year: {element['year']} | Venue: {element['venue']: >10}")
                if not found:
                    print("Could not find specified artist. Type the exact name or type 'back' to return to the previous menu. ~(˘▾˘~)")
                else:
                    return
            #returns nothingn all work is done here

    
    def list_venues(self, n):
        '''
        Author: Brandon, Leon 
        '''

        table = self.db["dblp"]
        #grouped_table = table.aggregate([
        #    {$match:{
        #        venue: 
        #        
        #        },
        #    {$group:
        #        {venue: "$venue"
        #            }
        #        }
        #    ])

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
        '''
        results = table.distinct("venue",{"venue" : {"$exists": True, "$ne" : ""}})
        #find all unique venues
        final = []
        for venue in results:
            #for each venue find all books in that venue
            books = table.find({"venue": venue}, {"id": 1, "_id":0})
            count = 0
            for book in books:
                #for every book that is in our venue, find all spots where that book id is referenced
                ID = book["id"]
                current = table.count_documents({"references": ID})
                count += 5
            #n_articles = table.count_documents({"venue": venue})
            
            final.append((venue, 0, count))
        print("aaaaaa")
       # for i in range(0,n):
           # max_value = max(my_list, key=lambda tup: tup[2])
           # final.remove(max_value)
           # print(f"{i+1})Venue: {max_value[0]} | Articles: {max_value[1]} | References to venue: {max_value[2]}")
        '''
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



