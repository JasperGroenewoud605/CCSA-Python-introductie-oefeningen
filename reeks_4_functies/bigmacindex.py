def waardering(prijsBigMac, reeleWisselkoers):
    prijsBigMacUSA = 4.07
    bigMacWisselkoers = prijsBigMac/prijsBigMacUSA
    verschilWisselkoers = ((bigMacWisselkoers - reeleWisselkoers)/reeleWisselkoers)*100
    if verschilWisselkoers < -25:
        return 'sterk ondergewaardeerd'
    elif verschilWisselkoers < - 5:
        return 'ondergewaardeerd'
    elif verschilWisselkoers < 5:
        return 'ongeveer gelijk'
    elif verschilWisselkoers < 25:
        return 'overgewaardeerd'
    else: return 'sterk overgewaardeerd'

def wisselkoersanalyse(bedragMetEenheid, reelewisselkoers):
    bedrag, eenheid = bedragMetEenheid.split(" ", 1)
    bedrag = float(bedrag)
    return f"De {eenheid} is {waardering(bedrag, reelewisselkoers)} ten opzichte van de dollar."

print(waardering(3.44, 0.70))
print(wisselkoersanalyse('3.44 euro', 0.70))