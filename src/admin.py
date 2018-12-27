import pymysql
from Database import Database

database = Database()

_host = database.gethost()
_port = database.getport()
_sql_user = database.getuser()
_sql_password = database.getpassword()
_database = database.getdatabase()

'''
infordict is a dict that storge all needed Data
form as: 
{
    "name":name,
    "time":[start_time,end_time,repect],
    "level":0...5,
    "location":location,
    "introduction":introduction
}
'''


def addactivity(infodict):  # add activity into the
    db = pymysql.connect(_host, _port, _sql_user, _sql_password, _sql_password)
    cursor = db.cursor()
    # TODO add sql line in hear
    sql = ""
    # End
    cursor.execute(sql)
    db.close()


def delactivity(id):  # id is course_id
    db = pymysql.connect(_host, _port, _sql_user, _sql_password, _sql_password)
    cursor = db.cursor()
    # TODO add sql line in hear
    sql = ""
    # End
    cursor.execute(sql)
    db.close()
