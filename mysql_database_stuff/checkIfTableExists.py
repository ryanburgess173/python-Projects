from createConnection import MySQLConnection


def main():
    connection = MySQLConnection("learnPythonSQL")
    connection.get_mycursor().execute("SHOW TABLES")

    for x in connection.get_mycursor():
        print(x)


main()
