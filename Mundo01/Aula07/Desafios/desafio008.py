
t = 'Conversor de Medidas'

print('='*35)
print('{:^35}'.format(t))
print('='*35)

v = float(input('Digite uma medida em metros: '))

print('='*70)
print('{:.2f} metros equivale a'.format(v),end=' ') 
print('{:.2f} centimetros e {:.2f} milimetros'.format(v*100, v*1000))
print('='*70)


