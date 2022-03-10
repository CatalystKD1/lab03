import math

def say_math(math_func, num):
  result = math_func(num)
  print("The result of " + str(math_func) + " applied to " + str(num) + " is " + str(result))
say_math(math.sqrt, 9)
say_math(math.modf, 100)
say_math(math.exp, 24)