kilometerStandVoorRit = float(input())
kilometerStandNaRit = float(input())
benzineTotVolleTank = float(input())

def berekenBenzineVerbruik(kmStandVoorRit, kmStandNaRit, benzineTotVolTank):
    return benzineTotVolTank/((kmStandNaRit - kmStandVoorRit)/100)

print(berekenBenzineVerbruik(kilometerStandVoorRit,
      kilometerStandNaRit, benzineTotVolleTank))