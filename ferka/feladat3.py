class Versenyzo:
    def __init__(self, sor):
        split = sor.split(";")
        self.nev = split[0]
        self.orszag = split[1]
        self.technikai = float(split[2])
        self.komponens = float(split[3])
        self.levonas = float(split[4])

    def __str__(self):
        return f"{self.nev} ({self.orszag})\n\ttechnikai: {self.technikai}\n\tkomponens: {self.komponens}\n\tlevonás: {self.levonas}"

def beolvas():
    f = open("korcsolya.csv", "r", encoding="utf8").read().strip().split("\n")
    for i in range(len(f)):
        if i != 0:
            f[i] = Versenyzo(f[i])
    f.pop(0)
    print(f)
    return f

def fel15(f):
    print(len(f))

def fel16(f):
    for i in f:
        if i.orszag == "HUN":
            print("van magyar induló")
            break
        else:
            print("nincs magyar induló")
            break

def fel17(f):
    temp = 0
    for i in f:
        if not ervenyes(i):
            temp += 1
    print(f"{temp} embernek nem számithatók a pontjai")

def ervenyes(i):
    if i.komponens > 1000 or i.technikai > 1000:
        return False
    else:
        return True

def pontszam(i):
    return i.technikai + i.komponens - i.levonas

def fel18(f, nev):
    for i in f:
        if i.nev == nev:
            if ervenyes(i):
                print(f"{i.nev} pontszáma: {pontszam(i)}")

def fel19(f):
    a = input("Kérek egy nevet: ")
    fel18(f, a)

def fel110(f):
    w = open("tokeletes.txt", "w", encoding="utf8")
    for i in f:
        if ervenyes(i):
            w.write(f"{i.nev};{pontszam(i)}\n")

def main():
    lista = beolvas()
    fel15(lista)
    fel16(lista)
    fel17(lista)
    fel19(lista)
    fel110(lista)


main()