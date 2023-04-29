from math import sqrt

a = float(input('Coeficiente A: '))
b = float(input('Coeficiente B: '))
c = float(input('Coeficiente C: '))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print('Não possui raizes reais.')

else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    
    if delta == 0:
        print(f'A equação possui uma raiz real: {x1}')
    
    else:
        x2 = (-b - sqrt(delta)) / (2 * a)
        
        print(f"x' = {x1}")
        print(f"x'' = {x2}")
