
t = 'Análise'

print('='*45)
print('{:^45}'.format(t))

f = 'Curso em Vídeo Python'

print('='*45)
print('Frase: {}'.format(f))
print('='*45)

print('Quantidade de letras "o": {}'.format(f.count('o',0,14)))
print('Encontrar "rso": {}'.format(f.find('rso')))
print('Encontrar "Android": {}'.format(f.find('Android')))
print('Essa frase tem a palavra "Curso"? {}'.format('Curso' in f))
print('='*45)
