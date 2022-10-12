
from random import randint
from math import trunc
from time import sleep

t = 'Desafio 28 - Jogo da Adivinhação'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

r = randint(0,5)

num = trunc(float(input('Digite um número de 0 a 5: ')))

print('='*45)
print('Processando...')
print('='*45)

sleep(2)

if num == r:
    print('Parabéns, você acertou!\nO número escolhido era {}'.format(r))
else:
    print('Você perdeu!\nO número escolhido era {}'.format(r))
print('='*60)
