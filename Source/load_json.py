import sys

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
    pass



main()
