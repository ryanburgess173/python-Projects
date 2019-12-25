from Account import Account


class Checking(Account):

    __checks_written = []

    def __init__(self, initial_balance, apy, checks_written):
        super().__init__(initial_balance, apy)
        self.__checks_written = checks_written

    def get_checks_written(self):
        return self.__checks_written

    def set_checks_written(self, checks_written):
        self.__checks_written = checks_written

    def add_check(self, check):
        self.__checks_written.append(check)
