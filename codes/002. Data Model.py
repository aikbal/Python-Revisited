#!/usr/local/bin/python
# coding: utf-8
# author: Asif

# Objects, values and types
a = 5 # 5 is stored in memory, a is an object which refers to the data.
b = 4+1 # another object
c=b # c is another object

print("a=b?:",a is b) # True
print("c=b?:",c is b) # True

print("a:",id(a),"\tb:",id(b))

b = 10

print("Is c changed when b is changed?:",c is b) # Immutable objects

x = [1,2]
y = x
y[1] = 0
print("x=y?:",x is y) # True, Mutable object

print(type(a))
print(type(x))
print(type(type(x))) # type() returns an object of class type

# *******************************************************************************
# The standard type hierarchy

print(None)

# Mutable sequence

l = [1,2,3]
l1 = l[1:] # Creates new data
m = l1

l1[0]=9

print(l,l1,m)

# Immutable sequence

t = (1,2,3) # can't be changed!

print(len(t)) # Sequences have a function len() which returns number of objects in it.

# Mutable set 

x = set([1,2,3,])
x.add(6)

# Immutable set

y = frozenset([1,2,3])

print(x,y)

# Mappings

d = {} 
d['key'] = 5
print(d)