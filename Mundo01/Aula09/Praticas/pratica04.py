
t = 'Transformação'

print('='*45)
print('{:^45}'.format(t))

f01 = 'Curso em Vídeo Python'
f02 = '  Aprenda Python  '

print('='*45)
print('1ª Frase: {}'.format(f01))
print('='*45)

print('Reposicionamento: {}'.format(f01.replace('Python','Android')))
print('Letras maiúsculas: {}'.format(f01.upper()))
print('Letras minúsculas: {}'.format(f01.lower()))
print('"Capitalize": {}'.format(f01.capitalize()))
print('"Title": {}'.format(f01.title()))
print('='*45)

print('2ª Frase: {}'.format(f02))
print('='*45)
print('Sem os espaços: {}'.format(f02.strip()))
print('Sem os espaços da direita: {}'.format(f02.rstrip()))
print('Sem os espaços da esquerda: {}'.format(f02.lstrip()))
print('='*45)
