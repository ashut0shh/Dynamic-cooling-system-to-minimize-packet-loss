import socket
import time

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('<raspberry_pi_ip>', 5005)  # Replace with your Raspberry Pi's IP address

try:
    while True:
        # Send a packet
        message = "Hello, Raspberry Pi!"
        client_socket.sendto(message.encode(), server_address)
        print(f"Sent packet: {message}")

        # Wait for a second before sending the next packet
        time.sleep(1)  # Adjust the interval as needed

except KeyboardInterrupt:
    print("Client stopped.")
finally:
    client_socket.close()
