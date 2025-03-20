from paillier import Paillier

class Client:
    def __init__(self, bits=1024): 
        self.paillier = Paillier(bits) # constructor genereted the paillier cryptosystem
        self.public_key = self.paillier.public_key
        self.private_key = self.paillier.private_key

    def request(self, db_size, index):
        """ Creates a PIR request by encrypting a selection output """
        print(f"Creating request for index {index} in a database of size {db_size}")
        request_output = []

        for i in range(db_size):
            if i == index:
                encrypted_value = self.paillier.encrypt(1)
            else:
                encrypted_value = self.paillier.encrypt(0)
            request_output.append(encrypted_value)

        print("Request output created")
        return request_output

    def decryptAnswer(self, encrypted_response):
        """ Decrypts the server's response to retrieve the requested value """
        print("Decrypting server response...")
        result = self.paillier.decrypt(encrypted_response)
        print(f"Decryption complete: Retrieved value is {result}")
        return result
