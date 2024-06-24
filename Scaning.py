import socket
import sys
import time


usage = ("python3 Scaning.py <TARGET> <START_PORT> <END_PORT>")

print("/" * 100)

if (len(sys.argv) != 4):
    print("Bhaie arugment full fill kar ,Ek bar usage dekha le......./n", usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])

except socket.gaierror:
    print("Sorry bhaie! Domain ka ip nhi mila.....")
    sys.exit()

start_port = (int(sys.argv[2]))
end_port = (int(sys.argv[3]))

print("Scanning Ka Kam Chalu Hai", target)

for port in range(start_port, end_port + 1):

    print("Scanning PORT", port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target, port))  # using _ex because it will not terminate.
    if (not conn):
        print("PORT {} is OPEN".format(port))  
    s.close()
