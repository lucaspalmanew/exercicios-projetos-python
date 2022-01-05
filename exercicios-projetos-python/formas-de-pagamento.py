pn = float(input('Qual preço do produto: '))
print('''INFORMAÇÕES SOBRE O PAGAMENTO!!!
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] em até 2x no cartão
[ 4 ] em até 3x ou mais no cartão''')
opção = int(input('Qual a opção? '))
if opção == 1:
    total = pn - (pn * 10 / 100)
elif opção == 2:
    total = pn - (pn * 5 / 100)
elif opção == 3:
    total = pn
    parcela = total / 2
    print('Compra parcelada em 2x de R${}, SEM JUROS.'.format(parcela))
elif opção == 4:
    total = pn + (pn * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f}, COM JUROS.'.format(totparc, parcela))
else:
    total = 0
    print('Opção Inválida de pagamento')
print('Sua compra de R${} irá custar R${} no final'.format(pn, total))
