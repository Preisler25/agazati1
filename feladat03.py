class Versenyzo:
    def __init__(self, sor):
        split = sor.split(';')
        self.nev = split[0]
        self.orszag = split[1]
        self.technikai = float(split[2])
        self.komponens = float(split[3])
        self.levonas = int(split[4])
    def __str__(self):
        return f'{self.nev} ({self.orszag}) {self.technikai} {self.komponens} {self.levonas}'

def feladat0():
    f = open('korcsolya.csv', 'r').read().split('\n')
    for i in range(len(f)-1):
        if i != 0:
            f[i] = Versenyzo(f[i])
    f.pop(0)
    f.pop(-1)
    return f

def feladat1(lista):
    print("résztvevők: ", len(lista))

def feladat2(lista):
    for i in lista:
        if i.orszag == 'HUN':
            print("volt")
            return
        
def feladat3(lista):
    temp = 0
    for i in lista:
        if ervervenyes(i.technikai, i.komponens):
            temp += 1
    print(f"{temp} versenyzőnek nem számolható a pontszáma")

def ervervenyes(num1, num2):
    if num1 > 1000 or num2 > 1000:
        return False
    else:
        return True

def feladat4(lista, nev):
    for i in lista:
        if i.nev == nev:
            print(i)
            if ervervenyes(i.technikai, i.komponens):
                return pontszam(i.technikai, i.komponens, i.levonas)
            else:
                return 0

def pontszam(num1, num2, num3):
    return num1 + num2 - num3

def feladat5(f):
    a = input("Kérek egy nevet: ")
    print(f"{a} pontszáma: {feladat4(f, a)}")

def feladat6(f):
    temp_list = []
    for i in f:
        if ervervenyes(i.technikai, i.komponens):
            temp_list.append(i)
    feladat7(temp_list)

def feladat7(lista):
    f = open('tokeletesek.txt', 'w', encoding='utf-8')
    for i in lista:
        f.write(f"név:{i.nev} pont:{pontszam(i.technikai, i.komponens, i.levonas)}\n")

def main():
    f = feladat0()
    feladat1(f)
    feladat2(f)
    feladat3(f)
    feladat5(f)
    feladat6(f)

main()
