#Be szöveg, van e benne a keresett karakter, függvénnyel

def vizsgál (szöveg,betű):
    if betű in szöveg or betű.upper() in szöveg :
        return  "Szerepel benne a keresett betű"
    else:
        return "Nincs benne a keresett betű"


szöveg = input("Szöveg: ")
betű = input("Írja be a keresett betűt: ")

print(vizsgál(szöveg,betű))