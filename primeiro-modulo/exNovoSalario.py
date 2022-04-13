#ler nome e salario atual e dar 15% de aumento
#wage = Salario
name = input('Digite o seu nome: ')
wage = float(input('Digite o seu sálario atual: '))

newWage = wage + (wage * 15 / 100)
print('{} seu sálario teve aumento de 15% e passou para {:.3f} Reais'.format(name, newWage))
