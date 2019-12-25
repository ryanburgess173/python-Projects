class Address:

    __street_address = None
    __apt_number = None
    __city = None
    __state = None
    __zipcode = None

    def __init__(self, street_address, apt_number, city, state, zipcode):
        self.__street_address = street_address
        self.__apt_number = apt_number
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode

    def get_street_address(self):
        return self.__street_address

    def set_street_address(self, newStreetAddress):
        self.__street_address = newStreetAddress

    def get_apt_number(self):
        return self.__apt_number

    def set_apt_number(self, newAptNumber):
        self.__apt_number = newAptNumber

    def get_city(self):
        return self.__city

    def set_city(self, newCity):
        self.__city = newCity

    def get_state(self):
        return self.__state

    def set_state(self, newState):
        self.__state = newState

    def get_zip(self):
        return self.__zipcode

    def set_zip(self, newZip):
        self.__zipcode = newZip
