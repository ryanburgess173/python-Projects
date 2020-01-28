import mysql.connector


class MySQLConnection:
    mydb = None
    mycursor = None

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=""
        )
        self.mycursor = self.mydb.cursor()
