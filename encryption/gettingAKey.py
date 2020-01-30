from cryptography.fernet import Fernet


def main():
    key = Fernet.generate_key()
    print(key)


main()
