import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

#case 1
if a == 0:
    if b == 0:
        if c ==0:
            print('infinite solutions')
        else:
            print('no solutions')
else:
    D = b**2 - 4*a*c

    if D < 0:
        print('no real solutions')

    elif D == 0:
        x = -b / (2*a)
        print(f'x = {x}')
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f'x1 = {x1}, x2 = {x2}')
