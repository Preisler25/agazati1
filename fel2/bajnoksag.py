#Hely;Csapat;Győzelem;Döntetlen;Kapott Gól;Rugott gól;Pont
class Csapat:
    def __init__(self, sor):
        split = sor.split(';')
        self.hely = split[0]
        self.csapat = split[1]
        self.gyozelem = int(split[2])
        self.dontetlen = int(split[3])
        self.kapott_gol = int(split[4])
        self.rugott_gol = int(split[5])
        self.pont = int(split[6])

    def __str__(self):
        return f'{self.hely} {self.csapat} {self.gyozelem} {self.dontetlen} {self.kapott_gol} {self.rugott_gol} {self.pont}'
    
def feladat0():
    f = open('bajnoksag.csv', 'r').read().strip().split('\n')
    for i in range(len(f)):
        if i != 0:
            f[i] = Csapat(f[i])
    f.pop(0)
    return f

def feladat1(lista):
    print(f"Csapatok száma: {len(lista)}")

def feladat2(lista):
    a = input("Kérek egy csapatnevet: ")
    for i in lista:
        if i.csapat == a:
            print(i.hely)

def feladat3(lista):
    temp = 0
    for i in lista:
        temp += i.rugott_gol
    print(f"Az évben összesen {temp} gólt lőttek")

def feladat4(csapat):
    return 38 - (csapat.gyozelem + csapat.dontetlen)
            
def feladat5(lista):
    legtobbVereseg = lista[0]
    for i in lista:
        if feladat4(i) > feladat4(legtobbVereseg):
            legtobbVereseg = i
    print(f"A legtöbb vereséget szenvedő csapat: {legtobbVereseg.csapat}")
    if legtobbVereseg == lista[-1]:
        print("Az utolsó helyezett csapat a legtöbb vereséget szenvedte el.")
    else:
        print("Az utolsó helyezett csapat nem a legtöbb vereséget szenvedte el.")


def feladat6(lista):
    temp_list = []
    for i in lista:
        if abs(i.rugott_gol-i.kapott_gol) < 15:
            temp_list.append(i)
    f = open('adatok.txt', 'w')
    for i in temp_list:
        f.write(f"{i.csapat} {abs(i.rugott_gol-i.kapott_gol)}\n")
    f.close()

def main():
    f = feladat0()
    feladat1(f)
    feladat2(f)
    feladat3(f)
    feladat5(f)
    feladat6(f)

main()