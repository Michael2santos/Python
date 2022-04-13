print('Nome e notas do aluno para calcular média')
nome = input('Digite o nome do aluno:')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print('{} Sua média foi: {}'.format(nome, media))