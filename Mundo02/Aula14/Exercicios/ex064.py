
t = 'Exercício 64 - Tratando Vários Valores v1.0'

print('='*50)
print('{:^50}'.format(t))
print('='*50)

num = 0
soma = 0
i = 0

while num != 999:

    num = float(input('{}º número: '.format(i+1)))
    soma += num
    i += 1

# Desconsiderei o último valor digitado, que é o 999
i = i - 1
soma = soma - 999

print('='*60)
print('Você digitou {} número(s)'.format(i))
print('A soma entre eles é: {:.2f}'.format(soma))
print('='*60)
