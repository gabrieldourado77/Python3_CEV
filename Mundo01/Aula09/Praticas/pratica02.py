
t = 'Análise'

print('='*45)
print('{:^45}'.format(t))

f = 'Curso em Vídeo Python'

print('='*45)
print('Frase: {}'.format(f))
print('='*45)

print('Quantidade de caracteres: {}'.format(len(f)))
print('='*45)
print('Quantidade de letras "e": {}'.format(f.count('e',6,8)))
print('Quantidade de letras "o": {}'.format(f.count('o',0,14)))
print('Quantidade de letras "d": {}'.format(f.count('d',6,11)))
print('='*45)
