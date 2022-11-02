
# O código com o While True, não funcionou, mesmo estando correto.
# Então, resolvi utilizar o laço de repetição FOR, no lugar dele.
# Por isso, a resolução ficou diferente, do que estava no enunciado.

from math import trunc

t = 'Exercício 69 - Ánalise de Dados'

print('='*45)
print('{:^45}'.format(t))

c = 0
idade = 0
sexo = ''
quantMaisDe18 = 0
quantHomens = 0
quantMulheres = 0
mulheresMenosDe20 = 0

for c in range(0,3):
    
    print('='*45)
    print(f'Cadastre a {c + 1}ª pessoa')
    idade = trunc(float(input('Idade: ')))
    sexo = input('Sexo (M/F): ').strip().upper()

    if idade > 18:
        quantMaisDe18 += 1
    
    if sexo == 'M':
        quantHomens += 1
    else:
        quantMulheres += 1
    
    if sexo == 'F' and idade < 20:
        mulheresMenosDe20 += 1


print('='*60)
print(f'Quantidade de pessoas cadastradas: {c+1}')
print(f'Quantidade de pessoas, com mais de 18 anos: {quantMaisDe18}')
print(f'Quantidade de homens: {quantHomens}')
print(f'Quantidade de mulheres: {quantMulheres}')
print(f'Quantidade de mulheres, com menos de 20 anos: {mulheresMenosDe20}')
print('='*60)
