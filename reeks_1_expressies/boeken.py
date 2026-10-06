boek = 24.95
korting = 0.4
aantalBoeken = 60

def berekenKostBoeken(boek, korting, aantalBoeken):
    inkoopKosten = boek*aantalBoeken*(1-korting)
    verzendKosten = 3 + (aantalBoeken-1)*0.75
    return inkoopKosten+verzendKosten

kosten = round(berekenKostBoeken(boek, korting, aantalBoeken), 2)
print(kosten)