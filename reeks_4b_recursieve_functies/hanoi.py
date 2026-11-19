def hanoi(n):
    def verplaats(n, van, naar, hulp):
        if n == 0:
            return 0
        stappen = verplaats(n - 1, van, hulp, naar)
        print(f"Schijf {n} van {van} naar {naar}")
        stappen += 1
        stappen += verplaats(n - 1, hulp, naar, van)
        return stappen

    aantal = verplaats(n, "A", "C", "B")
    print(f"{aantal} stappen gedaan")
    
    

hanoi(2)