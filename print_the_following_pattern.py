n=int(input())
no=65+n-1
for i in range(1,n+1):
    for j in range(1,n+2-i):
        ch=chr(no)
        print(ch,end=' ')
    print()
    no=no-1