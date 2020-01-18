#!/usr/bin/python3

import os
import ast
import json

from .interface import interface
from .AES256 import crypt
from .keys import keys


class keystore(object):
    """
    The keys' database
    """


    def __json_troubleshooting(self, arg):
        if arg == '':
            return ""
        else:
            temp_data = ast.literal_eval(arg)
            return json.dumps(temp_data)

    def verify_file(self, file):
        # If file exists, true, else, false
        if not os.path.isfile(file):
            return False

        else:
            with open(file, "r") as f:
                read = f.read()

            if read == "":
                os.remove(file)
                return False
            else:
                return True

    def __init__(self, file):
        self.i = interface()
        self.file = file

        if not self.verify_file(file):
            # If the file dont exixt or it's void, run wizard
            self.wizard()
        else:
            self.password = self.i.passwd()
            self.crypt = crypt(self.password)

        self.__data = self.get_data()

    def get_data(self):
        with open(self.file, "rb") as f:
            token = f.read()
            return self.crypt.decrypt(token)

    def dump(self):
        # Save the current cyphertext
        token = self.crypt.encrypt(self.__data.encode())

        # Delete the file with old cyphertext
        os.remove(self.file)

        # Create a new file with same name
        os.mknod(self.file)

        # Write the saved cyphertext to new file
        with open(self.file, "wb") as f:
            f.write(token)

    def add(self, secret, title='None'):
        keys_dictionary = keys(self.__json_troubleshooting(self.get_data()))
        keys_dictionary.add(secret, title)

        self.__data = str(keys_dictionary.keysd)
        self.dump()
    
    def remove(self, title):
        keyring = keys(self.__json_troubleshooting(self.get_data()))

        removed_key = keyring.remove(title)
        
        self.__data = str(keyring)
        self.dump()

        return removed_key
    
    def get(self, title):
        keyring = keys(self.__data)
        return keyring.get(title)

    def keys(self):
        keys_ob = keys(self.__json_troubleshooting(self.__data))

        return keys_ob.keysd

    def wizard(self):
        """
        Helps user to gen new keystore and keys
        """

        with open(self.file, 'w+') as f:
            print("File {} created".format(self.file))

        # Create a new key to encrypt this file
        self.password = self.i.newpasswd()
        self.crypt = crypt(self.password)
        self.__data = ''
        self.dump()

        self.i.info("New Keystore created")

    def erase(self):
        self.i.warning("THIS WILL DELETE ALL TOTP KEYS !!!")
        self.i.sure()
        os.remove(self.file)
        os.remove(self.pltfile)
        exit(0)
