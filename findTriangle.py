lados = []
print()
print('APP CLASSIFICAÇÃO DE TRIÂNGULOS')
print()
print('Digite 3 valores inteiros para cada lado do triângulo:')
print()

v1 = None
while v1 is None:
    try:
        v1 = int(input('Entre o 1º lado:'))
    except ValueError:
        print('Porfavor digite um número inteiro.')

v2 = None
while v2 is None:
    try:
        v2 = int(input('Entre o 2º lado:'))
    except ValueError:
        print('Porfavor digite um número inteiro.')
   
v3 = None
while v3 is None:
    try:
        v3 = int(input('Entre o 3º lado:'))
    except ValueError:
        print('Porfavor digite um número inteiro.')           


lados.append(v1)
lados.append(v2)
lados.append(v3)
print(lados)


if lados[0] > (lados[1] and lados[2]):
    c = lados[0]

elif lados[1] > (lados[0] and lados[2]):
    c = lados[1]

else:
    c = lados[2]  

lados.remove(c)

if lados[0] > lados[1]:
    b = lados[0]

else:
    b = lados[1] 

lados.remove(b)
a = lados[0]

print(a)
print(b)
print(c)

if c < (a+b):
    if a == b:
        if a == c:
            print('Este triângunlo é EQUILÁTERO!')
        else:
            print('Este triângunlo é ISÓSCELES!')
    elif b == c:
        print('Este triângunlo é EQUILÁTERO!')
    else:
        if c^2 == (a^2 + b^2):
            print('Este triângunlo é ESCALENO RETÂNGULO!')
        else:
            print('Este triângunlo é ESCALENO!')
else:
    print('Não é um triângulo!')