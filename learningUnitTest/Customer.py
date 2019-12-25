class Customer:

    __firstName = None
    __lastName = None
    __phone = None
    __email = None
    __ssn = None
    __address = None

    def __init__(self, firstName, lastName, phone, email, ssn, address):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__phone = phone
        self.__email = email
        self.__ssn = ssn
        self.__address = address

    def get_firstName(self):
        return self.__firstName

    def set_firstName(self, newFirstName):
        self.__firstName = newFirstName

    def get_lastName(self):
        return self.__lastName

    def set_lastName(self, newLastName):
        self.__lastName = newLastName

    def get_phone(self):
        return self.__phone

    def set_phone(self, newPhoneNumber):
        self.__phone = newPhoneNumber

    def get_email(self):
        return self.__email

    def set_email(self, newEmailAddress):
        self.__email = newEmailAddress

    def get_ssn(self):
        return self.__ssn

    def set_ssn(self, newSSN):
        self.__ssn = newSSN

    def get_address(self):
        return self.__address

    def set_address(self, newAddress):
        self.__address = newAddress
