import socket
import time

def start_server(host='0.0.0.0', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")

        while True:  # Keep the server running indefinitely
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if data:
                    # Send an immediate response
                    immediate_response = b"Immediate Response"
                    conn.sendall(immediate_response)
                    print(f"Sent immediate response to {addr}")

                    # Wait for 5 seconds
                    time.sleep(5)

                    # Send final response after 5 seconds

                    final_response = b"Final Response after 5 seconds"
                    conn.sendall(final_response)
                    print(f"Sent final response to {addr}")
                else:
                    print(f"No data received from {addr}, closing connection")

if __name__ == "__main__":
    start_server()
