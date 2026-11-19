import math

def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

invoer = int(input())
totaalBeleefd = 0
if is_power_of_two(invoer) == True or invoer < 0:
    print(totaalBeleefd)
else:
    i = 1
    maxGetal = math.ceil(invoer/2)
    while i != maxGetal:
        som = 0
        refGetal = i
        for refGetal in range(i,maxGetal+1):
            som += refGetal
            if som == invoer:
                totaalBeleefd += 1
                i += 1
                break
            elif som > invoer:
                i += 1
                break
            refGetal += 1
    print(totaalBeleefd)