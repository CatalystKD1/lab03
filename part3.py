import math

def say_math(math_func, num, func):
  result = math_func(num)
  print("The result of " + func + " applied to " + str(num) + " is " + str(result))
say_math(math.sqrt, 9,"Square root")
say_math(math.modf, 100, "Mod F")
say_math(math.exp, 24, "EXP")