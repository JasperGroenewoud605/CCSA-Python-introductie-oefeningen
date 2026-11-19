def iszigzag(reeks):
    for i in range(0, len(reeks)-1):
        groterdan = i%2 == 0
        if groterdan == True:
            if reeks[i] >= reeks[i+1]:
                pass
            else: return False
        elif groterdan == False:
            if reeks[i] <= reeks[i+1]:
                pass
            else: return False
    return True

def zigzag_traag(reeks):
    resultaat = sorted(reeks)
    for i in range(0, len(resultaat)):
        if i%2 == 1:
            resultaat[i-1], resultaat[i] = resultaat[i], resultaat[i-1]
    reeks[:] = resultaat

def zigzag_snel(reeks):
    for i in range(0, len(reeks), 2):
        if i > 0 and reeks[i] < reeks[i - 1]:
            reeks[i], reeks[i - 1] = reeks[i - 1], reeks[i]
        if i < len(reeks) - 1 and reeks[i] < reeks[i + 1]:
            reeks[i], reeks[i + 1] = reeks[i + 1], reeks[i]

print(iszigzag([10, 5, 6, 3, 2, 20, 100, 80]))
print(iszigzag((10, 5, 6, 2, 20, 3, 100, 80)))
print(iszigzag([20, 5, 10, 2, 80, 6, 100, 3]))

reeks = [10, 90, 49, 2, 1, 5, 23]
r = zigzag_traag(reeks)
print(reeks)

reeks = [10, 90, 49, 2, 1, 5, 23]
zigzag_snel(reeks)
print(reeks)
