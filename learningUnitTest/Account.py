class Account:

    __customer = None
    __initial_balance = 0.0

    def __init__(self, customer, initial_balance):
        self.__customer = customer
        self.__initial_balance = initial_balance
