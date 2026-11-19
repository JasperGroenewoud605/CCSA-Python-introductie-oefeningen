def eerste(hidato):
    for i in range(0, len(hidato)):
        if 1 in hidato[i]:
            break
    return i, hidato[i].index(1)

def opvolger(hidato, rij_nr, kol_nr):
    opvolg_getal = hidato[rij_nr][kol_nr]
    for i in range(0, len(hidato)):
            if opvolg_getal+1 in hidato[i]:
                break
    if i == rij_nr-1 or i == rij_nr or i == rij_nr+1:
         if hidato[i].index(opvolg_getal+1) == kol_nr-1 or hidato[i].index(opvolg_getal+1) == kol_nr or hidato[i].index(opvolg_getal+1) == kol_nr+1:
              return i, hidato[i].index(opvolg_getal+1)
    else:
         return None, None

def laatste(hidato):
    rij_nr, kol_nr = eerste(hidato)
    resultaat = 0
    while resultaat != (None, None):
        vorig_resultaat = resultaat
        rij_nr, kol_nr = opvolger(hidato, rij_nr, kol_nr)
        resultaat = rij_nr, kol_nr
    return vorig_resultaat

def hidato(hidato):
    rij_nr, kol_nr = laatste(hidato)
    totaal_len = 0
    for list in hidato:
        totaal_len += len(list)
    if totaal_len == hidato[rij_nr][kol_nr]:
        return True
    else: return False
     
print(hidato([[5, 4, 11, 12], [6, 10, 3, 2], [7, 8, 9, 1]]))
print(hidato([[8, 14, 13, 12], [15, 1, 2, 11], [5, 3, 10, 16], [4, 6, 7, 9]]))
print(hidato(((18, 19, 20, 4, 5), (17, 1, 3, 6, 8), (16, 13, 2, 9, 7), (14, 15, 12, 11, 10))))