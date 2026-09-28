import math

len_AB = int(input())
len_BC = int(input())

angle = round(math.degrees(math.atan(len_AB / len_BC)))
print(str(angle) + chr(176))
