class Address:

    def __init__(self, street, apt=None, city, state, zipCode, country=None):
        self.__street = street
        self.__apt = apt
        self.__city = city
        self.__state = state
        self.__zip = zipCode
        self.__country = country
