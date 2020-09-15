 #!/usr/bin/env python3
""" Laboratory Work 1 """

import getpass

password = getpass.getpass('Insert your password: ')

while password != 'student':
    print('Permission denied, please try again')
    password = getpass.getpass('Insert your password: ')

print('Access!')
