soma = c = num = 0
while True:
    num = int(input('Qual tabuada você quer ver? '))
    if num < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num*c}')
    print('-' * 30)
print('*' * 30)
print('PROGRAMA ENCERRADO')
print('*' * 30)

