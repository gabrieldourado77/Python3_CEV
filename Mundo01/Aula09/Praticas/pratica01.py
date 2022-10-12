
t = 'Fatiamento'

print('='*45)
print('{:^45}'.format(t))

f = 'Curso em Vídeo Python'

print('='*45)
print('Frase: {}'.format(f))
print('='*45)

print('Terceira letra: {}'.format(f[2]))
print('6º Caracter: {}'.format(f[5]))
print('Palavras: "{}", "{}", "{}" e "{}"'.format(f[:5],f[6:8],f[9:14],f[15:]))
print('='*45)
print('Fatia: {}'.format(f[9::2]))
print('Fatia: {}'.format(f[6::3]))
print('='*45)
