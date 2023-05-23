def vizsgal(szó):
    if(szó[0] in magánhangzó):
        return "az " + szó
    else:
        return "a " + szó



magánhangzó = ["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"]

szó = input("Írjon be egy tetszőleges szót: ")
print(vizsgal(szó))

#magánhangó: a, á e é i í o ó ö ő u ú ü ű 
#mássalhangzó: 