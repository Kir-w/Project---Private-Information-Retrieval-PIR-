from utils import *
from Crypto.Util import number
import gmpy2

class Paillier:
    def __init__(self, bits):
        self.keyGen(bits)

    def keyGen(self, bits):
        # Generate two large prime numbers p and q
        self.p = number.getPrime(bits)
        self.q = number.getPrime(bits)
        print(f"Generated primes: p={self.p}, q={self.q}")
        
        # Compute n and lambda
        self.n = self.p * self.q
        self.lambda_ = (self.p - 1) * (self.q - 1)
        print(f"Computed n={self.n} and lambda={self.lambda_}")
        
        # Compute g and mu
        self.g = self.n + 1
        self.mu = gmpy2.invert(self.lambda_, self.n)
        print(f"Computed g={self.g} and mu={self.mu}")
        
        # Public and private keys
        self.public_key = (self.n, self.g)
        self.private_key = (self.lambda_, self.mu)
        print("Public and private keys successfully created!")

    def encrypt(self, message: int):
        print(f"Encrypting message: {message}")
        n2 = self.n ** 2
        r = number.getRandomRange(1, self.n)
        while gmpy2.gcd(r, self.n) != 1:
            r = number.getRandomRange(1, self.n)
        
        ciphertext = (pow(self.g, message, n2) * pow(r, self.n, n2)) % n2
        print(f"Ciphertext: {ciphertext}")
        return ciphertext
    
    def decrypt(self, ciphertext: int):
        print(f"Decrypting ciphertext: {ciphertext}")
        n2 = self.n ** 2
        L = lambda x: (x - 1) // self.n
        
        message = (L(pow(ciphertext, self.lambda_, n2)) * self.mu) % self.n
        print(f"Decrypted message: {message}")
        return message
    
# Encryption / Decryption test
phe = Paillier(1024)
message = "Secret message to encrypt"
message_int = string_to_int(message)

print(f"Original message: {message}")
print(f"Message as integer: {message_int}")

ciphertext = phe.encrypt(message_int)
decrypted_message = phe.decrypt(ciphertext)

assert int_to_string(decrypted_message) == message
print("Encryption/Decryption successful!")
