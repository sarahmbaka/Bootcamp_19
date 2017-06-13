def fizz_buzz(num):
  if num % 5 == 0:
    if num % 3 == 0:
      return "FizzBuzz"
    return "Buzz"
  elif num % 3 == 0:
    return "Fizz"
  return num
