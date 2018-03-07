# coding: utf-8

# 这个例子要在命令行里输入并带参数，如：python ex14.py Kenny
from sys import argv

script, user_name = argv
prompt = '> '
print('Hi %s, I\'m the %s' %(user_name, script))
print('I\'d like to ask you a few questions.')
print('Do you like me %s' % user_name)
likes = input(prompt)

print('Where do you like %s' %user_name)
lives = input(prompt)

print('What kind of computer do you have?')
computer = input(prompt)

print('''
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice
''' %(likes, lives, computer))
