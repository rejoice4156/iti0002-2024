"""Math exercises."""
import math

"""Time converter."""
seconds = 37810
# Calculate how many hours fit in the given amount of seconds (1h = 3600s).
hours = seconds // 3600
# Calculate the remainder of seconds left over after division by full amount of hours.
seconds = seconds % 3600
# Calculate how many minutes fit into the remainder of seconds left over (1min = 60s).
minutes = seconds // 60
print(hours, minutes)

"""Trigonometry calculator."""
deg = 339
# Convert given degrees into radians.
rad = math.radians(deg)
# Calculate the sine from given radians and round to 1 place after comma.
sine = round(math.sin(rad), 1)
# Calculate the cosine from given radians and round to 1 place after comma.
cosine = round(math.cos(rad), 1)
print(f"Sine is {sine}, cosine is {cosine}")

"""Greetings."""
hey = "Hey"
lots_of_heys = hey * 87
print(lots_of_heys)

"""Adding numbers."""
a = 81
b = 69
string_numbers = f"{a}{b}"
print(string_numbers)
