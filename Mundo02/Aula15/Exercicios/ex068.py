
from random import randint
from math import trunc

t = 'Exercício 68 - Ímpar ou Par'

print('='*40)
print('{:^40}'.format(t))
print('='*40)

aleat = 0
num = 0
esc = ''
soma = 0
vitorias = 0
derrotas = 0

while True:

    aleat = randint(0,10)
    num = trunc(float(input('Escolha um número de 0 a 10: ')))

    if num >= 0 and num <= 10:

        esc = input('Ímpar ou Par (I ou P)? ').strip().upper()

        if esc != 'I' and esc != 'P':
            while esc != 'I' and esc != 'P':
                print('='*50)
                print('Opção inválida!')
                esc = input('Ímpar ou Par (I ou P)? ').strip().upper()

        print('='*50)
        print(f'Você escolheu: {num} e o computador escolheu: {aleat}')
        soma = num + aleat

        if esc == 'I':

            if soma % 2 == 1:
                print(f'{num} + {aleat} = {soma} (Ímpar)\nVocê venceu!')
                vitorias += 1
            else:
                print(f'{num} + {aleat} = {soma} (Par)\nVocê perdeu!')
                derrotas += 1
                break
                
            print('='*50)

        elif esc == 'P':
                
            if soma % 2 == 0:
                print(f'{num} + {aleat} = {soma} (Par)\nVocê venceu!')
                vitorias += 1
            else:
                print(f'{num} + {aleat} = {soma} (Ímpar)\nVocê perdeu!')
                derrotas += 1
                break

            print('='*50)

    else:
        print('='*50)
        print('Número inválido!')

print('='*60)
print(f'Total de vitórias: {vitorias}')
print(f'Total de derrotas: {derrotas}')
print('='*60)
