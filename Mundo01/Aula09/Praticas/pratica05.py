
t = 'Divisão'

print('='*45)
print('{:^45}'.format(t))

f = 'Curso em Vídeo Python'

print('='*45)
print('Frase: {}'.format(f))
print('='*60)

print('Divisão (Split): {}'.format(f.split()))
print('Junção (Join): {}'.format(''.join(f.split())))
print('Quantidade de letras: {}'.format(len(''.join(f.split()))))
print('='*60)
