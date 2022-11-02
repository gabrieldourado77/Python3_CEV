
t = 'Exercício 53 - Palíndromo'

print('='*40)
print('{:^40}'.format(t))
print('='*40)


f = input('Digite uma frase: ').strip()
fJunto = ''.join(f.lower().split())

# Resolução com Fatiamento
# Coloquei um índice, que vai do ínicio (caracter 0) até o fim (que não foi definido).
# Depois, usei o incremento -1, para ser gerada uma frase invertida, pegando da última letra até a primeira.

fInverso = fJunto[::-1]


print('='*60)
print('A frase: "{}", '.format(f), end='')

# Se as duas frases forem iguais, temos um palíndromo
if fJunto == fInverso:
    print('é um palíndromo.')
else:    
    print('não é um palíndromo.')

print('='*60)
