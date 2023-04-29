from math import sqrt

a = float(input('Raiz A: '))
b = float(input('Raiz B: '))
c = float(input('Raiz C: '))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print('Não possui raizes reais.')

elif delta == 0:
    x = -b / (2 * a)
    print(f'A equação possui uma raiz real: {x}')

else:  
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
   
    print(f"x' = {x1}")
    print(f"x'' = {x2}")