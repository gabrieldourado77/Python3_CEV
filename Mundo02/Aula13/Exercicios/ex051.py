
from math import trunc

t = 'Exercício 51 - Progressão Aritmética'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

primeiro = trunc(float(input('Primeiro termo da P.A.: ')))
razao = trunc(float(input('Razão da P.A.: ')))

decimo = 0 # Décimo termo da P.A.

if razao != 0:

    # Cálculo do Enésimo Termo de uma P.A.
    # Fórmula: 1º termo + (a posição do termo, que eu quero encontrar - 1) * a razão da P.A.
    decimo = primeiro + (10 - 1) * razao
    
    print('='*45)
    print('P.A. - ', end='')

    for c in range(primeiro, decimo + razao, razao):
        print('{} '.format(c), end='')

    print('\n'+'='*60)

else:
    print('='*60)
    print('A razão não pode ser zero!\nTente novamente.')
    print('='*60)
