def meccs(perc):
    if(perc <90):
        return "A mérkőzés félbeszakadt"
    else:
        ráadás = perc-90
        return "A mérkőzés 90 perc+ "+str(ráadás)+" perc volt!"


perc = int(input("Hány percig tartott a meccs: "))
print("A mérkőzés", meccs(perc))
