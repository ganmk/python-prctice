import sys
def d():
    def f(n):
        c=list(n[::])
        return c
    for i in range(100,100000):
        d=f(str(i))
        s=0
        for j in d:
            s+=pow(int(j),len(d))
        if(s==int(i)):
            print("%d"%s)
d()
