# Encryption and Decryption in Python
# https://nitratine.net/blog/post/encryption-and-decryption-in-python/

from cryptography.fernet import Fernet

import logging as log
from .interface import interface

class crypt(object):
    def __init__(self, password):
        # Old implentation using SHA512
        #import hashlib
        #self.__salt = hashlib.sha512(password.encode()).digest()
        
        # New using Whirlpool
        import whirlpool
        wp = whirlpool.new(password.encode())
        self.__salt = wp.hexdigest().encode()
        
        self.key = self.derive_key(password)

    def derive_key(self, password):
        """
        Get a key from string

        Parameters
        ----------
        password : type str
            Use cryptography methods to derivate a key from a string

        Returns
        -------
        str (binary)
            A key in binary format

        More info
        ---------
        'Encryption and Decryption in Python'
            https://nitratine.net/blog/post/encryption-and-decryption-in-python/
        """

        from cryptography.hazmat.backends import default_backend
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
        import base64

        password = password.encode() # Convert to type bytes

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.__salt,
            iterations=100000,
            backend=default_backend()
        )

        key = base64.urlsafe_b64encode(kdf.derive(password))

        return key

    def encrypt(self, data):
        f = Fernet(self.key)

        if isinstance(data, str):
            return f.encrypt(data.encode())

        elif isinstance(data, bytes):
            return f.encrypt(data)

        else:
            raise Exception("Wrong type of variable to encrypt: {}".format(type(data)))

    def decrypt(self, token):
        f = Fernet(self.key)

        if isinstance(token, str):
            try:
                return f.decrypt(token.encode()).decode()
            except cryptography.fernet.InvalidToken as err:
                print("Invalid password: {}".format(err))
                return False
            finally:
                print("Decryption successfully")

        elif isinstance(token, bytes):
            try:
                return f.decrypt(token).decode()
            except cryptography.fernet.InvalidToken as err:
                print("Invalid password: {}".format(err))
                return False
            finally:
                print("Decryption successfully")
            
        else:
            raise Exception("Wrong type of variable to decrypt: {}".format(type(token)))
