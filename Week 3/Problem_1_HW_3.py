n = int(input('n = '))
def my_factorial(n):
    if n == 0:
        return 1
    else:
        return n * my_factorial(n-1)

print(my_factorial(n))

