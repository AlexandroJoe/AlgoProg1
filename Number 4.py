import math

a = float(input("Enter side length of the hexagon :"))

hexagon = ((3 * math.sqrt(3)) * (a ** 2)) / 2

print ("The area of a hexagon with side length", a, "is", hexagon)