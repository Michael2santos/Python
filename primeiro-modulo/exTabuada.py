#Ler numero inteiro e exibir tabuada do mesmo
number = int(input('Digite um número: '))
cont = 1
while cont <= 10:
    result = number * cont
    print('{} X {} = {}'.format(number, cont,result))
    cont += 1
