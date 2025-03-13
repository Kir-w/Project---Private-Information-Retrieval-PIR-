from paillier import Paillier

class Client:
    def __init__(self, bits=1024):
        print("Generating client key pair...")
        self.paillier = Paillier(bits)
        self.public_key = self.paillier.public_key
        self.private_key = self.paillier.private_key
        print("Client key pair generated!")

    def create_request(self, db_size, index):
        """ Creates a PIR request by encrypting a selection vector """
        print(f"Creating request for index {index} in a database of size {db_size}")
        request_vector = []

        for i in range(db_size):
            if i == index:
                encrypted_value = self.paillier.encrypt(1)
            else:
                encrypted_value = self.paillier.encrypt(0)
            request_vector.append(encrypted_value)

        print("Request vector created!")
        return request_vector

    def decrypt_response(self, encrypted_response):
        """ Decrypts the server's response to retrieve the requested value """
        print("Decrypting server response...")
        result = self.paillier.decrypt(encrypted_response)
        print(f"Decryption complete: Retrieved value is {result}")
        return result
