# coding: utf-8
from sys import argv

script, fileName = argv
txt = open(fileName)

print('Here\'s your life %r:' % fileName)
print(txt.read())

print('Type the filename again:')
fileAgain = input('> ')
txtAgain = open(fileAgain)

print(txtAgain.read())