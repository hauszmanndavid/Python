#1 Csapat átlag magassága (2 tizedes)
#2 keresés mezszém alapján
#3 hány center, bedobó, irányító van a csapatban?

file = open("jatekos2.txt","r")

Lfile = []

for i in file:
    if(i[-1]=='\n'):
        Lfile.append(i[:-1].split('\t'))
    else:
        Lfile.append(i.split('\t'))
  
del Lfile[0]

#vessző csere pontra:
for i in range(len(Lfile)):
    csere = ''
    for j in range(len(Lfile[i][1])):
        if(Lfile[i][1][j]==','):
            csere+='.'
        else:
            csere+= Lfile[i][1][j]
    Lfile[i][1] = float(csere)
    
print(Lfile)

#átlag magasság:
osszeg=0
for i in range(len(Lfile)):
   osszeg += int(Lfile[i][2])
   
print("A játékosok átlag magassága: ", round(osszeg/len(Lfile),2))

#keresés mezszám alapján:
keres = input("Keresett mezszám: ")

for keres in range(len(Lfile)):
    if(keres == (Lfile[i][1])):
        print("A játékos: ", Lfile[i][0])
    else:
        print("Ilyen mezszám nem található a csapatban")


#3
poszt = 0

for i in range(len(Lfile)):
    (poszt.append(Lfile[i][3]))

print("Ennyi Center: ", poszt.count("center"),"Ennyi Bedobó: ", poszt.count("bedobó"),"Ennyi irányitó: ", poszt.count("irányító"))
    
