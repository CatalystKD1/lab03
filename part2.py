import math

def quadratic(a, b, c):
  x1 = (-b + math.sqrt(b**2 - 4*a*c) ) / (2*a)
  x2 = (-b - math.sqrt(b**2 - 4*a*c) ) / (2*a)
  print("The roots are " + str(x1) + " and " + str(x2))
quadratic(2, 3, 1)
quadratic(1, 1, 0)
quadratic(1, 0, -1)
  