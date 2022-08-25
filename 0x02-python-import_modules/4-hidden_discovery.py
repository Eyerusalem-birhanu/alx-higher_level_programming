#!usr/bin/python3

if __name__ == '__main__':
'''print all names defined by hidden_4 module'''
imprt hidden_4

names = dir(hidden_4)
for name in name:
if name[:2] != '__':
print(name)
