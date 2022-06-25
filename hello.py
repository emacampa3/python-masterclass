#\n forces a new line, \t forces a tab (space)
#print(type(age)) prints the type of a variable ‘age’
#backslash = option + ž
#integer = whole number with no fractional part
#float = number with fractional part after decimal point

from calendar import MONDAY


greeting = 'Hello'
name = input('What is your name')
print(greeting + '' + name)

a=12
b=3
print(a*b)
print(a/b) # result is a float 4.0
print(a//b) # integer division, rounded down towards minus infinity: result is 4, an integer
print(a%b) # the reminder after integer division: result is 0

# program that returns an error
first_name = "John"
last_name = "Cleese"
age = 78
print(first_name + last_name + age) # numerical values cannot be added to strings

for i in range(1, 4):
  print(i) # result is 1, 2, 3, without number 4

# SLICING
home = "ljubljana"
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

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5]) # returns: MTWTFSS, as it slices to every fifth character

# all print the same output, extracting only the digits
data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[0:-1:5]) 
print(data[:-1:5]) 
print(data[::5]) 

flower = "blue violet" 
print('blue' in flower) # returns True

# SEQUENCE OPERATORS (string, list, tuple, range, byte/bytearray)
# string (can be used with + operator, star operator repeats a sequence a certain number of times)
# print("hello" * 5) prints hello 5 times
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

# f-string
name = "Ema"
name2 = "Branko"
print(name + f"loves {name2}") # returns: Ema loves Branko

flower = "rose"
colour = "red"
print("The {0} is {1}".format(flower,colour)) # prints: The rose is red

# code block = indented line
# = is used for assigning values to variables, == is used for testing equality

# IF STATEMENTS
# getting a number from the user
age = int(input("How old are you?")) # expects an integer 'int'
if age >= 18: 
  print("You are old enough to vote")
elif age == 900: # if age is equal to 900, the condition evaluates as true
  print("Sorry, Yoda, you dided in Return of the Jedi")
else: 
  print("Please come back in {0} years".format(18-age))

# guess the number: outputs are different, depending on the user input
answer = 5
print("Please guess number between 1 and 10: ")
guess = int(input()) # input is converted to an integer
if guess != answer: # guess is not equal to the answer
  if guess < answer:
    print("Please guess higher")
  else: # guess must be grewater than answer
    print("Please guess lower")
  guess = int(input()) # allows for another guess
  if guess == answer:
    print("Well done, you guessed it")
  else: 
    print("Sorry, you have not guessed it correctly")
else:
  print("You got it first time")

# conditions (and, or)
age = int(input("How old are you? "))
if 16 <= age <= 65: 
# if 16 < age < 65: if any of the conditions is true, tit will be evaluated to True: if age is less than 16, program does not have to check if is it also greater than 65
  print("Have a good day at work")
else:
  print("Enjoy your free time")

print("-" * 80) # prints 80 lines

# TRUE/FALSE
# FALSE: none, any type of 0, empty sequences
if 0: # 0 evaluates True
  print("True") # cannot be executed
else: 
  print("False") # returns False, as 0 can never be True

name = input("Please enter your name: ")
if name: # if name input is true (the name was given), this line evaluates to true and executes
# if name != "": another way of checking the input
  print("Hello, {}".format(name))
else: # no name input was given
  print("Are you the man with no name?")

# CHECKING IF SOMETHING IS IN THE SEQUENCE
parrot = "Norwegian Blue"
letter = input("Eneter a character: ") # also applies to words, is case sensitive
if letter in parrot:
  print("{} is in {}".format(letter, parrot))
else:
  print("The letter is not i n {}".format(parrot))

# when comparing string, .casefold() is useful, as it transforms the letters to lowercase

# FOR LOOPS
# for loop that prints out all the capital letters in quote 
quote = """Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads, the Fresh-Water System, and Public Health, what have the Romans ever done for us?"""
for char in quote:
    if char.isupper():
        print(char)

# iterating over a range (does not include the stop value)
for i in range(0,10):
    print("{}".format(i)) # prints the number from 0 to 9

# starts at 0, up to 9
for i in range(10):
  print("{}".format(i))

# values from 0 to 100, in steps of 7 (also all the printed numbers are divisible by 7)
for i in range(0, 100, 7):
  print("{}".format(i))
