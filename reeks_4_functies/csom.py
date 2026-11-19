def csom(getal):
    getal = int(getal)
    arrayGetal = list(str(getal))
    while len(arrayGetal) != 1:
        nieuwGetal = 0
        for gtl in arrayGetal:
            nieuwGetal += int(gtl)
        arrayGetal = list(str(nieuwGetal))
    return int(arrayGetal[0])

print(csom(840800))
print(csom(377096267))
print(csom(897593))

    