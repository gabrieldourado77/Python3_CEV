
from time import sleep

t = 'Exercício 70 - Estatísticas com Produtos'

print('='*50)
print('{:^50}'.format(t))

nome = ''
preco = 0
resp = ''
quantProdutos = 0
totalCompra = 0
quantMaisDe1000 = 0
maiorPreco = 0
menorPreco = 0
prodMaisCaro = ''
prodMaisBarato = ''

while True:

    print('='*50)
    print(f'{quantProdutos + 1}º Produto')
    nome = input('Nome: ').strip()
    preco = float(input('Preço: R$ '))
    print('='*50)

    quantProdutos += 1
    totalCompra += preco

    if preco > 1000:
        quantMaisDe1000 += 1
    
    if quantProdutos == 1:
        maiorPreco = preco
        menorPreco = preco
        prodMaisCaro = nome
        prodMaisBarato = nome
    
    elif preco > maiorPreco:
        maiorPreco = preco
        prodMaisCaro = nome
    
    elif preco < menorPreco:
        menorPreco = preco
        prodMaisBarato = nome


    resp = input('Quer continuar? (S/N) ').strip().upper()

    while resp != 'S' and resp != 'N':
        resp = input('Quer continuar? (S/N) ').strip().upper()

    if resp == 'N':
        print('='*50)
        print('Finalizando...')
        sleep(1)
        break


print('='*60)
print(f'Quantidade de produtos comprados: {quantProdutos}')

if quantMaisDe1000 == 1:
    print(f'Este produto custa mais de R$ 1000.00')
elif quantMaisDe1000 > 1:
    print(f'Há {quantMaisDe1000} produtos custando mais de R$ 1000.00')

if quantProdutos == 1:
    print(f'Nome do produto: {nome}')
else:
    print(f'Produto mais caro: "{prodMaisCaro}" de R$ {maiorPreco:.2f}')
    print(f'Produto mais barato: "{prodMaisBarato}" de R$ {menorPreco:.2f}')

print('='*60)
print(f'Total da compra: R$ {totalCompra:.2f}')
print('='*60)
