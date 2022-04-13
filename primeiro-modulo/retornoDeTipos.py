valor = input('Digite algo para ser analisado: ')
print('O tipo primitivo desde dado é:',type(valor))
print('É alphanumerico ?',valor.isalnum())
print('Contém letras?',valor.isalpha())
print('Contém letras minusculas?',valor.islower())
print('Contém números?',valor.isnumeric())
print('Contém letras maiusculas?',valor.isupper())
print('Contém espaços?',valor.isspace())

#.istitle quando tem letras maiusculas e minusculas na mesma palavra