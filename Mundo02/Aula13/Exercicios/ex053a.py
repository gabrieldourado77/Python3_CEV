
t = 'Exercício 53 - Palíndromo'

print('='*40)
print('{:^40}'.format(t))
print('='*40)

f = input('Digite uma frase: ').strip()
fJunto = ''.join(f.lower().split())
fInverso = ''

print('='*60)
print('A frase: "{}", '.format(f), end='')

# O inicio, é a quantidade de letras da frase, menos 1, para o laço começar na última letra. 
# Considerando, que sempre deve ser um a menos, do que o total. Por exemplo, de 0 a 19.
# O fim é -1, porque esse valor será desconsiderado e o laço acabará no índice 0.
# O incremento é -1, para que seja gerada, uma frase invertida, indo de trás pra frente.

for letra in range(len(fJunto) - 1, -1, -1):
    # O laço irá da última letra até a primeira e uma frase invertida, será guardada em fInverso
    fInverso = fInverso + fJunto[letra]

# Se as duas frases forem iguais, temos um palíndromo
if fJunto == fInverso:
    print('é um palíndromo.')
else:    
    print('não é um palíndromo.')

print('='*60)
