t= int(input())
c = []
for i in range(t):
    n= int(input())
    c.append(n)
c.sort()
set(c)
print(*c, sep='\n')
