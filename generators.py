def gensquares(N):
    for i in range(N):
        yield i**2

g = gensquares(10)
print(next(g))

#generators2

def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n = int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print (",".join(values))


#generator3

n = int(input())
divisGenerator = (i for i in range(n))
for i in divisGenerator:
    if (i % 3 == 0) and (i % 4 == 0):
        print(i)


#generator4

a,b = int(input()), int(input())
squaresGenerator = (i * i for i in range(a, b))
for i in squaresGenerator:
    print(i)


#generator5

n = int(input())
listGenerator = (i for i in range(n, 0, -1))
for i in listGenerator:
    print(i)

    