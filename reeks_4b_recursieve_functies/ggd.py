def ggd(getal1, getal2):
    kleinste = getal1 if getal1 < getal2 else getal2
    grootste = getal2 if kleinste == getal1 else getal1
    rest = grootste%kleinste
    return ggd(rest, kleinste) if rest != 0 else kleinste

print(ggd(21, 14))
print(ggd(48, 18))
print(ggd(18, 48))
print(ggd(17, 5))