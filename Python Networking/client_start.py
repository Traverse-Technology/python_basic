import socket

BUFFER_SIZE = 1024  # Packet size, 1024 is standard


def client_socket(tcp_ip, tcp_port):
    '''create_client socket'''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        # print(f'#<INFO> A client on: {addr} has connected.')
        print(f'#<INFO> Connected to server {tcp_ip}:{tcp_port}')
        sock.connect((tcp_ip, tcp_port))
        while True:
            message = input('Enter a message to send to the server: ')
            if message != "stop":
                sock.sendall(message.encode())
                data = sock.recv(BUFFER_SIZE)
                decoded_data = data.decode()
                print(f'#<INFO> Reply Received: {decoded_data}')
            else:
                print(f'#<INFO> Stop')
                break
                  

    # if you don't use "with" remember to close the socket


def main():
    tcp_ip = '127.0.0.1'  # IP address of server to connect to
    tcp_port = '5005'     # Port of server to connect to
    client_socket(tcp_ip, int(tcp_port))

    print('#<INFO> exiting...')


if __name__ == '__main__':
    main()