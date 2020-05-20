import numpy as np
import socket
import struct
from si_prefix import si_format
from scipy import stats

def direction_get():
    # Code copied from: https://wiki.python.org/moin/UdpCommunication
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1472) # buffer size is 1024 bytes
    # End of copied code
        a = struct.unpack_from('f', data)
        print("Direction data recieved: ", a[0])
        return a[0]

def direction_send(data):
    data1 = str(data)
    # Parts of code copied from: https://wiki.python.org/moin/UdpCommunication
    UDP_IP = "127.0.0.2"
    UDP_PORT = 5000
    MESSAGE = bytes(data1, encoding = 'utf-8')

    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    # End of copied code

def magnitude():
    # Code copied from: https://wiki.python.org/moin/UdpCommunication
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5006
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1472) # buffer size is 1024 bytes
    # End of copied code
        a = struct.unpack_from('f', data)
        print('Magnitude data: ', a[0])
        return a[0]

def error_handler(temp1):

    a = np.correlate(temp1,temp1)
    b = int(a[0]/sum(temp1) )
    tolerance = 10 # How many degrees is the tolerance rate
    b1 = b - tolerance
    b2 = b + tolerance
    n = 0
    for i in temp1:
        if b1 <= i <= b2:
            i = i
        else:
            temp1[n] = b
        n = n + 1
    return np.radians(temp1)


def main():
    dir1 = np.round(np.degrees(direction_get()))/2 
    mag = magnitude()
    data = np.loadtxt('directions.txt')
    print("Text loaded")
    no_signal = 255 # random number over 180 is sent to identify that there is no signal present
    if mag >= 1:
        while len(data) < 10:
            with open('directions.txt', 'a') as dirfile:
                dirfile.write("{}\n".format(str(dir1)))
        else: 
            with open('directions.txt', 'a') as dirfile:
                dirfile.write("{}\n".format(str(dir1)))
            yes_signal = error_handler(data)
            direction_send(yes_signal[0])
        print("Positive packet sent")
    else:
        with open('directions.txt', 'w') as dirfile:
            dirfile.write("{}\n".format(str()))
        direction_send(no_signal)
        print("Negative packet sent")

while __name__ == "__main__":
    main()
