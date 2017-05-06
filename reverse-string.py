#!/usr/bin/python

#Different ways to print a string in reverse order of its characters

s = 'abc'

print s[::-1]

print ''.join(reversed(s))

print s[slice(None, None, -1)]

def reverse(string):
    n = len(string)
    new_string = ''

    for i in range(n-1, -1, -1):
        new_string += string[i]

    print new_string

reverse(s)