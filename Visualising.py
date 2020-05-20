import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import socket
import struct
from si_prefix import si_format

def direction():
    # Code copied from: https://wiki.python.org/moin/UdpCommunication
    UDP_IP = "127.0.0.2"
    UDP_PORT = 5000
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    # End of copied code
        print("Data: ", float(data))
        #print("Direction data: ", a[0])
        return float(data)
"""
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
        return a[0]
        """

def frequency():
    # Code copied from: https://wiki.python.org/moin/UdpCommunication
    UDP_IP = "127.0.0.2"
    UDP_PORT = 5000
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1472) # buffer size is 1024 bytes
    # End of copied code
        a = struct.unpack_from('f', data)
        return a[0]
        
def main():

    dir1 = direction()
    print("Direction aquired: ", dir1) 
    if dir1 <= 181:
        freq = frequency()
        dir_rad = np.radians(dir1)
        print("Direction: ", dir1)
        print('Frequency: ', freq)
        color1 = 'white'
        color2 = 'red'
    else:
        dir_rad = 0
        freq = 0
        color1 = 'black'
        color2 = 'black'


    matplotlib.rcParams['figure.figsize'] = (8,4.5)
    plt.style.use('dark_background')
    ax1 = plt.subplot(111, projection='polar')
    ax1.set_rmax(1)
    ax1.set_thetamin(0)
    ax1.set_thetamax(180)
    ax1.text(2.45, 1.6, round(dir1), style='italic', 
        bbox={'facecolor': color2, 'alpha': 1, 'pad': 10})
    ax1.plot([0,dir_rad], [0,1], color = color1, linewidth=5.0)
    plt.show(block=False)
    plt.pause(0.001)
    plt.clf()

while __name__ == "__main__":
    main()
