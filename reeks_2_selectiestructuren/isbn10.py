isbnReeks = []

for _ in range(10):
    isbnReeks.append(int(input()))

def checkIsbnCode(reeks):
    totaal = 0
    for i in range(9):
        totaal += reeks[i]*(i+1)
    if totaal % 11 == reeks[9]:
        return 'OK'
    else:
        return 'FOUT'

print(checkIsbnCode(isbnReeks))
