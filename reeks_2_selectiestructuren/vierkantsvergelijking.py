import math

a = float(input())
b = float(input())
c = float(input())

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("geen wortels")
elif discriminant == 0:
    print("een wortel")
    x = -b / (2*a)
    print(x)
else:
    print("twee wortels")
    x1 = (-b + math.sqrt(discriminant))/(2*a)
    x2 = (-b - math.sqrt(discriminant))/(2*a)
    print(min(x1, x2))
    print(max(x1, x2))