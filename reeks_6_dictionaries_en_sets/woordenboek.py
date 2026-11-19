def vertaling_toevoegen(woord, vertaling_nl, woordenboek):
    woordenboek[woord] = vertaling_nl

def vertaling(woord, woordenboek):
    if woord in woordenboek:
        return(f'{woordenboek[woord]}')
    else: return('???')

woordenboek = {}
vertaling_toevoegen('plerzs', 'vrouw', woordenboek)
vertaling_toevoegen('nirtu', 'bloem', woordenboek)
vertaling_toevoegen('klinzoj', 'dorst', woordenboek)
vertaling_toevoegen('tilza', 'hond', woordenboek)
vertaling_toevoegen('zraidi', 'tijd', woordenboek)
print(woordenboek)

print(vertaling('tilza', woordenboek))
print(vertaling('guoles', woordenboek))