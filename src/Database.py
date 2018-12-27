class Database:
    _host = "129.204.75.9"
    _port = 3306
    _sql_user = "root"
    _sql_password = "mysql123456"
    _database = "DataSQL"

    def gethost(self):
        return self._host

    def getport(self):
        return self._port

    def getuser(self):
        return self._sql_user

    def getpassword(self):
        return self._sql_password

    def getdatabase(self):
        return self._database
