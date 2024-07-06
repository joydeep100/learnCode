# passing other functions as arguments to some function.
def sum(n, fun):
    total = 0
    for i in range(1,10):
        total+= fun(n)
    return total

def square(x):
    return x*x

print(sum(10, square)) # 900