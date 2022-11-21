import sys
from pymongo import MongoClient

def main():
    if len(sys.argv) > 2:
        json_filename = sys.argv[1]
        port = int(sys.argv[2])

        # Init db from here
        init_db(json_filename, port)

    else:
        print("Provide filename, port as argument!")
    return


def init_db(filename, port):
    assert type(filename) is str
    assert type(port) is int

    client = MongoClient("127.0.0.1", port)
    db = self.client["dblp"]



main()
