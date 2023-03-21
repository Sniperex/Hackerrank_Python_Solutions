happiness=0
n,m=input().split()
n,m=int(n),int(m)
array = [int(x) for x in input().split()]
A= set([int(x) for x in input().split()])
B= set([int(x) for x in input().split()])
for i in array:
    if i in A:
        happiness+= 1
    elif i in B:
        happiness-= 1
print(happiness)
