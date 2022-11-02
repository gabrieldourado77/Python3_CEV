
from math import trunc

t = 'Exercício 61 - Progressão Aritmética v2.0'

print('='*50)
print('{:^50}'.format(t))
print('='*50)

primeiro = trunc(float(input('Primeiro termo: ')))
razao = trunc(float(input('Razão: ')))
termo = 0  # Valores que serão mostrados
i = 1  # Variável contadora

if razao != 0:
    
    # A variável "termo" recebe o 1º termo da P.A.
    termo = primeiro

    print('='*45)
    print('P.A. - ', end='')

    while i <= 10:
        print('{} '.format(termo), end='')
        termo += razao
        i += 1

    print('\n'+'='*60)

else:
    print('='*60)
    print('A razão não pode ser zero!\nTente novamente.')
    print('='*60)
