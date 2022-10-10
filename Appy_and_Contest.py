t=int(input())
while t!=0:
    cnt=0
    n,a,b,k=map(int,input().split())
    for i in range(1,n+1):
        if cnt==k:
            break
        if i%a==0 and i%b==0:
            continue
        if i%b==0 or i%a==0:
            cnt=cnt+1
    if cnt==k:
        print("Win")
    else:
        print("Lose")
    t=t-1