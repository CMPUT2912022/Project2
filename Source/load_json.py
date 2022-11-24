import sys, json, os
from pymongo import MongoClient, TEXT
from pymongo.errors import ConnectionFailure
from pymongo.collation import Collation

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

    try:
        client.admin.command('ismaster')
    except ConnectionFailure:
        print("Connection to MongoDB server failed!")
        exit()

    db = client["291db"]

    # See if collection exists
    collist = db.list_collection_names()
    if "dblp" in collist:
        # drop db and reinit
        db.dblp.drop()

    # init collection
    db["dblp"]

    # Mass import from given file
    os.system("mongoimport --host=localhost:" + str(port) + " --file " + filename + " --db 291db --collection dblp")

    # Create indices
    db.dblp.create_index(
            [
                ("title", TEXT),
                ("authors", TEXT),
                ("abstract", TEXT),
                ("venue", TEXT),
                ("year", TEXT)
            ],
            default_language = "none"
            )
    db.dblp.create_index([("year", -1)])
    return



main()
