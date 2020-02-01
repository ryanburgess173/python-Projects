from cryptography.fernet import Fernet


def main():
    key = Fernet.generate_key()

    file = open('key.key', 'wb')
    file.write(key)
    file.close()


main()
