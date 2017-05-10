#!/usr/bin/python

mylist = ['', 'one', '', '', 'two', 'three']

#Below are ways to re-create a new list/generator that contains only elements with values not blanks.

#list comprehension
newlist = [ele for ele in mylist if ele != '']
print newlist

#generator comprehension
mylist_gen = (ele for ele in mylist if ele != '')
print ', '.join(mylist_gen)

#old school way
newlist2 = []
for ele in mylist:
    if ele != '':
        newlist2.append(ele)
print newlist2
