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
