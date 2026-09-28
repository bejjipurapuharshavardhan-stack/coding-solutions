import math

len_AB = int(input())
len_BC = int(input())

angle = round(math.degrees(math.atan(len_AB / len_BC)))

# \u00b0 is the pure text way to tell Python to print a degree symbol
print(str(angle) + "\u00b0")
