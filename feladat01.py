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

def feladat2():
    pass

def feladat3():
    pass

def main():
    feladat1_1()

if __name__ == "__main__":
    main()
