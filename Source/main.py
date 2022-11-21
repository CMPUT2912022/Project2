import sys
from Application.application import *
from Interface.cli import *


def main():
    db_ip = "127.0.0.1"
    db_name = "291db"

    # Get database argument
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        app = Application(db_ip, port, db_name)
        interface = CommandLineInterface(app)

        interface.start()
    else:
        print("Provide port as argument!")
    return


main()
