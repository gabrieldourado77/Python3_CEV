
from math import trunc
from random import randint

t = 'Exercício 58 - Jogo da Adivinhação v2.0'

print('='*50)
print('{:^50}'.format(t))
print('='*50)

aleat = randint(0,10)
i = 0
num = 0
p = 0

print('Pensei em um número, entre 0 e 10.\nConsegue adivinhar qual foi?')
print('='*50)

while num != aleat:
    num = trunc(float(input('Palpite: ')))
    p += 1

print('='*60)
print('Parabéns! O número que eu tinha pensado era {}.'.format(aleat))
print('Você precisou de {} palpite(s) para acertar.'.format(p))
print('='*60)
