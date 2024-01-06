# 001. Lexical Analysis
## Environment Decleration
> #!/usr/local/bin/python
## Text Encoding Decleration
> #coding: utf-8
## Comments
> Starts with # and ends with new line character
## Implicit Line Joining
> Expressions in parentheses, square brackets or curly braces can be split over more than one physical line without using backslashes. 
## Explicit Line joining
> Two or more physical lines may be joined into logical lines using backslash characters (\)


# Data Model
## Objects, values and types
> Data is stored in memory, In python it is represented by objects or by relation between objects. 'is'operator compares the identity of two objects, id() functions returns an integer representing its identity. We can think it as an address to the memory location where it is stored.
> Mutable objects can be changed, e.g. list, immutable objects can't be changed, e.g. int.
## The standard type hierarchy
> None is used to signify the absence of a value in many situations.
> numbers.Number : Created by numeric literals
>> numbers.Integral : int,bool
>> numbers.Real : float
>> numbers.Complex : complex
> Sequences : These represent finite ordered sets
>> Immutable sequences: String,tupples,bytes
>> Mutable sequences: List,Byte Arrays
>> sequence objects can be aaccessed by the index : a[i]
>> Sub sequence can be sliced from a sequence: a[i:i+j] 
> Sets : These represent unordered, finite sets of unique, immutable objects.
>> len() returns number of items in it, similaar to sequences
>> Mutable sets are created by constructor set(), Immutabble sets are created by frozenset()
> Mapping : Maps a key to an object e.g. Dictionary. Keys can't be mutable.
