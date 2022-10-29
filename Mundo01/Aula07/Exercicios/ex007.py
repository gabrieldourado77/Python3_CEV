
titulo = 'Média do Aluno'

print('='*35)
print('{:=^35}'.format(titulo))
print('='*35)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

print('='*25)
print('Média do Aluno: {:.2f}'.format((n1+n2)/2))
print('='*35)

