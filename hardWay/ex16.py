# coding: utf-8
from sys import argv

script, fileName = argv

print('We\'re going to erase %r.' % fileName)
print('If you do not want that, hit CTRL-C(^C).')
print('If you do want that, hit RETURN.')

input('?')

print('Opening the file...')
target = open(fileName, 'w')

print('Truncating the file. Goodbye!')
target.truncate()

print('Now I\'m going to ask you for three lines.')

line1 = input('line 1:')
line2 = input('line 2:')
line3 = input('line 3:')

print('I\'m going to write these to the file.')

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print('And finally, we close it.')
target.close()