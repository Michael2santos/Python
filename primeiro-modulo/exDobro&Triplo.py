from math import sqrt
print('Calcular Dobro, Triplo e Raiz Quadrada')
number = int(input('Digite um número: '))
dobro = number * 2
triplo = number * 3
raiz = sqrt(number)
print('O dobro de {} é {}'.format(number, dobro))
print('O Triplo de {} é {}'.format(number, triplo))
print('A raiz quadrada de {} é {:.2f}'.format(number,raiz))
#raiz quadrada pode ser calculada numero ** (1/2) ou pow(numero,(1/2))