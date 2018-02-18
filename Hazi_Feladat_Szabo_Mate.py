def feladat_1(a, b):
    a = a + b
    b = a - b
    a = a - b
    print(a, b)

def feladat_2():
    a = int(input('Elso egesz szam erteke: '))
    b = int(input('Masodik egesz szam erteke: '))
    c = int(input('Harmadik egesz szam erteke: '))
    if a > b and a > c:
        if b >= c:
            print(c, b, a)
        else:
            print(b, c, a)
    elif a > b and a < c:
        print(b, a, c)
    elif a < b and a > c:
        print(c, a, b)
    elif a < b and a < c:
        if b >= c:
            print(a, c, b)
        else:
            print(a, b, c)

def feladat_3(x):
    x = float(x)
    if x > -2 and x < 0:
        print(2 * x)
    elif x >= 0 and x < 2:
        print(x * x)
    elif x > 2:
        print('10')
    else:
        print('Nem definialt.')

def main():
    feladat_1(5,9)
    feladat_2()
    feladat_3()
main()