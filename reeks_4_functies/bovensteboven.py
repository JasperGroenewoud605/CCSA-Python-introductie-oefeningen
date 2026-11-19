

def bovensteboven(getal):
    reversedGetal = ''
    nonTurnables = ['2','3','4','5','7']
    arrayGetal = list(str(getal))
    
    for gtl in arrayGetal:
        if gtl in nonTurnables:
            return False

    arrayGetal.reverse()

    for gtl in arrayGetal:
        if gtl == '6':
            reversedGetal += '9'
        elif gtl == '9':
            reversedGetal += '6'
        else: reversedGetal += gtl

    reversedGetal = int(reversedGetal)

    if reversedGetal == getal: 
        return True
    else: return False

def volgende(getal):
    nieuwGetal = getal + 1
    while bovensteboven(nieuwGetal) != True:
        nieuwGetal += 1
    return nieuwGetal

invoer = int(input())
print(volgende(invoer))
