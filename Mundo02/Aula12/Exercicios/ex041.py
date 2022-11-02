
from datetime import date

t = 'Exercício 41 - Classificando Atletas'

print('='*50)
print('{:^50}'.format(t))
print('='*50)

nasc = int(input('Ano de nascimento: '))
atual = date.today().year
i = atual - nasc

print('='*60)
print('Idade: {} anos'.format(i))

if i <= 9:
    print('Categoria: Mirim')
elif i <= 14:
    print('Categoria: Infantil')
elif i <= 19:
    print('Categoria: Júnior')
elif i <= 25:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')

print('='*60)
