#Receber altura e largura imprimir m² e dizer qtde de tinta necessaria
altura = float(input('Digite a altura: '))
largura= float(input('Digite a largura: '))
area = altura * largura
tinta = area / 2
print('Sua área é de {:.2f} m² '.format(area))
print('E você irá precisar de {:.2f} litros de tinta para essa área'.format(tinta))
