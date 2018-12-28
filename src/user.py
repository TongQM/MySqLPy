import pymysql
from Database import Database

database = Database()

_host = database.gethost()
_port = database.getport()
_sql_user = database.getuser()
_sql_password = database.getpassword()
_database = database.getdatabase()


# get username:string,password:string,useremail:string, return id
def register(username, password, useremail, bio, reg_time):
    db = pymysql.connect(_host, _port, _sql_user, _sql_password, _sql_password)
    cursor = db.cursor()
    # TODO add sql line in hear
    sql = ""
    # End
    cursor.execute(sql)
    db.close()


def login(username, password):  # get username:string,password:string, return id
    db = pymysql.connect(_host, _port, _sql_user, _sql_password, _sql_password)
    cursor = db.cursor()
    # TODO add sql line in hear
    sql = ""
    # End
    cursor.execute(sql)
    db.close()


def getuserinfo(id):  # TODO need to warp in to the login activity
    db = pymysql.connect(_host, _port, _sql_user, _sql_password, _sql_password)
    cursor = db.cursor()
    # TODO add sql line in hear
    sql = ""
    # End
    cursor.execute(sql)
    # get userinfo
    results = cursor.fetchall()
    for row in results:
        reg_time = row[0]
        bio = row[1]
    db.close()
    return {"reg_time": reg_time, "bio": bio}


def getcollection(id):  # get userid return user activity
    db = pymysql.connect(_host, _port, _sql_user, _sql_password, _sql_password)
    cursor = db.cursor()
    # TODO add sql line in hear
    sql = ""
    # End
    cursor.execute(sql)
    # get user collention
    results = cursor.fetchall()
    for row in results:
        user_id = row[0]
        activity_id = row[1]
    db.close()
    return {"user_id": user_id, "activity_id": activity_id}


def restoreuser(useremail):  # check whether
    db = pymysql.connect(_host, _port, _sql_user, _sql_password, _sql_password)
    cursor = db.cursor()
    # TODO add sql line in hear
    sql = ""
    # End
    cursor.execute(sql)
    db.close()
