"""Math calculations."""

import math

"""Area of a circle."""
r = 90
circle_area = round((math.pi * r ** 2), 2)
print(circle_area)

"""Area of an equilateral triangle."""
a = 58
triangle_area = round((a ** 2 * math.sqrt(3)) / 4)
print(triangle_area)

"""Calculate discriminant."""
a = 73
b = 11
c = 37
discriminant = b ** 2 - 4 * a * c
print(discriminant)

"""Calculate hypotenuse length."""
a = 81
b = 44
c = math.sqrt(a ** 2 + b ** 2)
print(c)

"""Calculate cathetus length."""
c_side = 88
a_side = 43
b_side = math.sqrt(c_side ** 2 - a_side ** 2)
print(b_side)
