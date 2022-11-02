
t = 'Exercício 66 - Vários Números com Flag'

print('='*50)
print('{:^50}'.format(t))
print('='*50)

num = 0
soma = 0
i = 0

print('Digite alguns números ou 999 para sair')
print('='*50)

while True:

    num = float(input('{}º número: '.format(i+1)))
    
    if num != 999:
        soma += num
        i += 1
    else:
        break

print('='*60)
print(f'Você digitou {i} número(s)')
print(f'A soma entre eles é: {soma:.2f}')
print('='*60)
