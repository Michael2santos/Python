nome = str(input('Digite seu nome completo: ')).strip()
print('Nome em Maiusculas:',nome.upper())
print('Nome em Minusculas: ',nome.lower())
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
teste = nome.split()
print('Primeiro nome tem:',len(teste[0]),'Letras')
