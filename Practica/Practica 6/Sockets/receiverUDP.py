import socket

UDP_IP = "127.0.0.1" # localhost
UDP_PORT = 5005 # non-privileged ports > 1023

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data.decode('utf-8'))