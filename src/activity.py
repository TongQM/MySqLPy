import pymysql
from Database import Database

database = Database()

_host = database.gethost()
_port = database.getport()
_sql_user = database.getuser()
_sql_password = database.getpassword()
_database = database.getdatabase()

#! TODO setcomment


def setcomment(user_id, act_id, message):  # ! id is user's id message: string
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


def getcomment(id):  # ! this is act's id
    connection = pymysql.connect(
        _host, _port, _sql_user, _sql_password, _sql_password)
    # End
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `*` FROM `Comments` WHERE `Comments.act_id` = %d"
            cursor.execute(sql, (id))
            results = cursor.fetchall()
            for row in results:
                message = row[1]
                auth_id = row[2]
                act_id = row[3]
            # TODO return user_id
            return {"message": message, "auth_id": auth_id, "act_id": act_id}
    except Exception as e:
        print("Wrong", e)
    finally:
        connection.close()


def getactinfo(id):  # ! this is act's id BUG!!!!
    connection = pymysql.connect(
        _host, _port, _sql_user, _sql_password, _sql_password)
    # End
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `*` FROM `Activity` WHERE `Activity.id`=%d"
            cursor.execute(sql, (id))
            # TODO their must a bug because time problem
            results = cursor.fetchall()
            for row in results:
                name = row[0]
                time = row[1]  # !bug!
                level = row[2]
                location = row[3]
                introduction = row[4]
                teacher = row[5]
            return {"name": name, "time": time, "level": level, "location": location, "introduction": introduction, "teacher": teacher}

    except Exception as e:
        print("Wrong", e)
    finally:
        connection.close()

    #! get act name ,introducation
