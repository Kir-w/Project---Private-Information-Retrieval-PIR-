from client import Client
from server import Server

# Initialize client and server
client = Client(bits=1024)
server = Server(db_size=10)

# Choose an index to request
index_to_retrieve = 3
print(f"Client is requesting the value at index {index_to_retrieve}")

# Client creates a request
request_client = client.request(server.db_size, index_to_retrieve)

# Server processes the request
encrypted_response = server.answerRequest(request_client, client.public_key)

# Client decrypts the response
retrieved_value = client.decryptAnswer(encrypted_response)

# Verify correctness
print(f"Retrieved value: {retrieved_value}")
assert retrieved_value == server.database[index_to_retrieve], "PIR failed"
print("PIR test successful")

