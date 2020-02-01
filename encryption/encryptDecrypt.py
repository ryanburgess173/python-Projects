from cryptography.fernet import Fernet


class EncryptDecrypt:
    __key = None
    __message = None

    def __init__(self, key, message):
        self.__key = key
        self.__message = message

    def encrypt(self):
        f = Fernet(self.__key)
        self.__message = f.encrypt(self.__message.encode())

    def decrypt(self):
        f = Fernet(self__key)
