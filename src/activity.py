import pymysql
from Database import Database

database = Database()

_host = database.gethost()
_port = database.getport()
_sql_user = database.getuser()
_sql_password = database.getpassword()
_database = database.getdatabase()


def setcomment(id, message):  # ! id is user's id message: string
    db = pymysql.connect(_host, _port, _sql_user, _sql_password, _sql_password)
    cursor = db.cursor()
    # TODO add sql line in hear
    sql = ""
    # End
    cursor.execute(sql)
    db.close()


def getcomment(id):  # ! this is act's id
    db = pymysql.connect(_host, _port, _sql_user, _sql_password, _sql_password)
    cursor = db.cursor()
    # TODO add sql line in hear
    sql = ""
    # End
    cursor.execute(sql)
    db.close()


def getactinfo(id):  # ! this is act's id
    db = pymysql.connect(_host, _port, _sql_user, _sql_password, _sql_password)
    cursor = db.cursor()
    # TODO add sql line in hear
    sql = ""
    # End
    cursor.execute(sql)
    # get actinfo
    results = cursor.fetchall()
    # TODO their must a bug because time problem
    for row in results:
        name = row[0]
        time = row[1]  # !bug!
        level = row[2]
        location = row[3]
        introduction = row[4]
    db.close()
    return {"name": name, "time": time, "level": level, "location": location, "introduction": introduction}
