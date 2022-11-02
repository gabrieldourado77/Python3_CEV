
t = 'Exercício 48'

print('='*35)
print('{:^35}'.format(t))
print('='*35)

s = 0

print('Soma dos números que:')
print('- Estão entre 1 e 500\n- São ímpares\n- São multíplos de 3')
print('='*35)

for i in range(1,501,2):
    if i % 3 == 0:
        s = s + i

print('Resultado da Soma: {}'.format(s))
print('='*60)
