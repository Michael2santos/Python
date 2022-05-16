#receber angulo.
#mostrar valor do seno,cosseno e tangente
import math
print('Digite o ângulo para Calcular ')
angulo = float(input('Qual o angulo:'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem seno {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o cosseno {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem a tangente {:.2f}'.format(angulo, tangente))


