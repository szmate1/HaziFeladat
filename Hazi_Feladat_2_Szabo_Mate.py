def feladat_1(n):
    db=0
    for i in range(1,n+1):
        if n%i==0:
            db=db+1
    if db==4: #1,onmaga,+2
        print(True)
    else:
        print(False)

def main():
    feladat_1(10)
main()