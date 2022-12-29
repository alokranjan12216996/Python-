n=8
while n>0:
    a=1
    b=1
    c=1
    count=2
    while count <n:
        c=a+b
        a=b
        b=c
        count+=1
    n-=1
    print("fibonacci of %d is %d",(n,c));