import math
def nieuw_kaartspel(symbool_lijst, getallen_lijst):
    resultaat_lijst = []
    for symbool in symbool_lijst:
        for getal in getallen_lijst:
            resultaat_lijst.append(f'{symbool} {getal}')
    return resultaat_lijst

def splits_kaartspel(kaartspel):
    deler = math.floor(len(kaartspel)/2)
    lijst_1 = kaartspel[:deler]
    lijst_2 = kaartspel[deler:]
    return lijst_1, lijst_2

def faro_shuffle(eerste_stapel, tweede_stapel):
    resultaat = []
    i = 0
    for i in range(0, len(tweede_stapel)):
        if i <= len(eerste_stapel)-1:
            resultaat.append(eerste_stapel[i])
        resultaat.append(tweede_stapel[i])
    return resultaat

print(faro_shuffle(['dood 0', 'dood 1', 'liefde 0'],['liefde 1', 'tijd 0', 'tijd 1']))
print(faro_shuffle(['blad 1', 'blad 2', 'blad 3', 'steen 1'],['steen 2', 'steen 3', 'schaar 1', 'schaar 2', 'schaar 3']))
print(faro_shuffle([],['James 7']))