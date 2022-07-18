# Fibonacci sequence function
def fibonacci(n: int) -> int: 
  if 0 <= n <= 1:
    return n

  n_minus1, n_minus2 = 1, 0

  result = None
  for f in range(n - 1):
    result = n_minus1 + n_minus2
    n_minus2 = n_minus1
    n_minus1 = result

  return result


for i in range(36):
  print(i, fibonacci(i))
