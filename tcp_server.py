import socket
import time

def start_server(host='0.0.0.0', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                # Send an immediate response
                immediate_response = b"Immediate Response"
                conn.sendall(immediate_response)
                print(f"Sent immediate response to {addr}: {data}")
                
                # Wait for 5 seconds
                time.sleep(5)
                
                # Send final response after 5 seconds
                final_response = b"Final Response after 5 seconds"
                conn.sendall(final_response)
                print(f"Sent final response to {addr}")

if __name__ == "__main__":
    start_server()
