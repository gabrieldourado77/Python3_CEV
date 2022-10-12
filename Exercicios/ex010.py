
t = 'Conversor de Moedas'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

r = float(input('Quanto dinheiro você tem na sua carteira?\nR$ '))
cotacao = 3.27

print('='*45)
print('Cotação do dólar: 3,27')
print('='*52)
print('Com {:.2f} reais,'.format(r),end=" ") 
print('você pode comprar {:.3f} dólares'.format(r/cotacao))
print('='*52)

