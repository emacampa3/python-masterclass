greeting = 'Hello'
name = input('WHat is your name')

#\n forces a new line, \t forces a tab (space)
#print(type(age)) prints the type of a variable ‘age’
#backslash = option + ž
#integer = whole number with no fractional part
#float = number with fractional part after decimal point

print(greeting + '' + name)

a=12
b=3
print(a*b)
print(a/b) # result is a float 4.0
print(a//b) # integer division, rounded down towards minus infinity: result is 4, an integer
print(a%b) # the reminder after integer division: result is 0

for i in range(1, 4):
  print(i) # result is 1, 2, 3

home = "ljubljana"

# SLICING
print(home[2]) # returns the third letter
print(home[-1]) # returns the last letter
# negative index: last letter is index -1, not index 0

print(home[0:5]) # return characters, start at position 0 up to, not including, position 2
print(home[:5]) # the same result

print(home[3:]) # starts at index 3 up to the last index
print(home[:]) #returns a complete string

print(home[-5:-3]) # returns lj
print(home[-5:7]) # returns lj: starts at index -4 and then to positive index 7 (not including)

print(home[0:6:3]) # returns lbn: forst 6 letters, but every third
# 0 = start value, 6 = stop value (doesn't inlcude the 7th letter), 3 = step

number = 123456789
print(number[1::4]) # returns: 26 (starts at the position 1 and slices every 4th character)

#BACKWARDS: reversing the sequence (start value must be greater than the stop value)
print(home[9:0:-1])  #returns a reverse order: anajlbuj DOES NOT INCLUDE THE FIRST LETTER L
print(home[9::-1]) # IS EQUAL TO: print(home[::-1]) ommiting a stop value: includes letter L: returns a whole word in reversed order

# the last 4 letters of the sequence in correct order
print(home[-4:])
# returns the last item
print(home[-1:])
# returns the first letter in a sequence
print(home[:1]) # is equal to print(home[0]), but returns an error, if string is empty (while the first option still passes)

# SEQUENCE OPERATORS (string, list, tuple, range, byte/bytearray)
# string (can be used with + operator, star operator repeats a sequence a certain number of times)
print("hello" * 5) # prints hello 5 times
# list & tuple can also be multiplied

# curly brace is replaced with the first value in the format list, age
age = 22
print("My age is {0} years".format(age)) # returns: My age is 22 years
print("There are {0} days in {1}, {2} and {3}".format(31, "Jan", "Mar", "May")) # There are 31 days in Jan, Mar and May
# 4 replacement fields (first value goes into {0}, second to {1} and so on)
print("There are {0} days in Jan, Mar and May".format(31)) # the same output

print((""" bla """)) # text between tripple quotes will return the exact replica of the placement

# returns list of 13 numbers, their squared and cubed versions
for i in range(1, 13):
  print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3)) # double asterix means: power to, ':2' or ':4' is formating strings to align nicer

for i in range(1, 13):
  print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3)) # '<' aligns the return values to the left

print("{0:12}".format(22 / 7)) # default: prints 15 decimals
print("{0:12f}".format(22 / 7)) # specifying float value: 6 digits affter decimal point
print("{0:12.50f}".format(22 / 7)) # still specifying float value, with precision of 50: 50 points after decimal point
# '12' is a field width


