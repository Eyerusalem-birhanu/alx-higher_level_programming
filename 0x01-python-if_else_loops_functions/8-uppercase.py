#!/usr/bin/python3
def uppercase(str):
        for c in str:
        if odr(c) >= 97 and odr(c) <= 123:
            c = chr(odr(c) - 32)
        print('{}'.format(c), end='')
    print('')
