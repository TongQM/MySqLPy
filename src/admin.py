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
    "teacher":teacher,
    "time":[start_time,end_time,repect],
    "level":0...5,
    "location":location,
    "introduction":introduction
}
'''


def addactivity(infodict):  # add activity into the
    connection = pymysql.connect(
        _host, _port, _sql_user, _sql_password, _sql_password)
    # End
    try:
        with connection.cursor() as cursor:
            # Create a new record
            # TODO add sql line in here
            sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # !connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    except Exception as e:
        print("Wrong", e)
    finally:
        connection.close()


def delactivity(id):  # id is activity_id
    connection = pymysql.connect(
        _host, _port, _sql_user, _sql_password, _sql_password)
    # End
    try:
        with connection.cursor() as cursor:
            # Create a new record
            # TODO add sql line in here
            sql1 = "delete from activity where activity_id=%d;"
            sql2 = "delete from time where id in (select time from Activity where activity_id=%d)"
            sql = sql1 + sql2
            cursor.execute(sql, (id, id))
        # !connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    except Exception as e:
        print("Wrong", e)
    finally:
        connection.close()
