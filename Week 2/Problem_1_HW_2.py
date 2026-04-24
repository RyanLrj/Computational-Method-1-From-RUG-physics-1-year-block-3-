# question (a)
from operator import truediv

fibonacci = [1, 1]
for _ in range(18):
    next_number = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_number)

print(len(fibonacci))
print(fibonacci)

# question (b)

primonacci = []
for i in fibonacci:
    is_prime = True

    if i < 2:
        is_prime = False
    else:
        for divisor in range(2, i):
            if i % divisor == 0:
                is_prime = False

    if is_prime:
        primonacci.append(i)
print(primonacci)

# question (c)
fibonacci_while = [1, 1]

while len(fibonacci_while) < 20:
    next_number = fibonacci_while[-1] + fibonacci_while[-2]
    fibonacci_while.append(next_number)

primonacci_while = []
k = 0
while k < len(fibonacci_while):
    n = fibonacci_while[k]
    is_prime = True

    if n < 2:
        is_prime = False
    else:
        divisor = 2
        while divisor < n:
            if n % divisor == 0:
                is_prime = False
            divosor = divisor + 1

    if is_prime:
        primonacci_while.append(n)

    k = k + 1

print(fibonacci_while)
print(primonacci_while)



