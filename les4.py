import random, time
import matplotlib.pyplot as plt

def zoek_argo(x, rij):
    l = 0
    r = len(rij) - 1
    while l != r:
        m = (l+r) //2
        if rij[m] < x:
            l = m + 1
        else: r = m
        return l
    
    
    #while 1 < len(rij) and rij[i] != x:
    #   i = i + 1 
    #return i


resultaten = []
aantal_keer = 100
for k in range(1, 14):
    n = 2 ** k
    rij = random.sample(range(1_000_000_000), n)
    te_zoeken = random.choices(rij, k=30)
    start = time.perf_counter()
    for zoek in te_zoeken:
        for i in range(aantal_keer):
            zoek_argo(zoek, rij)
    tijd = (time.perf_counter() - start / (len(te_zoeken)* aantal_keer))
    resultaten.append((n, tijd))

xs, ys = zip(*resultaten)
plt.plot(xs, ys, '-0')
plt.xlabel("n")
plt.ylabel("gemiddelde tijd (s)")
plt.show()