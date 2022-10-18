
t = 'Reajuste Salarial'

print('='*50)
print('{:^50}'.format(t))
print('='*50)

s = float(input('Digite o salário do funcionário: R$ '))
ns = s + (s*(15/100))

print('='*50)
print('Aumento salarial: 15%')
print('Salário com aumento: R$ {:.2f}'.format(ns))
print('='*50)
