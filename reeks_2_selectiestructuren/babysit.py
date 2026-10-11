invGetal1 = int(input()) 
invGetal2 = int(input()) / 60 * 100
invGetal3 = int(input()) 
invGetal4 = int(input()) / 60 * 100
totaalPrijs = 0
beginTijd = invGetal1 + (invGetal2/100)
eindTijd = invGetal3 + (invGetal4/100)
totaalTijd = eindTijd - beginTijd

if eindTijd < 18 or beginTijd < 18:
    print("ongeldige invoer")
else:
    if eindTijd > 21.5:
        if beginTijd > 21.5:
            verschilTijd = eindTijd - beginTijd
        else:
            verschilTijd = eindTijd - 21.5
        totaalPrijs += verschilTijd * 4
        totaalTijd -= verschilTijd

    totaalPrijs += totaalTijd * 2
    print(totaalPrijs)