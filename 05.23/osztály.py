class HíresNő:
    def __init__(self, név, foglalkozás, nemzetiség):
        self.név = név
        self.foglalkozás = foglalkozás
        self.nemzetiség = nemzetiség
        
    def előtag(self):
        if self.nemzetiség == "n":
           return "Frau"
        elif self.nemzetiség == "a":
            return "Ms"
        else:
            return "A megadott elöljáró tag nem található"

lLista = []

for i in range(3):
    név = input("Add meg a híres nő nevét! ")
    foglalkozás = input("Add meg a foglalkozását! ")
    nemzetiség = input("Add meg a  nemzetiségét (a/n)! ")
    híresnő = HíresNő(név, foglalkozás, nemzetiség)
    lLista.append(híresnő)

for i in lLista:
    print(i.előtag(), i.név+ "egy híres"+ i.foglalkozás,)
