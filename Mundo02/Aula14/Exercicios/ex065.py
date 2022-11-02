
t = 'Exercício 65 - Valores'

print('='*35)
print('{:^35}'.format(t))
print('='*35)

resp = ''
i = 0
fim = 2
num = 0
soma = 0
media = 0
maior = 0
menor = 0

while resp != 'N':

    for i in range(i,fim):
        num = float(input('Digite o {}º número: '.format(i+1)))
        soma += num

        if i == 0:
            maior = num
            menor = num

        elif num > maior:
            maior = num

        elif num < menor:
            menor = num

    print('='*40)
    print('Deseja continuar? (S/N)')
    resp = input('Resposta: ').upper()
    print('='*40)

    if resp == 'S':
        i += 1
        fim = i + 2

    elif resp == 'N':
        media = soma / (i+1)
        print('Você digitou {} números'.format(i+1))
        print('A média deles é: {:.2f}'.format(media))
        print('O maior valor é: {:.2f}'.format(maior))
        print('O menor valor é: {:.2f}'.format(menor))
        print('='*60)

    else:
        print('Resposta inválida! Tente novamente.')
        print('='*60)
        break
