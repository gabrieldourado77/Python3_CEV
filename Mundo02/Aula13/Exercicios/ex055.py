
t = 'Exercício 55 - Maior e Menor Peso'

print('='*40)
print('{:^40}'.format(t))
print('='*40)

maior = 0
menor = 0

for i in range(0,5):
    p = float(input('Peso da {}ª pessoa: '.format(i+1)))

    # Enquanto, só tiver um peso lido, esse peso será o maior e o menor.
    if i == 0:
        maior = p
        menor = p
    
    # Á partir do 2º peso lido, será verificado, qual é o maior e qual é o menor.
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p

print('='*60)
print('Maior peso lido: {:.2f}'.format(maior))
print('Menor peso lido: {:.2f}'.format(menor))
print('='*60)
