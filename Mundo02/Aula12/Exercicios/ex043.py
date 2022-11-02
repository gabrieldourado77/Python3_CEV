
t = 'Exercício 43 - IMC'

print('='*30)
print('{:^30}'.format(t))
print('='*30)

p = float(input('Peso em Kg: '))
a = float(input('Altura em metros: '))
imc = p / a**2

print('='*30)
print('IMC: {:.2f}'.format(imc))
print('Status: ',end='')

if imc < 18.5:
    print('abaixo do peso.')
elif imc < 25:
    print('peso ideal.')
elif imc < 30:
    print('sobrepeso.')
elif imc < 35:
    print('obesidade grau I.')
elif imc <= 40:
    print('obesidade grau II.')
else:
    print('obesidade grau III')

print('='*60)

