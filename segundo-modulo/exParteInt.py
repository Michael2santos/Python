#Ler numero real e mostrar somente sua parte inteira
from math import trunc
number = float(input('Digite um numero real: '))
print('O número digitado foi {}\nE sua parte inteira é {}'.format(number, trunc(number)))