
from time import sleep

t = 'Exercício 59 - Menu'

print('='*40)
print('{:^40}'.format(t))
print('='*40)

num = [0.0, 0.0]
op = ' '
soma = 0
mult = 0
maior = 0

for c in range(0,2):
        num[c] = float(input('Digite o {}º número: '.format(c+1)))

while op != '5':

    print('='*50)
    print('Menu')
    print('[1] Somar\n[2] Multiplicar\n[3] Maior número')
    print('[4] Adicionar novos números\n[5] Sair')
    print('='*50)
    op = input('Opção: ').strip()
    print('='*50)

    if op == '1':
        soma = num[0] + num[1]
        print('Soma: {:.2f} + {:.2f} = {:.2f}'.format(num[0], num[1], soma))
        break

    elif op == '2':
        mult = num[0] * num[1]
        print('Multiplicação: {:.2f} X {:.2f} = {:.2f}'.format(num[0], num[1], mult))
        break

    elif op == '3':
        if num [0] > num[1]:
            maior = num[0]
            print('O maior número é o {:.2f}.'.format(maior))
        
        elif num[1] > num[0]:
            maior = num[1]
            print('O maior número é o {:.2f}.'.format(maior))
        
        else:
            print('Os dois números são iguais.')
        
        break

    elif op == '4':
        for c in range(0,2):
            num[c] = float(input('Digite o {}º número: '.format(c+1)))
    
    elif op == '5':
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida! Tente novamente.')
        sleep(1)

print("="*60)
