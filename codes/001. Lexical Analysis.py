#!/usr/local/bin/python
# coding: utf-8
# author: Asif
# This is a comment
# First line is to specify which interpreter to use
# Second line is to declare the encoding type



print(1) # This statement ends with new line character

# Explicit line joining

print("Line 1 \
    Line 2") # This statement ends here!

# Implicit line joining
a = [ [1,2,3], # Line 1
      [4,5,6], # Line 2
      [7,8,9]]  # This statement ends here! These lines can have comments too!




# Above 4 lines are blank lines and ignored by the interpreter. It might include tab, space etc.

# Identifiers are unlimited in length. Case is significant.
jchgajhcgajcg = 5

# Keywords
print(True > False)

# Reserved classes of identifiers: * _

print( "String: ab\nc") # String
print(r"Raw String: ab\nc") # Raw string
print(f"formatted String: ab{jchgajhcgajcg}c")

print("Integer:",1)
print("Float:",2.5)
print("Imaginary:",6j)

# Operators
print(5+4)
