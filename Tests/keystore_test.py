#!/usr/bin/python3
import os
import unittest
from FunTOTP import keystore

class TestStringMethods(unittest.TestCase):
    password = "rtertk45453"
    key = "ZYTYYE5FOAGW5ML7LRWUL4WTZLNJAMZS"
    file = "testfile.funtotp"

    def test_just_create_a_instance(self):
        k = keystore.keystore(self.file)
    
    def test_add_key(self):
        k = keystore.keystore(self.file)
        k.add('top secret string', 'title')
        print(k.get('title'))
    
    def test_remove(self):
        k = keystore.keystore(self.file)
        k.add('title', 'top secret string')
        k.remove('title')
    
    def test_totp(self):
        k = keystore.keystore(self.file)
        k.add(self.key, "Test Secret")
        print(k.keys())
    
    def test_dump(self):
        k = keystore.keystore(self.file)
        k.add(self.key, "Test Secret")
        k.dump()
    

if __name__ == '__main__':
    unittest.main()
