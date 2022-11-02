
from datetime import date

t = 'Exercício 39 - Alistamento Militar'

print('='*50)
print('{:^50}'.format(t))
print('='*50)

nasc = int(input('Digite o seu ano de nascimento: '))
atual = date.today().year
i = atual - nasc

print('='*60)
print('Idade: {} anos.'.format(i))

if i < 18:
    tempo = 18 - i
    alist = atual + tempo

    print('Ainda falta(m) {} ano(s) para o seu alistamento.'.format(tempo))
    print('Ano do alistamento: {}'.format(alist))
elif i == 18:
    print('Chegou a hora de você se alistar.')
else:
    tempo = i - 18
    alist = atual - tempo

    print('O seu alistamento foi em {}'.format(alist))
    print('Você deveria ter se alistado a {} ano(s) atrás'.format(tempo))

print('='*60)
