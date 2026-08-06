import socket
import datetime

def start_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind(("127.0.0.1", 2222))
        server.listen(5)
        print("Honeypot is listening on port 2222......")

        while True:
            client, addr = server.accept()
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with open("attack_logs.txt", "a") as f:
                f.write(f"{timestamp} - IP: {addr[0]} tried to access port 2222\n")
            
            print(f"Attack detected from: {addr[0]}")
            client.close()
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.close()

if __name__ == "__main__":
    start_honeypot()