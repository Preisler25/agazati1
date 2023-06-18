import random

def fel01():
    a = int(input("Kérek egy termék árat: "))
    b = int(input("Kérek egy éves eladott mennyiséget: "))
    c = round((a * b)/12, 2)
    
    print("A havi átlag bevétel: ", c)
    if c > 35000:
        print("sikeres")
    else:
        print("sikertelen")

fel01()

def kereses(nev, lista):
    if nev in lista:
        return True

def ajánlás(lista):
    return random.choice(lista)

def fel02():
    f = open("elemek.txt", "r", encoding="utf8").read().strip().split("\n")
    print("lista elemeinek száma:", len(f))
    print("lista utolsó eleme:" , f[-1])
    a = input("Kérek egy elemet: ")
    if kereses(a, f):
        print("Van ilyen elem")
    else:
        print("Nincs ilyen elem")
    print ("Ajánlott elem: ", ajánlás(f))
    

fel02()