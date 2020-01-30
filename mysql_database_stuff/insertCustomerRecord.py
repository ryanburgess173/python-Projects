from createConnection import MySQLConnection


def main():
    connection = MySQLConnection("learnPythonSQL")
    mycursor = connection.get_mycursor()

    continueInserting = True
    while(continueInserting):
        userChoice = str(
            input("Would you like to insert a new customer record? (y/n)"))
        if(userChoice != 'y'):
            print("Okay, thank you for your time.")
            break
        else:
            name, address = getUserInput()
            insertRecord(mycursor, name, address)
            connection.get_mydb().commit()
            print(mycursor.rowcount, "record inserted.")


def getUserInput():
    name = str(input("Enter full name of customer: "))
    address = str(input("Enter full address of customer: "))
    return name, address


def insertRecord(mycursor, name, address):
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = (name, address)
    mycursor.execute(sql, val)


main()
