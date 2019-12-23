class Customer:

    __firstName = ""
    __lastName = ""
    __phone = ""
    __email = ""
    __ssn = ""
    __address = None

    def __init__(self, firstName, lastName, phone, email, ssn, address):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__phone = phone
        self.__email = email
        self.__ssn = ssn
        self.__address = address
