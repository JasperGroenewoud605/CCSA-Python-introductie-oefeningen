def fib(invoer):
    if invoer == 0 or invoer == 1:
        return invoer
    return fib(invoer-1) + fib(invoer-2)

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(20))