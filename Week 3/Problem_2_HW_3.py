def my_factorial(n):
    if n == 0:
        return 1
    else:
        return n * my_factorial(n - 1)

t = int(input('terms of the taylor expansion = '))
x = float(input('x = '))
def taylor_sin(x, terms=t):
    result = 0

    for k in range(terms):
        numerator = (-1)**k * x**(2*k +1)
        denominator = my_factorial(2*k+1)
        result += numerator/denominator

    return result
print(taylor_sin(x))

