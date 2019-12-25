from Account import Account


class Savings(Account):

    __apy = 0.0
    __max_withdraws = 0

    def __init__(self, customer, initial_balance, apy, max_withdraws):
        super().__init__(initial_balance, apy)
        self.__apy = apy
        self.__max_withdraws = max_withdraws
