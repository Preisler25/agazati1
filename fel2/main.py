import random

lista = []

def feladat01():
    a = int(input("Hány almát szeretne haza vinni?\n"))
    b = (a//20)
    if a%20 != 0: 
        b += 1
        print("körök: ", b)
    else:
        print("körök: ", b)
    
    if b > 3:
        print("3 kör alatt nem lehet hazavinni")
    else:
        print("3 kör alatt hazaviszi az almákat")

"""
Geci nem értem mi a fazs???

Józsi bácsi az almaszüret után esti bulit szervez, amelyre 12barátjaérkezik. A barátoknak a kiskaputól az  ajtóig  kell  eljutniuk  a 3 vadorzó kutya  mellett.A bejutást a  legrövidebb  időn  belül  elvégezniük, nehogy a kutyák felfedezzék őket!•Hozzon  létre  egy  listát  globális  láthatósággal.Készítsen  függvényt gyorsasagnéven!  A függvényben  töltse  fela  listát 2-120  közötti  számokkal.,  vagyis  azzal  az  idővel,  amennyi  idő alatt bejutottaka barátok a házba!Atovábbiakban ezzel a listával dolgozzon!•Írja ki a lista elemeit egymás mellé tabulátorral elválasztva. (Használjon fehér karaktert(\t)!)•. Írjon függvényt legnagyobbsebesseg névvel, mely visszaadja annak a barátnaka sebességét, mely a leggyorsabban teljesítette a25 méteres távolságot(KAPUTÓ-AJTÓIG)!Az eredményt m/s formában határozza meg!•Írassa ki azoknak a exbarátoknaka sorszámát, akik 1percen kívül jutottak be a házba!
"""

def gyorsasag():
    global lista

    for i in range(12):
        lista.append(random.randint(2, 120))

def legnagyobbsebesseg():
    global lista
    min(lista)
    print(f"\nleggyorsabb: {25/int(min(lista))} m/s")

def feladat02():
    global lista    


    gyorsasag()

    for i in lista:
        print(i, end="\t")
    
    legnagyobbsebesseg()

    for i in lista:
        if i < 60:
            print(lista.index(i))

def main():
    feladat01()
    feladat02()

main()

    