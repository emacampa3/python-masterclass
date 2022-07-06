#\n forces a new line, \t forces a tab (space)
#print(type(age)) prints the type of a variable ‘age’
#backslash = option + ž
#integer = whole number with no fractional part
#float = number with fractional part after decimal point

from calendar import MONDAY
from functools import partial


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
  print("Sorry, Yoda, you died in Return of the Jedi")
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

# NESTED FOR LOOP: multiplication table (12x12)
for i in range(1,13):
  for j in range(1,13):
    print("{0} times {1} is {2}".format(j, i, i * j))

# list = ordered sequence of values, in square brackets
shopping_list = ["milk", "pasta", "eggs"]
# prints all items, except for bread
for item in shopping_list:
  if item == "bread":
    continue # causes all the remaining code in the block to be skipped
    # break (instead of continue) after its execution causes the loop to stop: useful, when searching for an item
  print("Buy" + item)

#searching for an item in range
shopping_list = ["milk", "bread", "pasta", "eggs"]
item_to_find = "pasta"
found_at = None # constant, that shows that something does not have a value

for index in range(len(shopping_list)):
  if shopping_list[index] == item_to_find:
    found_at = index
    break

# if item_to_find in shopping_list:
#   found_at = shopping_list.index(item_to_find)
  
if found_at is not None: # if item is found
  print("Item found at position {}".format(found_at)) # Item found at position 2
else: # if item is not found
  print("{} not found".format(item_to_find))

# WHILE LOOPS
# iterating over the numbers
i = 0
while i < 10: # while condition is true, execute this block
  print("{}".format(i))
  i += 1

# if input equals to an item in the list, loop breaks
available_exits = ["n", "s", "e", "w"]
chosen_exit = ""

while chosen_exit not in available_exits: # requests an item for as long as input is false
  chosen_exit = input("Please choose a direction: ")
  if chosen_exit.casefold() == "quit":
    print("Game over")
    break

else:
  print("aren't you glad you got out of there")

# prints the numbers from 0 to 20 that arent divisible by 3 or 5
for i in range(21):
    if i%3 == 0 or i%5 == 0:
        continue
    print(i)

import random
highest = 10
answer = random.randint(1,highest) # function in random module (generates a random number within the range)
print(answer) # only for testing
guess = 0 # initialise to any number, that does not equal the answer
print("Please guess number between 1 and {}".format(highest))

while guess != answer: # loops until guess equals the answer
  guess = int(input())

  if guess == 0: # player can exit the game
    break
  if guess == answer:
    print("You have guessed it")
    break
  else:
    if guess < answer:
      print("Guess higher")
    else: 
      print("Guess lower")

# splitting the code: "", ENTER, ""

# BINARY SEARCH: to guess a number between 1 and 1000, with halving the guesses, 10 guesses are needed (1000, 500, 250 or 750 and so on)
low = 1
high = 1000
print("Please think of a number between {} and {}".format(low,high))
input("Press ENTER to start")

guesses = 1
while low != high: # continue looping as long as this is True (when they are equal: correct number is found, the loop will terminate)
  guess = low + (high - low) // 2 # calculates the mid point between the lowest and highest value
  high_low = input("My guess is {}. Should I guess higher or lower? Enter h or l, or c, if my guess was correct ".format(guess).casefold())
 
  if high_low == "h": # guess higher
    low = guess + 1
  elif high_low == "l": # guess lower
    high = guess - 1
  elif high_low == "c":  
    print("I got it in {} guesses".format(guesses))
    break
  else: 
    print("Enter h, l or c")

  guesses *= 1
else: # runs when loop is terminated normally
  print("You though of the number {}".format(low))
  print("I got it in {} guesses".format(guesses))

# AUGMENTED ASSIGNMENT
greeting = "Good "
greeting += "morning "
greeting *= 5
print(greeting) # prints Good morning 5 times

# 5 * 8: adding 5 eight times
multiplier = 8
answer = 0
for i in range(multiplier):
  answer += number
print(answer)

numbers = [1, 45, 32, 12, 60]
for number in numbers:
  if number % 8 == 0: # reject if exactly divisible by 8
    print("numbers are unacceptable")
    break
else: # result if the loop terminates nrormally (if the loop is terminated before, this does not run)
  print("numbers are fine")

