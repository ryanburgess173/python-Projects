import Address
import Customer
import Account
import Savings
import Checking


def main():
    address = Address.Address("1832 Billy T. Trail",
                              "", "Mebane", "NC", "27302")
    customer = Customer.Customer("Johnathan", "Burgess", "336-508-8174",
                                 "ryanburgess173@outlook.com", "000-00-0000", address)
    savingsAccount = Savings.Savings(customer, 7500, 4.5, 6)
    print(savingsAccount)


main()
