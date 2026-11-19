def varkenswoord(woord):
    ArrayWoord = list(str(woord))
    klinkers = ['a','e','i','o','u']
    nieuwWoord = ''
    for lttr in klinkers:
        if lttr == ArrayWoord[0].lower():
            woord += "way"
            return woord
    
    EersteHoofdletter = ArrayWoord[0].isupper()
    i = 0
    while ArrayWoord[0] not in klinkers:
        letter = ArrayWoord.pop(0)
        ArrayWoord.append(letter.lower() if i == 0 else letter)
        i += 1
    if EersteHoofdletter == True:
        ArrayWoord[0] = ArrayWoord[0].upper()
    for letter in ArrayWoord:
        nieuwWoord += letter
    nieuwWoord += 'ay'
    return nieuwWoord

def varkenslatijn(zin):
    ArrayWoorden = zin.split()
    newArrayWoorden = []
    newZin =''
    tkn = None
    for woord in ArrayWoorden:
        nieuwWoord = ''
        ArrayWoord = list(str(woord))
        for char in ArrayWoord:
            if char.isalpha() == False:
                index = ArrayWoord.index(char)
                tkn = ArrayWoord.pop(index)
            else: nieuwWoord += char
        newZin += varkenswoord(nieuwWoord)
        if tkn != None:
            newZin += tkn
            tkn = None
        newZin += ' '
    return newZin.strip()
        
        #newArrayWoorden.append(nieuwWoord)
        #if tkn != None:
        #    newArrayWoorden.append(tkn)
        #   tkn != None
    
        

#print(varkenslatijn("Dit is een test!"))
#print(varkenslatijn('And now for something completely different!'))
print(varkenslatijn('Stwike him, centuwion, stwike him vewy wuffly'))
print(varkenslatijn("No, I'm only pulling your leg, it's crucifixion really!"))