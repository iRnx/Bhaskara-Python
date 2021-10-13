def bhaskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)

    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    return delta, x1, x2


a = int(input('Valor de (A): '))
b = int(input('Valor de (B): '))
c = int(input('Valor de (C): '))
resp = bhaskara(a, b, c)
lista = list()
for c in resp:
    lista.append(c)
print(f'O valor de DELTA é: {lista[0]}')
print(f'O valor de X1 é: {lista[1]}')
print(f'O valor de X2 é: {lista[2]}')
