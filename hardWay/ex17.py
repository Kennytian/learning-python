# conding: utf-8

from sys import argv
from os.path import exists

script, fromFile, toFile = argv

print('Copying form %s to %s' %(fromFile, toFile))

# we could to these two on one line too, how?
input = open(fromFile)
inData = input.read()

print('The input file is %d bytes long' % len(inData))

print('Does the output file exist? %r' % exists(toFile))
print('Ready, hit RETURN to continue, CTRL-C to abort.')

input()

output = open(toFile, 'w')
output.write(inData)

print('Alright, all done.')
output.close()
input.close()
