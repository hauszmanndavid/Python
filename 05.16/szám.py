def vizsgál (szám1,szám2):
    if szám1 > szám2:
        return szám1 + " a nagyobb szám"
    elif szám2 > szám1:
        return szám2 + " a nagyobb szám"
    else:
        return "a két szám egyenlő"


szám1 = input("Írja be az első számot: ")
szám2 = input("Írja be a második számot: ")

print(vizsgál(szám1,szám2))