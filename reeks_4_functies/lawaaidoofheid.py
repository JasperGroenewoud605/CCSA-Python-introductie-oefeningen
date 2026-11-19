import math

def maximale_blootstelling(decibels):
    maxSeconden = 28800.0
    if decibels < 80:
        return -1.0
    elif decibels == 80:
        return maxSeconden
    else:
        aantalTeHardeDb = decibels - 80
        aantalKeerTeHard = math.floor(aantalTeHardeDb / 3)
        for i in range (1, aantalKeerTeHard + 1):
            maxSeconden = maxSeconden/2
        return round(maxSeconden, 1)

invoer = float(input())
print(maximale_blootstelling(invoer))