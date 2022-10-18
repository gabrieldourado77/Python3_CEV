
t = 'Desafio 29 - Radar Eletrônico'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

v = float(input('Digite a velocidade do carro: '))

if v > 80:
    m = 7 * (v-80)
    print('='*45)
    print('Você será multado!\nValor da multa: R$ {:.2f}'.format(m))
elif v == 80:
    print('='*60)
    print('Cuidado! Você quase ultrapassou o limite de velocidade.')
else:
    print('='*45)
    print('Você está dentro do limite de velocidade.')
print('='*65)
