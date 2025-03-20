import time
import matplotlib.pyplot as plt
from client import Client
from server import Server

# List of database sizes to test
db_sizes = list(range(10, 101, 10))  # Testing from 10 to 100 elements in steps of 10
client_times = []
server_times = []
num_tests = 5  # Run multiple tests for averaging

# Initialize client
client = Client(bits=1024)

for size in db_sizes:
    print(f"\nTesting with database size: {size}")

    # Initialize server with a database of the current size
    server = Server(db_size=size)

    # Choose a random index to retrieve
    index_to_retrieve = size // 2  # Picking a middle index for consistency

    # Measure client request time (averaged over multiple runs)
    client_total_time = 0
    for _ in range(num_tests):
        start_time = time.time()
        request_vector = client.request(size, index_to_retrieve)
        client_total_time += (time.time() - start_time)
    client_time = client_total_time / num_tests
    client_times.append(client_time)
    print(f"Client request time (average): {client_time:.6f} seconds")

    # Measure server processing time (averaged over multiple runs)
    server_total_time = 0
    for _ in range(num_tests):
        start_time = time.time()
        encrypted_response = server.answerRequest(request_vector, client.public_key)
        server_total_time += (time.time() - start_time)
    server_time = server_total_time / num_tests
    server_times.append(server_time)
    print(f"Server processing time (average): {server_time:.6f} seconds")

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(db_sizes, client_times, label="Client Execution Time", marker="o")
plt.plot(db_sizes, server_times, label="Server Execution Time", marker="s")

plt.xlabel("Database Size (Number of Elements)")
plt.ylabel("Execution Time (seconds)")
plt.title("PIR Performance: Client vs Server Execution Time")
plt.legend()
plt.grid()
plt.show()
