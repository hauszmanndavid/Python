f = open("szam.txt","r")

Ladatok = f.readlines()
Ljavitott = []
for adat in Ladatok:
    Ljavitott.append(int(adat.rstrip()))

print(Ljavitott)

