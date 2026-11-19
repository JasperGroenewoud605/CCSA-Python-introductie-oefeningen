def hoeveel_rozen(roodWit, witBlauw, groterOfKleiner):
    if groterOfKleiner not in ("<", ">"):
        print("Verkeerde invoer")
        return None

    for blauw in range(2, witBlauw + 1):
        wit = witBlauw - blauw
        rood = roodWit - wit
        roodBlauw = rood + blauw
        if rood < 2:
            continue

        if groterOfKleiner == "<" and roodBlauw < witBlauw:
            return [blauw, wit, rood]
        if groterOfKleiner == ">" and roodBlauw > witBlauw:
            return [blauw, wit, rood]

    return None

roodWit = int(input())
witBlauw = int(input())
groterOfKleiner = str(input())

waarden = hoeveel_rozen(roodWit, witBlauw, groterOfKleiner)

print(f"{waarden[0]}\n{waarden[1]}\n{waarden[2]}")
