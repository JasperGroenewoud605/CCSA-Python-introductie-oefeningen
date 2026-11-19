def zien(list):
    lijst = []
    aantal_rood = 0
    for gok in list:
        if aantal_rood % 2 == 1:
            lijst.append('R')
        else: lijst.append('B')
        if gok == 'R':
            aantal_rood += 1
    return tuple(lijst)

def zeggen(lists):
    lijst = list((lists[::-1]))
    nieuwe_lijst = []
    aantal_rood = 0
    def zeggenRecursief(lijst):
        wissel_lijst = []
        if lijst[0] == 'B':
            nieuwe_lijst.append('B')
            lijst.pop(0)
        elif lijst[0] == 'R':
            nieuwe_lijst.append('R')
            lijst.pop(0)
            for i in range(0,len(lijst)):
                if lijst[i] == 'R':
                    wissel_lijst.append('B')
                else: wissel_lijst.append('R')
        if len(lijst) > 1:
            zeggenRecursief(wissel_lijst or lijst)
        else:
            nieuwe_lijst.append((wissel_lijst or lijst).pop())
            return nieuwe_lijst
    zeggenRecursief(lijst)
    return tuple(nieuwe_lijst[::-1])

#print(zien(('R', 'B', 'R', 'R', 'B')))
print(zeggen(('B', 'R', 'R', 'B', 'R')))

#print(zien(['R', 'R', 'B', 'R', 'R', 'B', 'R', 'B', 'R', 'R']))
print(zeggen(['B', 'R', 'B', 'B', 'R', 'B', 'B', 'R', 'R', 'B']))

#print(zien('BBRBRBRBBRBR'))
print(zeggen('BBRBRBRBBRBB'))