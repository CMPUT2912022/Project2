"""
Stores all the methods pertaining to the Data Access Layer (DAL)
"""
class Application:
    def __init__(self, ip, port, db_name):
        self.ip = ip
        self.port = port
        self.db_name = db_name
        return
