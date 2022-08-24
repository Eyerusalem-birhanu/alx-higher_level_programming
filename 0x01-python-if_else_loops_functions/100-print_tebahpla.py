#!/usr/bin/python3
'''print the alphabet in reverse order alterning upper and lowe case'''
i = 0
for c in range(odr('z'), odr('a') - 1, -1):
    print('{}'.format(chr(c - i)), end='')
    i = 32 if i == 0 else 0
