import pymysql
from Database import Database

database = Database()

_host = database.gethost()
_port = database.getport()
_sql_user = database.getuser()
_sql_password = database.getpassword()
_database = database.getdatabase()


# get username:string,password:string,useremail:string, return id
def register(login_name, username, password, useremail, bio):
    connection = pymysql.connect(
        _host, _port, _sql_user, _sql_password, _sql_password)
    # End
    try:
        with connection.cursor() as cursor:
            # Create a new record
            # TODO add sql line in here
            sql1 = "INSERT INTO `Auth` (`login_name`,`password`,`user_email`)  VALUES (%s, %s, %s)"
            cursor.execute(sql1, (login_name, password, useremail))
            sql2 = "INSERT INTO `User` (`user_name`, `bio`) VALUES (%s, %s)"
            cursor.execute(sql2, (username, bio))

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
            sql = "SELECT `Auth.user_id` FROM `Auth` WHERE `Auth.login_name` = %s AND Auth.`password` = %s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()
            return result
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
            sql = "SELECT `*` FROM `User` WHERE `User`.id = %d"
            cursor.execute(sql, (id))
            results = cursor.fetchall()
            for row in results:
                user_name = row[1]
                bio = row[2]
            return {"user_name": user_name, "bio": bio}

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
            sql = "SELECT Collection.activity_id FROM Collection WHERE Collection.user_id = %d"
            cursor.execute(sql, (id))
            # get user collention
            result = cursor.fetchone()
            return result

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
