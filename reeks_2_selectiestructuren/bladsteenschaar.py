speler1 = input().lower()
speler2 = input().lower()

wint_van = {
    "schaar": {"blad","hagedis"},
    "blad": {"steen", "spock"},
    "steen": {"schaar", "hagedis"},
    "hagedis": {"blad", "spock"},
    "spock": {"schaar", "steen"},
}

if speler1 == speler2:
    print("gelijkspel")
elif speler2 in wint_van[speler1]:
    print("speler1 wint")
else:
    print("speler2 wint")