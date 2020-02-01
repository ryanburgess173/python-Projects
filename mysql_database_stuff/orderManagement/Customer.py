class Customer:

    __firstName = None
    __lastName = None
    __homePhone = None
    __cellPhone = None
    __address = None
    __email = None
    __customerProfile = None

    def __int__(self, fName, lName, home, cell, address, email, cP):
        self.__firstName = fName
        self.__lastName = lName
        self.__homePhone = home
        self.__cellPhone = cell
        self.__address = address
        self.__email = email
        self.__customerProfile = cP

    def setFirstName(self, fName):
        self.__firstName = fName

    def getFirstName(self):
        return self.__firstName

    def setLastName(self, lName):
        self.__lastName = lName

    def getLastName(self):
        return self.__lastName

    def setHomePhone(self, homePhone):
        self.__homePhone = homePhone

    def getHomePhone(self):
        return self.__homePhone

    def setCellPhone(self, cellPhone):
        self.__cellPhone = cellPhone

    def getCellPhone(self):
        return self.__cellPhone
