#!/usr/bin/python3
# Start with 'z' and go backwords to 'a'
for i in range(122, 96, -1):
    # Print alternating lowercase and uppercase
    if (122 - i) % 2 == 0:
        print(chr(i).lower(), end='')
    else:
        print(chr(i).upper(), end='')
