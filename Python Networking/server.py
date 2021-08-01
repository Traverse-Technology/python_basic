import socket

TCP_PORT = 5005     # The port to use.
BUFFER_SIZE = 1024  # Packet size - 1024 is standard.


def server_socket(tcp_ip, tcp_port):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # bind the socket to the tcp address and port and start to listen
        sock.bind((tcp_ip, tcp_port))
        sock.listen()
        print(f'#<INFO> Server Initialising on {tcp_ip}:{tcp_port}')
        print('#<INFO> Awaiting connection...')
        tcp_ip = socket.gethostbyname(socket.gethostname())
        print(f'TCP IP is {tcp_ip}')
        # wait for a client to connect
        conn, addr = sock.accept()
        print(f'#<INFO> A client on: {addr} has connected.')
        # process all incoming data from the client....
        while True:
            data = conn.recv(BUFFER_SIZE)
            message = input('Enter a message to send to the client: ')
            if data:
                print(f'#<INFO> Received: {data.decode()}')
                # send a confirmation to the client
                conn.sendall(f'Server: {message}'.encode())
                # conn.sendall('Got that thanks!'.encode())
            else:
                print('#<INFO> End of Data - Socket Exiting...')
                break

        conn.close()
        

def main():
    tcp_ip = socket.gethostbyname('localhost')
    server_socket(tcp_ip, TCP_PORT)


if __name__ == '__main__':
    main()