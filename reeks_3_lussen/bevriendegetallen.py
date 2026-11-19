import math

def maak_som_van_echte_delers(invoer):
    maxDeler = math.ceil(invoer/2)
    som = 0
    for refGetal in range(1,maxDeler+1):
        if invoer%refGetal == 0:
            som += refGetal
    return som
invoer1 = int(input())
invoer2 = int(input())

somInvoer1 = maak_som_van_echte_delers(invoer1)
somInvoer2 = maak_som_van_echte_delers(invoer2)

print(f"{invoer1} en {invoer2} zijn {"geen "if invoer1 != somInvoer2 or invoer2 != somInvoer1 else ""}bevriende getallen")