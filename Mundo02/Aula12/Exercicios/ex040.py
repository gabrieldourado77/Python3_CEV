
from time import sleep

t = 'Exercício 40 - Média do Aluno'

print('='*40)
print('{:^40}'.format(t))
print('='*40)

nt01 = float(input('Digite a 1ª nota do aluno: '))
nt02 = float(input('Digite a 2ª nota do aluno: '))


if nt01 > 10 or nt02 > 10:
    print('Nota inválida! Tente novamente')
    print('='*60)
    
    nt01 = float(input('Digite a 1ª nota do aluno: '))
    nt02 = float(input('Digite a 2ª nota do aluno: '))

    m = (nt01 + nt02) / 2

    sleep(0.5)

    print('='*60)
    print('Média do aluno: {:.2f}'.format(m))

    if m < 5:
        print('Status: reprovado')
    elif m >= 5 and m < 7:
        print('Status: está de recuperação')
    elif m >= 7 and m <= 10:
        print('Status: aprovado')
    else:
        print('Ocorreu um erro! Tente novamente.')    
else: 
    m = (nt01 + nt02) / 2
    sleep(0.5)
    print('='*60)
    print('Média do aluno: {:.2f}'.format(m))
    
    if m < 5:
        print('Status: reprovado')
    elif m >= 5 and m < 7:
        print('Status: está de recuperação')
    elif m >= 7 and m <= 10:
        print('Status: aprovado')
    else:
        print('Ocorreu um erro! Tente novamente.')    

print('='*60)
