number = int(input('Digite um numero inteiro ate 9999:'))
unidade = number // 1 %10
dezena = number //10 % 10
centena = number //100 %10
milhar = number // 1000 % 10
print(number,'tem',unidade, 'unidades')
print(number,'tem', dezena,'Dezenas')
print(number,'tem',centena,'centenas')
print(number,'tem',milhar,'milhar' )