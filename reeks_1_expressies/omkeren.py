getal1 = int(input())
getal2 = int(input())
getal3 = int(input())

def wisselGetallen(getal1, getal2, getal3):
    wisselGetal = getal1
    getal1 = getal3
    getal3 = wisselGetal
    return [getal1, getal2, getal3]

getallen = wisselGetallen(getal1, getal2, getal3)
print(f"{getallen[0]} {getallen[1]} {getallen[2]}")