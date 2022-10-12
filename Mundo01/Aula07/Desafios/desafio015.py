
t = 'Aluguel de Carros'
custodia = 60.00
custokm = 0.15

print('='*45)
print('{:^45}'.format(t))
print('='*45)

dias = int(input('Quantidade de dias: '))
print('='*45)
km = float(input('Quantidade de Km percorridos: '))
print('='*45)

aluguel = dias * custodia + km * custokm

print('Valor do Aluguel: R$ {:.2f}'.format(aluguel))
print('='*45)

