# Fibonacci series 0,1,1,2,3,5,8...
# basic approach
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# using memoization


def fibdp(n, computed={0: 1, 1: 1}):

    if n not in computed:
        computed[n] = fibdp(n-1) + fibdp(n-2)

    return computed[0]


print(fibdp(5))

# factorial 5! = 5*4*3*2*1 ; 0! = 1 , 1! = 1


def fact(n):
    if (n < 0):
        return None    # note factorial of -ve numbers do not exist
    if (n >= 0 and n <= 1):
        return 1
    else:
        return n * fact(n-1)


print(fact(5))  # 120
print(fact(-20))  # None
