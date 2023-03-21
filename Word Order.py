#Taking multiline input
n=int(input())
array=[]
for i in range(n):
    words= input()
    array.append(words)
    
#Print distinct words
array1=[]
[array1.append(x) for x in array if x not in array1]
print(len(array1))


#Counting distinct elements
for j in array1:
    occ=array1.count(j)
    print(occ,end='')


