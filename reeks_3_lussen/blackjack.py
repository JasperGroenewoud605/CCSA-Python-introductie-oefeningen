totaal = 0

while totaal < 21:
    invoer = int(input())
    if invoer == 0:
        break
    totaal += invoer

if totaal == 21:
    print("Gewonnen!")
elif totaal > 21:
    print(f"Verbrand ({totaal})")
elif totaal < 21:
    print(f"Voorzichtig gespeeld ({totaal})")