a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    if b>=c:
        print("min",c)
    else:
        print("min",b)
        print("max",a)
    if b>=c and b>=a:
            if c>=a:
                print("min",a)
    else:
        print("min",c)
        print("max",b)
    if c>=a and c>=b:
            if a>=b:
                print("min",b)
    else:
        print("min",a)
        print("max",c)

