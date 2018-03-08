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

def main():
    feladat_1(10)
    feladat_2(5)
    feladat_3(513)
    feladat_4()
    feladat_5(7)
    feladat_9()
main()