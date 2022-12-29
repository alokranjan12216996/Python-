def factorial_with_while_loop(n):
    if isinstance(n,int) and n >= 0: 
        if n == 0: 
            return 1
        else:
            factorial = 1
            while n > 1: 
                factorial = factorial * n
                n = n - 1
            return factorial
    else: 
        return "Not valid input"

print(factorial_with_while_loop(3))
print(factorial_with_while_loop(5))
print(factorial_with_while_loop(8))
print(factorial_with_while_loop(12))
