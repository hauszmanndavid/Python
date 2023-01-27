file = open("utvonal2.txt","r")
file2=open("rovid.txt","w")
file_data = []
file2_rovid = []

for i in file:
    if(i[-1]=='\n'):
        file_data.append(i[:-1].split('\t'))
    else:
        file_data.append(i.split('\t'))
  
del file_data[0]

#vessző csere pontra:
for i in range(len(file_data)):
    csere = ''
    for j in range(len(file_data[i][1])): #ezzel mindig a 2.(távolság)-ot vizsgálja
        if(file_data[i][1][j]==','):
            csere+='.'
        else:
            csere+= file_data[i][1][j]
    file_data[i][1] = float(csere)
    
print(file_data)

print("Útvonalak darabszáma: ", len(file_data),"darab")
print("Nem oktatási célú ösvények: ")
for i in range(len(file_data)):
    if("tan" not in file_data[i][0].lower()):
        print(file_data[i][0])
        
'''for i in range(len(file_data)):
    if(file_data[i][1]<1):
        file2_rovid.append(file_data[i])'''

#<xkm     
max=float(input("Maximum hány km mennél: "))


 
for i in range(len(file_data)):
    if(file_data[i][1]<=max):
        file2.write(file_data[i][0]+"\t"+file_data[i][2]+"\n")
        
#Átlag hossz
osszeg = 0

for i in range(len(file_data)):
    osszeg+=file_data[i][1]
    
print("Az út  átlagos hossza: ", round(osszeg/len(file_data),2))

#keresett
keres = input("Keresett útvonal: ")

for i in range(len(file_data)):
    if(keres.lower() in file_data[i][0].lower()):
        print(file_data[i][0]+"\t"+str(file_data[i][1])+file_data[i][2])