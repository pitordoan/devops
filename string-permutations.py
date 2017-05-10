#!/usr/bin/python

from sets import Set

def find_permutation(string):
    if len(string) <= 1:
        return string

    perms = Set()

    for c in string:
        re_perms = find_permutation(string.replace(c, '', 1))
        for perm in re_perms:
            perms.add(c + perm)

    return list(perms)

s = 'abc'
print find_permutation(s)