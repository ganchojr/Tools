import socket
import sys
from datetime import datetime
import subprocess

# Clear the screen
subprocess.call('clear', shell=True)

# Input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Banner
print()
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)
print()

# Check time started
t1 = datetime.now()


try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Checking time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total = t2 - t1

# Printing the information to screen
print("Scanning Completed in: ", total)
