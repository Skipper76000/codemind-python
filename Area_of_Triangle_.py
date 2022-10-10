import math
a,b,c=map(int,input().split())
sq=(a+b+c)/2
area=math.sqrt(sq*(sq-a)*(sq-b)*(sq-c))
print("%.2f"%area)