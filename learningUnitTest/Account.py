class Account:

    __customer = None
    __initial_balance = 0.0

    def __init__(self, customer, initial_balance):
        self.__customer = customer
        self.__initial_balance = initial_balance

    def get_customer(self):
        return self.__customer

    def set_customer(self, newCustomer):
        self.__customer = newCustomer

    def get_initial_balance(self):
        return self.__initial_balance

    def set_initial_balance(self, newInitialBalance):
        self.__initial_balance = newInitialBalance
