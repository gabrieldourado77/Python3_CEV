
titulo = 'Dobro, Triplo e Raiz Quadrada'

print('='*35)
print('{:=^35}'.format(titulo))
print('='*35)

n = float(input('Digite um número: '))

print('='*25)
print('Dobro: {:.2f}\nTriplo: {:.2f}'.format(n*2,n*3))
print('Raiz Quadrada: {:.3f}'.format(n**(1/2)))
print('='*35)
