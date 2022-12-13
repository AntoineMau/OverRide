#!/usr/bin/python

import sys

login = sys.argv[1]
login_serial = (ord(login[3]) ^ 0x1337) + 0x5eeded
for char in login:
    login_serial += (ord(char) ^ login_serial) % 0x539
print(login_serial)
