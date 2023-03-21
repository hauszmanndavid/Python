class Állatfaj:
    def __init__(self, fajnév, tömeg):
        self.fajnév = fajnév
        self.tömeg = tömeg
    def döntés(self):
        return
     
Állat = []   
for i in range(3):
    fajnév = input("Add meg egy állatfaj nevét! ")
    tömeg = input("Hány kilogramm a tömege egy állatfajnak? ")
    össztömeg = Állatfaj(fajnév,tömeg) 
    Állat.append(össztömeg)
    
for i in Állat:
    print("A(z) " + i.fajnév + " tömege "+ i.tömeg + " kg.")
    