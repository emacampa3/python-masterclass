# FUNCTIONS
def multiply(x, y): # x, y = parameters
  result = x * y
  return result

# function call
answer = multiply(10.5, 4) # 10.5, 4 = arguments
print(answer)

for val in range(1,5):
  two_times = multiply(2, val)
  print(two_times) # multiplying the values from 1 to 4 with 2

# Challenge: palindrome
def is_palindrome(string):
  # reversing the original string, checking, if reversed string equals original: evaluates to True or False
  return string[::-1].casefold() == string.casefold()

word = input("Enter a word to check: ")
if is_palindrome(word):
  print("'{}' is a palindorme".format(word))
else:
  print("'{}' is not a palindorme".format(word))


# another function
def palindrome_sentence(string):
  return string[::-1].casefold().isalnum() == string.casefold().isalnum()


word = input("Enter a sentence to check: ")
if palindrome_sentence(word):
  print("'{}' is a palindorme".format(word))
else:
  print("'{}' is not a palindorme".format(word))

# another version of the same function
def palindrome(sentence):
  string = ""
  for char in sentence:
    if char.isalnum():
      string += char
  # return string[::-1].casefold() == string.casefold()
  return is_palindrome(string) # referring to already writen function

word = input("Enter a sentence to check: ")
if palindrome(word):
  print("'{}' is a palindorme".format(word))
else:
  print("'{}' is not a palindorme".format(word))
 

