def feladat_1(n):
    db=0
    for i in range(1,n+1):
        if n%i==0:
            db=db+1
    if db==4: #1,onmaga,+2
        print(True)
    else:
        print(False)

def feladat_2(a):
    primes=[]
    n=1000
    for i in range(2,n):
        szamlalo=0
        for j in range(1,n):
            if i%j==0:
                szamlalo += 1
        if szamlalo<3:
            primes.append(i)
    print(primes[a-1])

def feladat_3(n):
    szam=2
    while True:
        szam=szam*2
        if szam>=n:
            print(szam)
            break

def feladat_4():
    s1=0
    s2=0
    s3=0
    k1=0
    k2=0
    k3=0
    for i in range(100,999):
        s1=i%10
        k1=i//10
        s2=k1%10
        k2=k1//10
        s3=k2%10
        k3=k2//10
        if s1!=s2 and s1!=s3 and s2!=s3:
            print(i)

def feladat_5(n):
    db=0
    max=0
    for i in range(1,n+1):
        s=0
        for j in range(1,i+1):
            if i%j==0:
                s += 1
            if s>=max:
                max=j
    print(max)

def feladat_6(a,b):
    a=str(a)
    b=str(b)
    x=list(a)
    y=list(b)
    v=0
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                v += 1
    if v>0:
        print('A ket szam rokon.')
    else:
        print('A ket szam nem rokon.')

def feladat_7(a,b):
    sum_a=0
    sum_b=0
    for i in range(1,a):
        if a%i==0:
            sum_a=sum_a+i
    for j in range(1,b):
        if b%j==0:
            sum_b=sum_b+j
    if sum_a==b and sum_b==a:
        print("Ez a ket szam barat.")
    else:
        print("Ez a ket szam nem barat.")

def feladat_8(n):
    db=0
    x=1
    while x<n:
        x=x+1
        db=db+1
    print(db)

def feladat_9():
    paszuj=1
    x=2
    perc=0
    asd=1
    while True:
        asd =+ paszuj//x
        paszuj=asd
        x += 1
        perc += 1
        if paszuj>=300:
            print(perc)

def feladat_19():
    try:
        fajl=open("be.txt",mode='r')
        max=0
        for sor in fajl:
            sor=sor.strip()
            sor=sor.split(' ')
            cim=sor[0]
            szam=int(sor[1])
            if szam>max:
                max=szam
                tmp=cim
        print(tmp)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_20():
    try:
        fajl=cod.open("be.txt",encoding='utf-8', mode='r')
        s = 0
        for sor in fajl:
            sor=sor.strip()
            sor=sor.split(';')
            lakossag=int(sor[2])
            if lakossag>s:
                s=lakossag
                tmp=sor[0]
        print(tmp)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_21():
    try:
        fajl=open('be.txt',mode='r')
        fajl2=open('ki.txt', mode='w')
        for sor in fajl:
            s = 0
            sor=sor.strip()
            sor=sor.split(';')
            nev=sor[0]
            for i in range(1,len(sor)):
                s=s+int(sor[i])
            fajl2.write("%s %d\n" % (nev,s))
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_22():
    try:
        fajl = open("be.txt", mode='r')
        fajl2 = open('ki.txt', mode='w')
        m = 100  # minimum
        for sor in fajl:
            sor = sor.strip()
            sor = sor.split(';')
            nev=sor[0]
            eredm=float(sor[2])
            if eredm<m:
                m=eredm
                tmp=nev
        fajl2.write(tmp)
    except Exception as e:
        print(e)
    finally:
        fajl.close()
        fajl2.close()

def main():
    feladat_1(10)
    feladat_2(5)
    feladat_3(513)
    feladat_4()
    feladat_5(7)
    feladat_6(123, 123)
    feladat_7(220,284)
    feladat_8(5)
    feladat_9()
    feladat_19()
    feladat_20()
    feladat_21()
    feladat_22()
main()