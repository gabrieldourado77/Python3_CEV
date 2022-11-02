
from random import choice
from time import sleep


t = 'Exercício 45 - Pedra, Papel e Tesoura'

print('='*50)
print('{:^50}'.format(t))
print('='*50)

esc = ['pedra','papel','tesoura']

print('Digite:\n[1] Pedra\n[2] Papel\n[3] Tesoura')
print('='*30)
op = input('Opção: ')

print('='*35)

if op == '1' or op == '2' or op == '3':

    if op == '1':
        op = 'pedra'
    elif op == '2':
        op = 'papel'
    else:
        op = 'tesoura'

    esc = choice(esc)

    print('Jo')
    sleep(0.5)
    print('ken')
    sleep(0.5)
    print('pô!')
    sleep(0.5)
    print('='*35)

    print('O usuário escolheu: {}\nO computador escolheu: {}'.format(op,esc))
    print('='*35)

    if op == esc:
        print('Empate')

    elif op == 'pedra' and esc == 'tesoura':
        print('A pedra venceu a tesoura')

    elif op == 'pedra' and esc == 'papel':
        print('O papel venceu a pedra')

    elif op == 'papel' and esc == 'pedra':
        print('O papel venceu a pedra')

    elif op == 'papel' and esc == 'tesoura':
        print('A tesoura venceu o papel')

    elif op == 'tesoura' and esc == 'pedra':
        print('A pedra venceu a tesoura')

    else:
        print('A tesoura venceu o papel')    

else:
    print('Opção inválida! Tente novamente.')

print('='*60)