# Challenge
choice = None

while choice != "0":
  if choice in "12345":
    print("You choose {}".format(choice))
  else:
    print("Please chose your option from the list below:")
    print("1:\tLearn Python")
    print("2:\tLearn Java")
    print("3:\tGo swimming")
    print("4:\tHave dinner")
    print("5:\tGo to bed")
    print("0:\tExit")

  choice = input()

# Program, that prints out the even numbers from 0 to 20 (inclusive)
for value in range(11):
  value *= 2
  print(value)

# more efficient
for value in range(0,21,2):
  print(value)

for x in range(30):
  if x % 3 == 0 or x % 5 == 0:
    continue
  print(x)

# the same output
for x in range(30):
  if x % 3 != 0 and x % 5 != 0:
    print(x)

# LIST
computer_parts = ["monitor", "keyboard", "mouse"]
for part in computer_parts:
  print(part)

print(computer_parts[0:3]) # slicing a list produces another list

# immunable types: int, float, bool, str, tupple, bytes, frozen set (values cannot be changed)
# mutable objects: list, dict, set, bytearray (values can be changed)
# adding an item to the shopping list: 
shopping_list += ["cookies"]
shopping_list.append("cream") 

print("mississippi".count("s")) # 4: string 's' appears 4 times


available_parts = ["keyboard", "monitor", "mouse"]
# created an empty list, add valid choices to that list
valid_choices = []
for i in range(1, len(available_parts) + 1): # output are indexes of parts + 1
  valid_choices.append(str(i))
print(valid_choices) 

current_choice = "-"
computer_parts = [] # new empty list, that will contain the parts added to the list
while current_choice != 0:
  if current_choice in valid_choices:
    index = int(current_choice) - 1
    chosen_part = available_parts[index]
    # if part is already in list, remove it
    if chosen_part in computer_parts:
      print("Removing {}".format(current_choice))
      computer_parts.remove(chosen_part)
    else:
      print("Adding {}".format(current_choice))
      computer_parts.append(chosen_part)
    print("Your list now contains: {}".format(computer_parts))
  else: 
    print("Please add options from the list below:")
    for number, part in enumerate(available_parts): # returns a pair of values (index position = number and value of the item = part)
      print("{0}: {1}".format(number + 1, part))
  
  current_choice = input()

print(computer_parts)


for index, character in enumerate("abcdef"):
  print(index, character) # index numbers match the characters

# Challenge: sort data into two lists
data = [
  "Andromeda - Shrub",
  "Bellflower - Flower",
  "China Pink - Flower",
  "Daffodil - Flower",
  "Evening Primrose - Flower",
  "French Marigold - Flower",
  "Hydrangea - Shrub",
  "Iris - Flower",
  "Japanese Camellia - Shrub",
  "Lavender - Shrub",
  "Lilac - Shrub",
  "Magnolia - Shrub",
]

flowers = []
shrubs = []

for plant in data:
  if "Flower" in plant:
    flowers.append(plant)
  else:
    shrubs.append(plant)

even = [2,4,6,8]
odd = [1,3,5,7,9]
even.extend(odd) # adding odd to even
even.sort(reverse=True) # without condition, list is ascending sorted 
print(even)

pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram, key=str.casefold) # case insensitive sort
print(letters) # returns the list with alphabetically sorted items

numbers = [2.3, 4.5, 8.7, 3.1, 9.1, 1.6]
sorted_numbers = sorted(numbers) # returns a new list list (original list is not altered)
print(sorted_numbers)
numbers.sort() # the same sorted output, but returns an original sorted list
# another_sorted_numbers = numbers.sort() function 'sort' does not return anything:assigning sort method to a variable is a no go: another_sorted_numbers returns None
print(numbers)

names = ["Graham", "john", "Emma", "eric", "Terry", "Marco"]
names.sort(key=str.casefold)
print(names)

empty:list = []
even = [2,4,6,8]
odd = [1,3,5,7,9]
numbers = even + odd 
sorted_numbers = sorted(numbers) # ordered list of ints
digits = sorted("23462046") # returns a list of strings (digits): sorting a string results in list of sorted strings
digits = list("23462046") # returns an unsorted list of strings
more_numbers = numbers[:] # duplicating an existing list by slicing it
more_numbers = numbers.copy() # copying the numbers list

