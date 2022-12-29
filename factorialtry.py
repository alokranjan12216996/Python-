n=int(input("enter the number"))
ans=1
while n>1:
    ans *=n
    n=n-1
    print("factorial",ans)