def vizsgál(eredetiár,újár):
    egyszázalék = eredetiár/100
    if újár > eredetiár:
        növekedés = újár-eredetiár
        return round((növekedés/egyszázalék),2), "ennyi százalékkal nőtt a termék ára"
    elif újár < eredetiár:
        csökkenés = eredetiár-újár
        return round((csökkenés/egyszázalék),2), "ennyi százalékkal lett kevesebb a termék ára"
    elif eredetiár==újár:
        return "Nincs árváltozás"



eredetiár = int(input("Adja meg  az eredeti árat: "))
újár = int(input("Adja meg az ús árat: "))
print(vizsgál(eredetiár,újár))
