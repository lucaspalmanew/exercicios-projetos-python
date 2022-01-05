vc = float(input('Qual o valor da casa? '))
vs = float(input('Qual o seu salário? '))
a = int(input('Em quantos anos você vai pagar? '))
vp = vc / (a * 12)
mínimo = vs * 30 / 100
if vp <= mínimo:
    print('A prestação mensal será de R${}!'.format(vp))
else:
    print('Seu empréstimo foi negado por ultrapassar 30% do seu salário mensal!')


