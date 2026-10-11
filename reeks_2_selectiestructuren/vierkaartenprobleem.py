invoerKeuze = str(input()).lower()

if invoerKeuze == "waarde":
    invoerGetal = int(input())
    invoerJaOfNee = str(input()).lower()
    if invoerGetal == 3:
        if invoerJaOfNee == "ja":
            keuze = "Fout"
        else: #invoerJaOfNee == "nee"
            keuze = "Juist"
    else: #invoerGetal == 8
        if invoerJaOfNee == "ja":
            keuze = "Juist"
        else: #invoerJaOfNee == "nee"
            keuze = "Fout"
    print(f"{keuze}: kaarten met {invoerKeuze} {invoerGetal} moeten{" niet"if invoerGetal == 3 else ""} gedraaid worden.")
else: #invoerKeuze == "kleur"
    invoerKleur = str(input()).lower()
    invoerJaOfNee = str(input()).lower()
    if invoerKleur == "rood":
        if invoerJaOfNee == "ja":
                keuze = "Fout"
        else: #invoerJaOfNee == "nee"
                keuze = "Juist"
    else: #invoerGetal == 8
        if invoerJaOfNee == "ja":
                keuze = "Juist"
        else: #invoerJaOfNee == "nee"
                keuze = "Fout"
    print(f"{keuze}: kaarten met {invoerKeuze} {invoerKleur} moeten{" niet"if invoerKleur == "rood" else ""} gedraaid worden.")