f = open("kerdes.txt","r")

feladatok = f.readlines()

for c in feladatok:
    for betu in c:
        if(betu!='*'):
            print(betu,end="")
            
print("\n")
for kerdes in feladatok:
    helye = kerdes.index('*')
    print(helye)
    jo=kerdes[helye+1]
    
    
tipp = input()
if(tipp==jo):
    print("Gratula")
else:
    print("Rossz")
print("Jó válasz: ",jo)
varakozas = input()
