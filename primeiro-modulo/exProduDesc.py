#Receber valor do produto e calcular novo preço com 5% desconto
prod = float(input('Qual o valor do produto? '))
novoPreco = prod - (prod * 5 / 100)
print('O produto com 5% de desconto vai sair a {:.2f} Reais'.format(novoPreco))