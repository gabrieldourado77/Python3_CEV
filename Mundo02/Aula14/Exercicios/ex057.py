
t = 'Exercício 57 - Validação'

print('='*40)
print('{:^40}'.format(t))
print('='*40)

s = ''

while s != 'M' and s !='F':
    s = input("Digite o seu sexo [M/F]: ").strip().upper()  

print('='*60)

if s == 'M':
    print('Você é um homem.')
else:
    print('Você é uma mulher.')

print('='*60)
