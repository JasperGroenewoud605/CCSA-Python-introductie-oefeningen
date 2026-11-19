def zeef(n):
    lijst=list(range(2, n+1))
    def zeef_methode(n, lijst, lijst_priem = []):
        m = min(lijst)
        m_lijst = range(m, n+1, m)
        for waarde in m_lijst:
            if waarde == m:
                lijst_priem.append(m)
            if waarde not in lijst:
                pass
            else: lijst.remove(waarde)
        if len(lijst) == 0:
            return lijst_priem
        else: return zeef_methode(n, lijst, lijst_priem)
    return zeef_methode(n, lijst)

print(zeef(6))
print(zeef(30))
print(zeef(100))

def zeef2(n):
    is_priem = []
    for num in range(n + 1):
        num = True
        is_priem.append(num)
    is_priem[0], is_priem[1] = False, False
    i = 2
    m = i
    while n > m * m:
        if is_priem[m] == True:
            for num in range(m * m, n+1, m):
                if num != m:
                    is_priem[num] = False
        
    return is_priem



print(zeef2(6))
    

