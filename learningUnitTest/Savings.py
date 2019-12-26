from Account import Account


class Savings(Account):

    __apy = 0.0
    __max_withdraws = 0

    def __init__(self, customer, initial_balance, apy, max_withdraws):
        super().__init__(customer, initial_balance)
        self.__apy = apy
        self.__max_withdraws = max_withdraws

    def get_apy(self):
        return self.__apy

    def set_apy(self, newAPY):
        self.__apy = newAPY

    def get_max_withdraws(self):
        return self.__max_withdraws

    def set_max_withdraws(self, newMaxWithdraws):
        self.__max_withdraws = newMaxWithdraws
