print('Digite os dados para ver o valor a pagar!')
km = float(input('Quantos KMs você rodou? '))
dias = int(input('Quantos dias você ficou com o carro? '))
valorkm = km * 0.15
valordia = dias * 60
total = valorkm + valordia
print('{} Kms e {} dias, o valor a pagar será de {} R$'.format(km,dias,total))
