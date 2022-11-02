
from math import trunc

t = "Exercício 36 - Aprovando um Empréstimo"

print('='*50)
print('{:^50}'.format(t))
print("="*50)

casa = float(input('Digite o valor da casa: R$ '))
sal = float(input('Digite o salário do comprador: R$ '))
anos = trunc(float(input('Em quantos anos, o empréstimo será pagado? ')))

prest = casa / (anos*12)
limite = sal * (30/100)

print('='*55)
print('Valor da Prestação: R$ {:.2f}'.format(prest))

if prest <= limite:
    print('='*55)
    print('O empréstimo foi aprovado!')
else:
    print('='*55)
    print('O empréstimo foi negado!')
    print('O valor da prestação, não pode exceder 30% do salário.')
    
print('='*60)
