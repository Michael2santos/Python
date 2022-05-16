frase = str(input('Digite uma frase: ')).upper().strip()#upper letras maiusculas e strip remove espaços inicio e fim
print('Analisando a frase...')
print('A letra "A" aparece {} vezes na frase '.format(frase.count('A')))#conta qtde de A
print('A primeira letra "A" apareceu na {}° posição'.format(frase.find('A')+1))
print('A ultima letra "A" aparece na {}° posição'.format(frase.rfind('A')+1))