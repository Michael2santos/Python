from math import sqrt
#Receber comprimento do cateto oposto.
#e do cateto adjacente.
# de um triangulo retangulo .e calcule a hipotenusa
#math.hypot
#.(x, y)sqrt(x*x + y*y)
#A² = B² + C²
#hipotenusa = (ca ** 2 + co ** 2) ** (1/2)
#hipotenusa = math.hypot(ca, co)
print('Calculcando a Hipotenusa')
oposto = float(input('Digite a medida do Cateto Oposto: '))
adjac = float(input('Digite a medida do Cateto adjacente: '))
total = sqrt(oposto * oposto + adjac * adjac)
print('A Hipotenusa é igual a {:.2f}'.format(total))