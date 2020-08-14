######################################################################################
# Script Name: listComprehension                                                     #
# Description: This script will print the user executing the program and will also   #
#              keep checking the current system processes running at the moment.     #
# Version    : 1.0                                                                   #
######################################################################################

## Old method of creating list out of a string ##
mylist = 'Hello'
newlist = []

for letter in mylist:
    newlist.append(letter)

print(newlist)

## List comprehension in python to replicate the above behaviour ##

mystring = 'Hello'

mylist_n = []

mylist_n = [letter for letter in mystring]

print (mylist_n)

## enumerate example

mystr = 'Hello World'

for index,item in enumerate(mystr):
    print(index, item)


mylist = [x for x in range(0,11)]
print (mylist)

mylist = [x for x in range(0,11) if x%2 == 0]
print (mylist)
