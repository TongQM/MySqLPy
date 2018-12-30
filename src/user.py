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
        # Auth


def login(username, password):  # get username:string,password:string, return id
    connection = pymysql.connect(
        _host, _port, _sql_user, _sql_password, _sql_password)
    # End
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ('webmaster@python.org',))
            result = cursor.fetchone()
            print(result)
            # TODO return user_id

    except Exception as e:
        print("Wrong", e)
    finally:
        connection.close()


def getuserinfo(id):  # Auth:User_id , User:id TODO need to warp in to the login activity
    connection = pymysql.connect(
        _host, _port, _sql_user, _sql_password, _sql_password)
    # End
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ('webmaster@python.org',))
            result = cursor.fetchone()
            print(result)
            # TODO return user_id

    except Exception as e:
        print("Wrong", e)
    finally:
        connection.close()


def getcollection(id):  # get userid return user activity
    connection = pymysql.connect(
        _host, _port, _sql_user, _sql_password, _sql_password)
    # End
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ('webmaster@python.org',))
            # get user collention
            results = cursor.fetchall()
            for row in results:
                user_id = row[0]
                activity_id = row[1]
            return {"user_id": user_id, "activity_id": activity_id}
            # TODO return user_id

    except Exception as e:
        print("Wrong", e)
    finally:
        connection.close()

    #! get act name ,introducation

# TODO add restor function
# def restoreuser(useremail):
#     db = pymysql.connect(_host, _port, _sql_user, _sql_password, _sql_password)
#     cursor = db.cursor()
#     # TODO add sql line in here
#     sql = ""
#     # End
#     cursor.execute(sql)
#     db.close()
