geplukteAppels = int(input())

def berekenAppels(geplukteAppels):
    volKisten = geplukteAppels // 20
    volPalleten = volKisten // 35
    overigVolKist = volKisten % 35
    overigAppels = geplukteAppels % 20
    return [volPalleten, overigVolKist, overigAppels]

waardes = berekenAppels(geplukteAppels)
print(f"{waardes[0]}\n{waardes[1]}\n{waardes[2]}")