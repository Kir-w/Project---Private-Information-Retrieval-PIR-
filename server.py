import random
from paillier import Paillier

class Server:
    def __init__(self, db_size=10):
        print(f"Generating a database with {db_size} elements...")
        self.db_size = db_size
        self.database = [random.randint(1, 100) for _ in range(db_size)]
        print(f"Database initialized: {self.database}")

    def process_request(self, request_vector, public_key):
        """ Computes the homomorphic response based on the request vector """
        print("Processing PIR request...")
        encrypted_sum = 1  # Start with neutral element for multiplication

        for i in range(self.db_size):
            encrypted_value = request_vector[i]
            encrypted_sum *= pow(encrypted_value, self.database[i], public_key[0]**2)  # Homomorphic multiplication
            encrypted_sum %= public_key[0]**2  # Keep result within n²

        print("Computation complete! Sending encrypted response...")
        return encrypted_sum

