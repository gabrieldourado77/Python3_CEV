
from math import trunc
from time import sleep

t = 'Exercício 62 - Super Progressão Aritmética'

print('='*50)
print('{:^50}'.format(t))
print('='*50)

primeiro = trunc(float(input('Primeiro termo: ')))
razao = trunc(float(input('Razão: ')))

termo = 0  # Valor do termo, que será mostrado
i = 0  # Variável contadora
resp = ''
quantTermos = 9
maisTermos = 0

if razao != 0:

    while resp != 'N':

        # A variável "termo" recebe o 1º termo da P.A.
        termo = primeiro

        print('='*45)
        print('P.A. - ', end='')

        while i <= quantTermos:
            print('{} '.format(termo), end='')
            termo += razao
            i += 1

        print('\n'+'='*60)
        print('Deseja mostrar mais termos? (S/N)')
        resp = input('Resposta: ').upper()
        print('='*60)

        if resp == 'S':
            maisTermos = trunc(float(input('Quantos? ')))
            i = quantTermos
            # A quant. de termos recebe: ela mesma + quantos termos a mais, o usuário quer ver
            quantTermos += maisTermos

            while i < quantTermos:
                print('{} '.format(termo), end='')
                termo += razao
                i += 1
            
            print('\n'+'='*60)
            break

        elif resp == 'N':
            print('Finalizando...')
            sleep(1)
            print('='*60)

        else:
            print('Resposta inválida! Tente novamente.')
            print('='*60)
            break

else:
    print('='*60)
    print('A razão não pode ser zero!\nTente novamente.')
    print('='*60)
