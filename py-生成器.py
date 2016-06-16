g=[i + 1 for i in range(10)]
l=[]
for j in g:
     l.append(j)
print l#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

[i + 1 for i in range(10) if i % 2]#满足条件的生成器

g = (i + 1 for i in range(10) if i % 2)
l = []
for j in g:
     l.append(j)
print l#[2, 4, 6, 8, 10]
