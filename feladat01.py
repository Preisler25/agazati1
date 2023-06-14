import random

def feladat1():
    a = int(input("Kérek a termék árát: "))
    b = int(input("Kérek a éves eladott mennyiséget: "))
    c = round((a * b)/12)
    print("A havi átlag bevétel: ", c)
    if c > 35000:
        print("nyereséges")
    else:
        print("nem nyereséges")

def feladat2():
    f = open('elemek.txt', 'r').read().split('\n')
    print(len(f))
    print(f[-1])    
    a = input("Kérek egy elemet: ")
    if kereses(f, a):
        print("Van ilyen elem")
    else:
        print("Nincs ilyen elem")
    print(f"Egy random elem: {ajánlás(f)}")

def kereses(lista, elem):
    if elem in lista:
        return True
    else:
        return False

def ajánlás(lista):
    return random.choice(lista)

def main():
    feladat1()
    feladat2()

if __name__ == '__main__':
    main()