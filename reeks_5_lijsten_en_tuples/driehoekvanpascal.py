import math
def driehoek(r):
    if isinstance(r, int) == False or r < 0:
        raise AssertionError("ongeldig aantal rijen")
    rijen, rij_x, rij_x2, rij_finaal = [], [], [], []
    for rij in range(0, r+1):
        if rij == 1:
            rij_x.append(1)
            rijen.append(rij_x)
        if rij > 1:
            rij_x, rij_x2 = rijen[-1], rijen[-1]
            rij_x, rij_x2 = [0] + rij_x, rij_x2 + [0]
            for value in range(0, len(rij_x)):
                rij_finaal.append(rij_x[value] + rij_x2[value])
            rijen.append(rij_finaal)
            rij_finaal = []
    return rijen

def zeshoek(r, k):
    if k >= r or k == 1:
        raise AssertionError("ongeldige interne positie")
    k, r = k - 1, r - 1
    lijst_getallen = []
    driehoek_x = driehoek(r+2)
    midden_rij = driehoek_x[r]
    boven_rij = driehoek_x[r-1]
    onder_rij = driehoek_x[r+1]
    lijst_getallen.extend([boven_rij[k-1], boven_rij[k], midden_rij[k+1], onder_rij[k+1], onder_rij[k], midden_rij[k-1]])
    return lijst_getallen

def kwadraat(r, k):
    if k >= r or k == 1:
        raise AssertionError("ongeldige interne positie")
    lijst_getallen = zeshoek(r, k)
    lijst_factoren = []
    product = math.prod(lijst_getallen)
    for getal in lijst_getallen:
        lijst_factoren.extend([f"{getal}", "x"])
    lijst_factoren.pop()
    string_factoren = " ".join(lijst_factoren)
    vierkantswortel = math.isqrt(product)
    return f"{string_factoren} = {product} = {vierkantswortel} x {vierkantswortel}"

    

#print(driehoek(0))
#print(driehoek(1))
#print(driehoek(2))
#print(driehoek(3))
#print(driehoek(4))
#print(driehoek(5))
#print(driehoek(-1))
#print(driehoek(3.14))

#print(zeshoek(8, 4))
#print(zeshoek(16, 7))
#print(zeshoek(3, 3))

print(kwadraat(8, 4))
print(kwadraat(16, 7))
#print(kwadraat(3, 3))