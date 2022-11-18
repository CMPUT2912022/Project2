"""
Command Line Interface (CLI) for Application
"""

class CommandLineInterface:
    functions = []
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
            selection = input("Selection: ")
            if selection in self.functions.keys():
                # Execute function call
                self.functions[selection][1]()
            elif selection in ["q", "Q"]:
                # Quit the application
                halt = True
            else:
                # Invalid input
                print("\n\n\nInvalid selection\n\n")
            print()
        return

    def search_articles(self):
        pass

    def search_authors(self):
        pass
    
    def list_venues(self):
        pass
    
    def add_article(self):
        pass
