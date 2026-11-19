import math

p = int(input())
k = int(input())
i = 1
a = k
while i <= p:
    c = a % p
    b = (a - c) // p
    print(f"{a} noten = {math.floor(b)} noten voor piraat#{i} en {"geen" if c == 0 else f"{c}"} {"noot" if c == 1 else "noten"} voor de aap")
    a = a - b - c
    i += 1

c = a % p
b = (a - c) // p
print(f"elke piraat krijgt {b} noten en {"geen" if c == 0 else f"{c}"} {"noot" if c == 1 else "noten"} voor de aap")