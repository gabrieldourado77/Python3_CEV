
t = 'Exercício 44 - Gerenciador de Pagamentos'

print('='*50)
print('{:^50}'.format(t))
print('='*50)

preco = float(input('Preço do produto: R$ '))

print('='*50)
print('Escolha a forma de pagamento')
print('[1] Dinheiro\n[2] Cheque\n[3] Cartão de Crédito')
print('='*50)
op01 = input('Opção: ')

print('='*50)

if op01 == '1':
    print('O pagamento será á vista, em dinheiro.')
    novoPreco = preco - preco * (10/100)
    print('Preço do produto: R$ {:.2f}'.format(novoPreco))
    print('Desconto: 10%')

elif op01 == '2':
    print('O pagamento será á vista, em cheque.')
    novoPreco = preco - preco * (10/100)
    print('Preço do produto: R$ {:.2f}'.format(novoPreco))
    print('Desconto: 10%')

elif op01 == '3':
    print('Como você deseja pagar?')
    print('[1] Á vista\n[2] 2x no cartão\n[3] 3x ou mais no cartão')
    print('='*50)
    op02 = input('Opção: ')
    print('='*50)

    if op02 == '1':
        print('O pagamento será á vista.')
        novoPreco = preco - preco * (5/100)
        print('Preço do produto: R$ {:.2f}'.format(novoPreco))
        print('Desconto: 5%')
    
    elif op02 == '2':
        parc = preco / 2
        print('O pagamento será parcelado em 2x no cartão.')
        print('Preço do produto: R$ {:.2f}'.format(preco))
        print('Parcela: R$ {:.2f}'.format(parc))

    else:
        vezes = int(input('Deseja parcelar em quantas vezes? '))
        novoPreco = preco + preco * (20/100)
        parc = novoPreco / vezes

        print('='*50)
        print('O pagamento será parcelado em {}x no cartão.'.format(vezes))
        print('Preço do produto: R$ {:.2f}'.format(novoPreco))
        print('Parcela: R$ {:.2f}'.format(parc))
else:
    print('Opção inválida! Tente novamente.')
       
print('='*65)
        