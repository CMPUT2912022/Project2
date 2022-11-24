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
        search = input("\nEnter Keywords (space separated): ")
        result = self.app.search_articles(search)

        trimmed_result = [{"id": d["id"], "title": d["title"], "year": d["year"], "venue":d["venue"]}
                 for d in result
                 ]

        for i in range(len(trimmed_result)):
            print("Article No", i, ":")
            pprint(trimmed_result[i], indent=4)
            print("\n")

        if len(result) > 0:
            # Allow user to select a particular article for more info
            prompt = "Article number for more info (or 'q' to quit): "
            selection = input(prompt)
            while selection not in ['q', 'Q'] and (not selection.isnumeric() or int(selection) not in range(len(result))):
                # Check that selection is a number and in correct range, or quit symbol, 
                print("\nInvalid input!")
                selection = input(prompt)

            if selection not in ['q', 'Q']:
                article_index = int(selection)
                print(self.delim_str)
                pprint(result[article_index])
                print("\n\nReferred to by:")
                aid = result[article_index]["id"]
                result = self.app.get_referees(aid)
                pprint(result)
        return

    def search_authors(self):
        '''
        Author: Leon, Connor
        '''
        keyword = input("Search ('back' to exit): ")
        if keyword.lower() != "back":
            print()
            results = self.app.search_authors(keyword)
            authors = {}
            for name in results:
                if keyword.lower() in name.lower():
                    n_publications = self.app.get_total_pubs(name)
                    authors[name] = n_publications
                    print(f"Author: {name : <30}Publications: {n_publications}")

            if len(authors)>0:
                should_halt = False
                chosen = ""
                while not should_halt:
                    chosen = input("Select an author ('back' to exit): ")
                    if chosen.lower() == "back":
                        should_halt = True
                    elif chosen in authors:
                        print()
                        auth = authors[chosen]
                        info = self.app.get_author_details(chosen)
                        for element in info:
                            print(f"Title: {element['title']:<70} | Year: {element['year']} | Venue: {element['venue']: >10}")
                        should_halt = True
                    else:
                        print("Could not find specified artist. Type the exact name or type 'back' to return to the previous menu. ~(˘▾˘~)")
            else:
                print("Nothing found...  (╯°□° ）╯︵ ┻━┻")
        return
    
    def list_venues(self):
        '''
        Author: Brandon, Leon 
        '''

        n = input("Number of venues to show: ")
        try:
            n = int(n)
        except:
            if n.lower() == "back":
                return
            else:
                print()
                print("Not a number! ಠ_ಠ")
                return
        
        self.app.list_venues(int(n))
        
    def add_article(self):
        '''
        Author: Brandon
        '''
        count =int(input("Enter the number of articles: (Enter '0' to return)"))
        if count == 0:
            return 
        else: 
            for i in range(count):
                self.app.add_article()

