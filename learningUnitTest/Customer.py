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
