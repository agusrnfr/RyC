import socket

UDP_IP = "127.0.0.1" # localhost
UDP_PORT = 5005 # non-privileged ports > 1023
MESSAGE = b"Long Live Taylor Swift!" # Must be bytes

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE.decode('utf-8'))

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))