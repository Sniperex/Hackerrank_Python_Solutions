# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB=int(input())
BC=int(input())
AC=math.sqrt((AB**2)+(BC**2))
MC=AC/2
BM=MC
theta=math.acos((BC**2)/(2*BM*BC))

deg=math.degrees(theta)
deg1=round(deg)
degree=chr(176)                          
print(deg1,degree,sep='')