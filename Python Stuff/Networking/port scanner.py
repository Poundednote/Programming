import socket
import sys


def scan_host(host, port, r_code=1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        code = s.connect_ex((host, port))

        if code == 0:
            r_code = code

        s.close()

    except Exception as e:
        pass

    return r_code


# Settings
host = ''
max_port = 5000
min_port = 1

try:
    host = input('Enter Host Address: ')
except KeyboardInterrupt:
    print('Keyboard Interrupt Exiting...')
    sys.exit(1)

hostip = socket.gethostbyname(host)
print(hostip)

for port in range(min_port, max_port):
    try:
        response = scan_host(host, port)
        print('scanning')
        if response == 0:
            print('Port %d: Open' % (port))

    except Exception as e:
        pass

input('...')
