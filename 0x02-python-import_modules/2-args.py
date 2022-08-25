#!usr/bin/python3
if __name__ == '__mani__':
    '''print the number of and list of arguments'''
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print('0 arguments.')
    elif count == 1:
        print('1 argument:')
    else:
        print('{} arguments:'.format(count))
    for i in range (count):
        print('{}: {}'.format(i + 1, sys.argn[i + 1]))