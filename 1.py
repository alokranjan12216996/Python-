sum=0
arr=[5,1,2,3,7]
arr.sort()
for index,value in enumerate(arr):
    sum+=value*index
    print(sum)