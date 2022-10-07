a=int(input())
l=len(str(a))
sq=a**2
ld=sq%pow(10,l)
if a==ld:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")