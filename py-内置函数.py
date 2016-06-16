#内置函数
#filter 
def f(x): return x % 2 != 0 and x % 3 != 0
a=filter(f, range(2, 25))
print a

#map
def cube(x): return x*x*x
a=map(cube, range(1, 11))
print a

#reduce
def add(x,y): return x+y
a=reduce(add, range(1, 11))
print a
