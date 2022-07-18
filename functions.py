# FUNCTIONS
def multiply(x: float, y: float) -> float: # x, y = parameters
  """
    Multiply 2 numbers.
 
    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.
 
    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
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


# Palindrome function with annotation
def is_palindrome(string: str) -> bool: # function tyoe and return of the function
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
 

# function
def banner_text(text):
  screen_width = banner_width
  if len(text) > screen_width - 4:
    # crashes the program when text is too long
    raise ValueError("String {0} is larger than specified width {1}".format(text, screen_width))

  if text == "*":
    print("*" * screen_width)
  else:
    centered_text = text.center(screen_width - 4)
    output_string = "**{0}**".format(centered_text)
    print(output_string)

banner_width = input("Enter a banner width: ")
banner_text("*")
banner_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
banner_text("Maecenas ornare lacus lacus, vitae luctus enim ultricies auctor.")
banner_text("Ut eget sollicitudin nunc, quis mattis est. Morbi.")
banner_text("*")

# using a diferent parameter definition
def sum_numbers(*values: float) -> float:
  """ calculates the sum of all the numbers passed as arguments """
  result = 0
  for number in values:
    result += number
  return result


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
