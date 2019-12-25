from Account import Account


class Checking(Account):

    __checks_written = []

    def __init__(self, initial_balance, apy, checks_written):
        super().__init__(initial_balance, apy)
        self.__checks_written = checks_written
