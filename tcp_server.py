import socket
import time

def start_server(host='0.0.0.0', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        
        while True:  # Keep server running
            conn, addr = s.accept()  # Accept client connection
            print(f"Accepted connection from {addr}")

            with conn:
                try:
                    data = conn.recv(1024)  # Receive data from client
                    if data:
                        print(f"Received data from {addr}: {data.decode()}")

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
                        print(f"No data received from {addr}")
                except Exception as e:
                    print(f"Error occurred with connection from {addr}: {e}")

if __name__ == "__main__":
    start_server()
