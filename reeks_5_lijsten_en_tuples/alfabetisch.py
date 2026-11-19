def alfabetisch(zin):
    nieuwe_zin = " ".join(sorted(zin.split()))
    return nieuwe_zin

print(alfabetisch('zeven zatte zaventemse zotten zullen zeven zomerse zondagen zwemmen zonder zwembroek'))
print(alfabetisch('een pet met een platte klep is een plattekleppet'))
print(alfabetisch('je ziet een boel vliegen vliegen maar er is geen een bij bij'))
