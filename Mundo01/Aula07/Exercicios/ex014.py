
t = 'Conversor de Temperaturas'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

c = float(input('Temperatura em graus Celsius: '))

f = c * 1.8 + 32

print('='*45)
print('Temperatura em graus Fahrenheit: {:.2f}°F'.format(f))
print('='*45)

