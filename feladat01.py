def feladat1():
    feladat1_1()

def feladat2():
    feladat2_1()

def feladat3():
    pass

def feladat1_1():
    ar = int(input("Ár: "))
    mennyiseg = int(input("Mennyiség: "))
    feladat1_2(ar , mennyiseg)

def feladat1_2(ar , mennyiseg):
    rounded = round((mennyiseg / 12) * ar , 2)
    print("Havi átlag bevételed: " + str(rounded) + " Ft")
    feladat1_3(rounded)

def feladat1_3(rounded):
    if rounded > 30000:
        print("Sikeres a vállalkozás!")
    else:
        print("Sikertelen a vállalkozás!")

def feladat2_1():
    f = open("elemek.txt", "r").read().strip().split("\n")
    print(f"Lista elemeinek száma: {feladat2_2(f)}")
    print(f"Lista utolsó eleme: {feladat2_3(f)}")
    print(f"Lista tartalmazza-e a/az '??' elemet: {kereses('Arany', f)}")

def feladat2_2(list_elemek):
    return len(list_elemek)

def feladat2_3(list_elemek):
    return list_elemek[-1]

def kereses(elem_neve, lista):
    for i in range(len(lista)):
        if lista[i] == elem_neve:
            return True
    return False

def feladat2_5(list_elemek):
    input("Kérek egy elemet: ")
    

def main():
    feladat1()
    feladat2()
    feladat3()

if __name__ == "__main__":
    main()
