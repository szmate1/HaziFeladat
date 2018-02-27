import math
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

def feladat_4(a,b,c):
    if a < b and a < c:
        print('a legkisebb szam: ', a)
    elif b < a and b < c:
        print('a legkisebb szam: ', b)
    else:
        print('a legkisebb szam: ', c)
    a=abs(a)
    b=abs(b)
    c=abs(c)
    if a > b and a > c:
        print('abszolutertekben vett maximum: ', a)
    elif b > a and b > c:
        print('abszolutertekben vett maximum: ', b)
    else:
        print('abszolutertekben vett maximum: ', c)

def feladat_5(a,b,c,d):
    #print(a,b,c,d) gondolom igy erti a feladat
    if d>=0:
        print(a,c,b,d)
    else:
        print(a,b,d,c)

def feladat_6(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        print("Nem kepezheto haromszog.")
    elif a+b>c and a+c>b and c+b>a:
        p=(a+b+c)/2
        T=math.sqrt(p*(p-a)*(p-b)*(p-c))
        r=T/p
        R=a*b*c /(4*T)
        print("R=%.2f és r=%.2f" % (R,r))
    else:
        print("Nem kepezheto haromszog.")

def feladat_7(h,sz,d):
    K=2*(h+sz)
    maradek=d-K
    if maradek>0:
        print(maradek,' meter drot maradt.')
    elif maradek<0:
        print(maradek, 'meter drot hianyzik a korbekeriteshez.')
    else:
        print('Pont eleg lett a drot.')

def feladat_8(x,a,b,c,d):
    if x<5:
        print('az f(x) fv. erteke: ', (3*x)-5)
    elif x<=10 and x>=5:
        print('az f(x) fv. erteke: 10')
    elif x>10:
        print('az f(x) fv. erteke: ', (9*x)+1)
    if a+c>2*d and b>0:
        print(d-(3*b))
    elif a+c<2*d and b<0:
        print(d+(3*b))
    else:
        print('4')

def feladat_10(a,b):
    db=0
    for i in range(a,b):
        if i%4==0 and (i%100!=0 or i%4==0):
            db += 1
    print(db," db szokoev volt/lesz a ket evszam kozott.")

def feladat_12(maxpont,elert):
    szazalek=(elert/maxpont)*100
    if szazalek>=60:
        print('Sikeres')
    else:
        print('Sikertelen')

def feladat_14(hs): #honapsorszam
    if hs==1:
        print("Januar")
    elif hs==2:
        print("Februar")
    elif hs==3:
        print("Marcius")
    elif hs==4:
        print("Aprilis")
    elif hs==5:
        print("Majus")
    elif hs==6:
        print("Junius")
    elif hs==7:
        print("Julius")
    elif hs==8:
        print("Augusztus")
    elif hs==9:
        print("Szeptember")
    elif hs==10:
        print("Oktober")
    elif hs==11:
        print("November")
    elif hs==12:
        print("December")
    else:
        print('Hiba')

def feladat_15(a,b):
    hanyados=0
    while a>=b:
        hanyados += 1
        a -= b
        continue
    print(hanyados)

def feladat_16(a,b):
    r=a%b
    while r !=0:
        a=b
        b=r
        r=a%b
    lnko=a
    print(lnko)

def feladat_17(szam):
    masolat=szam
    ujszam=0
    while szam>0:
        szamjegy=szam%10
        ujszam=(ujszam*10)+szamjegy
        szam=szam//10
        continue
    if ujszam==masolat:
        print(True)
    else:
        print(False)

def feladat_18(a,b):
    x=a
    y=b
    p=0
    while x>0:
        if x%2!=0:
            p=p+y
        x=x//2
        y=y+y
    print(p)

def feladat_19(n):
    for i in range(3, n):
        if n % i == 0:
            print(False)
    print(True)

def feladat_20(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        if n == 2:
            print(a,b)
        else:
            c = a+b
            print(a,b,c)
            k = 3
            while k < n:
                a = b
                b = c
                c = a+b
                print(c)
                k = k+1

def feladat_21(n):
    ujszam=0
    while n != 0:
        ujszam=(ujszam*10)+(n%10)
        n=n//10
    print(ujszam)

def feladat_22(alap,kitevo):
    eredmeny=1
    while kitevo > 0:
        if kitevo%2 != 0:
            eredmeny = eredmeny*alap
            kitevo -= 1
        alap=alap*alap
        kitevo=kitevo//2
    print(eredmeny)

def feladat_23(ig):
    n = 1
    while n <= ig:
        sum = 0
        oszto = 1
        while oszto < n:
            if not n % oszto:
                sum += oszto
            oszto = oszto + 1
        if sum == n:
            print(n, "tokeletes szam")
        n = n + 1

def feladat_24():
    szam=1
    s1=0
    s2=0
    while szam != 0:
        szam=int(input('adj meg egy szamot: '))
        if szam%7 == 5:
            s1 += 1
        if szam%13 == 7:
            s2 += 1
    print('7-tel valo osztas eseten',s1,'db szam maradeka volt 5.\n13-mal valo osztas eseten',s2,'db szam maradeka volt 7.')

def feladat_25(lakossag,terulet):
    nepsur=lakossag//terulet
    print('az orszag nepsurusege: ', nepsur,'fo/km^2') #noszvaj
    if nepsur < 50:
        print('ritkan lakott')
    elif 50 <= nepsur <= 300:
        print('atlagos nepsurusegu')
    else:
        print('surun lakkott')

def feladat_26():
    szam=1
    dbp=0
    dbn=0
    k=0
    while szam != 0:
        szam=int(input('adj meg egy szamot: '))
        if szam>0:
            dbp +=1
        elif szam<0:
            dbn +=1
        ertek=k+szam
        print(ertek)
        k=ertek
    print(dbp,'db pozitiv es ',dbn,'db negativ szamot adtal meg')

def main():
    feladat_1(5,9)
    feladat_2()
    feladat_3(0.5)
    feladat_4(5,-8,2)
    feladat_5(5,6,7,8)
    feladat_6(3,4,5)
    feladat_7(50,25,150)
    feladat_8(11,2,4,5,8)
    feladat_10(2000, 2014)
    feladat_12(70, 120)
    feladat_14(7)
    feladat_15(250, 125)
    feladat_16(360, 225)  # nem értem
    feladat_17(1221)
    feladat_18(45,17)
    feladat_19(109)
    feladat_20(9)
    feladat_21(55362)
    feladat_22(5,3)
    feladat_23(500)
    feladat_24()
    feladat_25(1856,18.5)
    feladat_26()
main()