n= int(input())
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)
for i in range(1,n):
    temp=i
    total_sum=0
    while(temp>0):
        total_sum+=factorial(temp%10)
        temp=int(temp/10)
    if(total_sum==i):
        print(i-1," ")