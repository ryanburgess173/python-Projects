class Customer:

    def __int__(self, fName, lName, home, cell, address, email, cP):
        self.__firstName = fName
        self.__lastName = lName
        self.__homePhone = home
        self.__cellPhone = cell
        self.__address = address
        self.__email = email
        self.__customerProfile = cP

    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, fName):
        self.__firstName = fName

    @firstName.deleter
    def firstName(self):
        del self.__firstName
