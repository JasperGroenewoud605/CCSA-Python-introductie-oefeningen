def even_oneven(getal):
    arrayGetal = list(str(getal))
    totaalAantalEven, totaalAantalOneven = 0, 0

    for gtl in arrayGetal:
        gtl = int(gtl)
        if gtl%2 == 1:
            totaalAantalOneven += 1
        else: totaalAantalEven += 1

    resultaat = (totaalAantalEven, totaalAantalOneven)
    return resultaat

def volgende(getal):
    arrayGetal = list(str(getal))    
    totaalGetal = len(arrayGetal)
    evenEnOneven = (even_oneven(getal))
    return int(f"{evenEnOneven[0]}{evenEnOneven[1]}{totaalGetal}")
        
def stappen(invoer):
    totaal = 0
    getal = invoer
    while getal != 123:
        getal = volgende(getal)
        totaal += 1
    return totaal


#print(even_oneven(886328712442992))
#print(even_oneven(10515))
#print(even_oneven(145))

#print(volgende(886328712442992))
#print(volgende(10515))
#print(volgende(145))

print(stappen(886328712442992))
print(stappen(1217637626188463187643618416764317864))
print(stappen(0))
print(stappen(1))