import sys
from paramiko import RSAKey
from pssh.pssh_client import ParallelSSHClient
from pssh import utils
from pssh.exceptions import AuthenticationException, UnknownHostException, ConnectionErrorException

if len(sys.argv) < 2:
    print('Hostnames not given.')
else:
    utils.enable_host_logger()
    hostnames = sys.argv[1].split(',')

    while True:
        username = input('Enter username of all hosts: ')
        if not username:
            continue
        else:
            break

    password = input('Enter password of all hosts: ')

    client = ParallelSSHClient(hostnames, user=username, pkey=password)

    while True:
        try:
            command = str(input('> '))
            if command == 'done':
                exit()
            output = client.run_command(command, stop_on_errors=False)
            for hostname in output:
                for out in output[hostname]['stdout']:
                    pass
        except KeyboardInterrupt:
            pass
        except AuthenticationException:
            print('Authentication error')
        except UnknownHostException:
            print('Unknown host error')
        except ConnectionErrorException:
            print('Connection error')
