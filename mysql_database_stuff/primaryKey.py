from createConnection import MySQLConnection


def main():
    connection = MySQLConnection("learnPythonSQL")
    connection.get_mycursor().execute("SHOW TABLES")
    print(connection.get_mycursor())
    for x in connection.get_mycursor():
        if x == "customers":
            try:
                connection.get_mycursor().execute(
                    "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
                print("table already exists so we are just going to add our id column.")
            except:
                print("error occurred")
        else:
            try:
                connection.get_mycursor().execute(
                    "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
                print("table didn't yet exist so we created it and added an id column")
            except:
                print("error occurred")


main()
