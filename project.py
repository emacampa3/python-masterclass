# Challenge: guessing game
import random

def get_integer(prompt):
  while True: # looping until user enters valid input
    temp = input(prompt)
    if temp.isnumeric(): # if input is a number, convert to int
      return int(temp) # executing return causes the while loop to stop
    print("{0} is not a valid number".format(temp)) # only exectues when invalid input is given


highest = 1000
answer = random.randint(1, highest)
print(answer)
guess = 0
print("Please guess number between 1 and 1000: ")

while guess != answer:
  guess = get_integer(": ")

  if guess == 0:  # player can exit the game
    break
  if guess == answer:
    print("You have guessed it")
    break
  else:
    if guess < answer:
      print("Guess higher")
    else:
      print("Guess lower")

# another function: returns the sum of all even or odd numbers up to the chosen input number
def sum_eo(n, t):
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))


x = sum_eo(11, 'o')
print(x)
