
txt = ['Exercício 47','Números pares, entre 1 e 50']

print('='*35)
print('{:^35}'.format(txt[0]))
print('='*35)
print('{:^35}'.format(txt[1]))
print('='*60)

for cont in range(0,25,2):
    print('{:^3} '.format(cont+2), end='')

print('\n')

for cont in range(26,50,2):
    print('{:^3} '.format(cont+2), end='')

print('\n'+'='*60)
