
from math import trunc

t = 'Exercício 56 - Analisador Completo'

print('='*40)
print('{:^40}'.format(t))
print('='*40)

somaIdade = 0
mediaIdade = 0
maiorIdade = 0
homemMaisVelho = ''
quantMulheres = 0

for cont in range(0,4):
    print('Dados da {}ª pessoa'.format(cont+1))
    n = input('Nome: ').strip()
    i = trunc(float((input('Idade: '))))
    s = input('Sexo (F ou M): ').strip().upper()
    print('='*60)

    somaIdade += i

    if s == 'M':
        if cont == 0:
            maiorIdade = i
            homemMaisVelho = n

        elif i > maiorIdade:
            maiorIdade = i
            homemMaisVelho = n
    
    elif s == 'F' and i < 20:
        quantMulheres += 1


mediaIdade = somaIdade / 4

print('Média da Idade do Grupo: {:.2f} anos.'.format(mediaIdade))
print('Homem mais velho: {}, com {} anos.'.format(homemMaisVelho, maiorIdade))
print('Quant. de mulheres com menos de 20 anos: {}'.format(quantMulheres))
print('='*60)
