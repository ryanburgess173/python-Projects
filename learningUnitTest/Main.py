from Address import Address
from Customer import Customer
from Account import Account
from Savings import Savings


def main():
    address = Address("1900 Travis Ln", "", "Mebane", "NC", "27302")
    customer = Customer("Johnathan", "Burgess", "(336) 508-8174",
                        "ryanburgess173@outlook.com", "000-00-0000", address)
    savings_account = Savings(customer, 8000, 4.5, 6)
    print(savings_account.get_customer().get_firstName(),
          savings_account.get_customer().get_lastName())


main()
