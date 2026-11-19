import math

som = 0
for i in range(1, 101):
    som += 1 / (i**2)

print(som)

som = 0
j = 0
while abs(som - math.pi**2 / 6) > 1/100:    
    j += 1
    som += 1 / (j**2)

print(j)