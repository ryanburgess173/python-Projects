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