computer_parts = ["monitor", "mouse", "keyboard"]
computer_parts[1] = "computer" # replaces the 2nd item 
computer_parts[3:] = ["computer"] # must be a list

date = [42,45,17,143,544,76,22,42,5325,813,68674,34,142,5254,6,775]
min_valid = 10
max_valid = 300

# process the low values
stop = 0
for index, value in enumerate(data):
  if value >= min_valid:
    stop = index
    break
print(stop)
del data[:stop]
print(data)

# process the high values
start = 0
for index in range(len(data) - 1, -1, -1): # range starting at the end, up to the first value at position 0 (since stop value is not included, -1), step of -1: backwards
  print(index) # checking to see if positions are correct
  if data[index] <= max_valid: # returns a start value, equal to the position to the last item, we still want to keep
    start = index + 1 
    break
print(start)
del data[start:]
print(data)

# removing rouge values by iterating backwards
data = [104, 101, 4, 308, 103, 5, 107, 100, 306, 124]
min_valid = 100
max_valid = 200

for index in range(len(data) -1, -1, -1):
  print(index) # indexes of the numbers in reverse order
  if data[index] < min_valid or data[index] > max_valid:
    print(index, data) # index of rouge numbers
    del data[index]
print(data) # only the correct values

# another version
top_index = len(data) -1 # index of the last item in array
for index, value in enumerate(reversed(data)):
  if value < min_valid or value > max_valid:
    print(top_index - index, value) # values with indexes in reversed order
    del data[top_index - index]

empty_list = []
even = [2,4,6,8]
odd = [1,3,5,7,9]
numbers = [even, odd] # a list containing two lists
print(numbers)

for number_list in numbers:
  print(number_list) # prints both lists: number_list is an item in array, that is also a list

  for value in number_list:
    print(value) # prints all values inside each lsit

# menu is a nested list, containing meals with spam; Challenge: print meals with spam removed
menu = []

for meal in menu:
  if "spam" not in meal:
    print(meal)
  else:
    meal.remove("spam")
    print(meal)

# the same result
for meal in menu:
  for item in meal:
    if item != "spam":
      print(item , end=" ") # provides space between items 
  print() # new line for meals

# the same result
for meal in menu:
  for index in range(len(meal) -1, -1, -1):
    if meal[index] == "spam":
      del meal[index]
  print(meal) 

name = "Ema"
age = 22
print(name, age) # Ema 22: sep default is space
print(name, age, sep=", ") # Ema, 22

# all the items inside an array must be strings
flowers = [ "daffodil", "primrose", "hydrangea", "iris", "lavender", "sunflower", "lily"]
separator = ", "
output = separator.join(flowers) # joins the flowers into a single string, separating them with comma
print(output)
# the same result
print(", ".join(flowers))

for meal in menu:
  for index in range(len(meal) -1, -1, -1):
    if meal[index] == "spam":
      del meal[index]
  print(", ".join(meal)) # items of each meal are printed on the same line, separated with comma

panagram = "The quick fox jumps over the lazy dog"
words = panagram.split() # list, containing the words in the string
print(words)

numbers = "843.393.919.920"
print(numbers.split(".")) # ["843", "393", "919", "920"]

values_list = ["843", "393", "919", "920"]
for index in range(len(values_list)): # list of ints rather than strings, using for loop
  values_list[index] = int(values_list[index])
print(values_list) # from ["843", "393", "919", "920"] to [843, 393, 919, 920]

# another method
integer_values = []
for value in values_list:
  integer_values.append(int(value)) # converting to an int and appending to new list
print(integer_values)

# Challenge
user_input = input("Please enter three numbers: ")
split_string = user_input.split(",")

# Convert the split_string into integers
int_list = []
for ss in split_string:
    int_list.append(int(ss))

# Calculate the result: a + b - c
result = int_list[0] + int_list[1] - int_list[2]
print(result)

# TUPLES: does not support item assignment (immutable), use less memory
name = "Ema"
age = 22
print(name, age) # Ema 22
print((name, age)) # tuple: ("Ema", 22)

metallica = "Ride the Lightning", "Metallica", 1984
print(metallica[1]) # Metallica

metallica2 = list(metallica)
print(metallica2) # returns a list with items inside a tuple, items can be changed
