"""
Command Line Interface (CLI) for Application
"""

from pprint import pprint

class CommandLineInterface:
    functions = []
    delim_str = "\n\n" + "="*70 + "\n\n"
    def __init__(self, app):
        self.app = app
        self.functions = {
                "1": ("Search for articles", self.search_articles),
                "2": ("Search for authors", self.search_authors),
                "3": ("List venues", self.list_venues),
                "4": ("Add an article", self.add_article)
                }

    def start(self):
        """
        Starts the interface. Begins taking user input, and displaying output.
        """
        print("Application started!\n\n")

        halt = False
        while not halt:
            print("Select option")
            for k, f in self.functions.items():
                print(k + ": " + f[0])
            print("q: Quit")
            selection = input("Selection: ")
            if selection in self.functions.keys():
                # Execute function call
                self.functions[selection][1]()
            elif selection in ["q", "Q"]:
                # Quit the application
                halt = True
            else:
                # Invalid input
                print("\nInvalid selection!")
            print(self.delim_str)
        return

    def search_articles(self):
        '''
        User should be able to provide one or more keywords, and the 
        system should retrieve all articles that match all those 
        keywords (AND semantics).

        Author: Connor
        '''
        keywords = input("\nEnter Keywords (space separated): ").split()
        result = self.app.search_articles(keywords)


        trimmed_result = [{"id": d["id"], "title": d["title"], "year": d["year"], "venue":d["venue"]}
                 for d in result
                 ]

        for i in range(len(trimmed_result)):
            print("Article No", i, ":")
            pprint(trimmed_result[i], indent=4)
            print("\n")


    def search_authors(self):
        '''
        Author: Leon
        '''
        keyword = input("Search for: ")
        if keyword.lower() == "back":
            return
        else:
            self.app.search_authors(keyword)
        
        # TODO
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

