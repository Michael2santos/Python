#Receber valor em metros e converter em centimetros e milimetros
metro = int(input('Digite quantos metros tem: '))
cent = metro * 100 #centimetros
mili = metro * 1000 #milimetros
print('{} metros tem {:.0f} centímetros'.format(metro, cent))
print('{} metros tem {:.0f} milímetros'.format(metro, mili) )
