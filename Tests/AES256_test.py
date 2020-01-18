from FunTOTP.AES256 import crypt
import unittest

class TestStringMethods(unittest.TestCase):
    password = "123"
    data = "Hello World"
    edata = b'gAAAAABd-4prMUAgBdi1YuWjpKuw_eLEPzRZlmGH5Wi9B0rEoUSgPYO_64-6eO4VLq93fY3voqdKzpPS00rlmx1eXwo-tPAfHg=='

    c = crypt(password)

    def test_encrypt_type(self):
        self.assertEqual(type(self.c.encrypt(self.data)), type(self.edata))

    def test_decrypt_string(self):
        self.assertEqual(self.data, self.c.decrypt(self.c.encrypt(self.data)))

    def test_decrypt_bytes(self):
        self.assertEqual(self.data, self.c.decrypt(self.c.encrypt(self.data.encode())))

    def test_two_instances_derive(self):
        C = crypt(self.password)
        self.assertEqual(C.derive_key("rtert"), self.c.derive_key("rtert"))

    def test_two_instances_decrypt(self):
        A = crypt(self.password)
        B = crypt(self.password)


        self.assertEqual(B.decrypt(A.encrypt(self.data)), self.data)

if __name__ == '__main__':
    unittest.main()
